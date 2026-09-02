"""Headless eval runs for docs/eval.md. Needs the Cursor CLI `agent` on PATH.

  python tools/eval-run.py --dummy t1-nook --arm always-cheap --model <slug> --n 3
  python tools/eval-run.py --dummy t1-nook --arm routed --n 3           # no --model = Auto
  python tools/eval-run.py --phrasings                                  # docs/evals/phrasings.md

Each dummy run: copy the dummy to a temp dir, run the agent with this repo as --plugin-dir,
run the dummy's Red command, check the design-keep rule, write one trace file from
docs/evals/trace-fixture.md. Turns are 1 by construction (one prompt); tool calls are
counted from stream-json events.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DUMMIES = ROOT / "docs" / "evals" / "dummies"
TRACES = ROOT / "docs" / "evals" / "traces"
NATIVE = {"Read", "Grep", "Glob", "Shell", "StrReplace", "Write"}
RED = re.compile(r"^Red:\s*`([^`]+)`", re.M)


def agent_bin() -> str:
    exe = shutil.which("agent") or shutil.which("cursor-agent")
    if not exe:
        sys.exit("Cursor CLI `agent` not on PATH. Install: https://cursor.com/docs/cli (then rerun).")
    return exe


def run_agent(workspace: Path, prompt: str, model: str | None, mode: str | None = None) -> list[dict]:
    cmd = [agent_bin(), "-p", "--force", "--trust", "--output-format", "stream-json",
           "--workspace", str(workspace), "--plugin-dir", str(ROOT)]
    if model:
        cmd += ["--model", model]
    if mode:
        cmd += ["--mode", mode]
    cmd.append(prompt)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=workspace)
    events = []
    for line in proc.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            continue
    return events


def tool_calls(events: list[dict]) -> list[tuple[str, str]]:
    """(tool name, first path-ish arg) per tool_call event; tolerant of schema drift."""
    out = []
    for e in events:
        if "tool_call" not in json.dumps(e)[:200] and e.get("type") not in ("tool_call", "tool_use"):
            continue
        blob = json.dumps(e)
        name = e.get("name") or e.get("tool_name") or (e.get("tool_call") or {}).get("name") or ""
        if not name:
            m = re.search(r'"(?:name|tool_name|subtype)"\s*:\s*"([A-Za-z_]+)"', blob)
            name = m.group(1) if m else "?"
        m = re.search(r'"(?:path|file_path|filePath|pattern|command)"\s*:\s*"([^"]+)"', blob)
        out.append((name, m.group(1) if m else ""))
    return out


def design_kept(before: str, after: str, red_marker: str) -> bool:
    kept = [l for l in before.splitlines() if l.strip() and red_marker not in l]
    return all(l in after for l in kept)


def run_dummy(name: str, arm: str, model: str | None, n: int) -> None:
    src = DUMMIES / name
    task = (src / "EVAL-TASK.md").read_text(encoding="utf-8")
    red = RED.search(task)
    if not red:
        sys.exit(f"{name}/EVAL-TASK.md has no Red: `command` line")
    design_src = src / "docs" / "design.md"
    before = design_src.read_text(encoding="utf-8") if design_src.is_file() else ""
    TRACES.mkdir(parents=True, exist_ok=True)
    for i in range(1, n + 1):
        with tempfile.TemporaryDirectory() as d:
            ws = Path(d) / name
            shutil.copytree(src, ws)
            subprocess.run(["git", "init", "-q"], cwd=ws, check=False)
            events = run_agent(ws, task, model)
            calls = tool_calls(events)
            extra = [c for c in calls if c[0] not in NATIVE]
            success = subprocess.run(red.group(1), shell=True, cwd=ws).returncode == 0
            after = (ws / "docs" / "design.md").read_text(encoding="utf-8") if design_src.is_file() else ""
            kept = design_kept(before, after, "Coming soon.") if before else True
        stamp = dt.date.today().isoformat()
        trace = TRACES / f"{stamp}-{name}-{arm}-{i}.md"
        trace.write_text(
            "# Trace\n\n"
            f"- Dummy: {name}\n- Arm: {arm}\n- Date: {stamp}\n- Model (picker name): {model or 'Auto'}\n"
            "- Cost class: fill from the picker\n"
            f"- Success: {'yes' if success and kept else 'no'} (Red exit {'0' if success else 'non-zero'}; design keep {'ok' if kept else 'FAILED'})\n"
            "- User turns until accepted: 1 (headless, one prompt)\n"
            f"- Tool calls (total): {len(calls)}\n- Extra tool calls (not Grep/Glob/Read or the named native): {len(extra)}\n"
            "- Tokens in / out (optional; skip if the dashboard is missing): skipped\n"
            f"- Notes (one line): headless via tools/eval-run.py; extra={[c[0] for c in extra][:8]}\n",
            encoding="utf-8",
        )
        print(f"{trace.name}: success={success} kept={kept} calls={len(calls)} extra={len(extra)}")


def run_phrasings(model: str | None) -> int:
    rows = []
    for line in (ROOT / "docs" / "evals" / "phrasings.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and cells[0] not in ("Phrase", "---"):
            rows.append(cells)
    failures = 0
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d) / "t1-nook"
        shutil.copytree(DUMMIES / "t1-nook", ws)
        for phrase, expected in rows:
            events = run_agent(ws, phrase, model, mode="plan")
            read = {m.group(1) for _, p in tool_calls(events) for m in [re.search(r"skills[\\/]([^\\/]+)[\\/]SKILL\.md", p)] if m}
            ok = (not read) if expected == "none" else (expected in read)
            failures += not ok
            print(f"{'PASS' if ok else 'FAIL'}  {expected:<14} read={sorted(read) or '-'}  <- {phrase}")
    print(f"{len(rows) - failures}/{len(rows)} phrasings routed as expected")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dummy", default="t1-nook")
    ap.add_argument("--arm", default="routed", choices=("routed", "always-cheap", "always-frontier"))
    ap.add_argument("--model", help="picker slug; omit for Auto (the routed arm)")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--phrasings", action="store_true", help="run docs/evals/phrasings.md instead of a dummy")
    a = ap.parse_args()
    if a.phrasings:
        return run_phrasings(a.model)
    run_dummy(a.dummy, a.arm, a.model, a.n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
