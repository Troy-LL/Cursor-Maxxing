"""Unfurnished hard fences (ADR 007). stdin: Cursor hook JSON. stdout: permission JSON.

preToolUse Write  -> deny a full-file write to a non-empty durable owner (patch in place).
beforeShellExecution -> deny `git add` / `git commit` that would put scratch/ in history.
Anything else, or any error, allows (fail-open; the prose fence still stands).
"""
from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

OWNER_NAMES = {"README.md", "AGENTS.md", "CLAUDE.md"}
OWNER_RE = re.compile(r"(^|/)docs/(architecture|design|eval)\.md$|(^|/)docs/decisions/[^/]+\.md$")


def allow() -> None:
    print(json.dumps({"permission": "allow"}))


def deny(agent: str, user: str) -> None:
    print(json.dumps({"permission": "deny", "agent_message": agent, "user_message": user}))


def is_owner(raw: str, cwd: Path) -> bool:
    p = Path(raw)
    if not p.is_absolute():
        p = cwd / p
    if not p.is_file() or p.stat().st_size == 0:
        return False
    rel = p.as_posix()
    return p.name in OWNER_NAMES or bool(OWNER_RE.search(rel))


def git(cwd: Path, *args: str) -> str:
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def scratch_ignored(cwd: Path) -> bool:
    return subprocess.run(["git", "check-ignore", "-q", "scratch/x"], cwd=cwd, capture_output=True).returncode == 0


def touches_scratch(paths: str) -> bool:
    return any(line.strip().startswith("scratch/") for line in paths.splitlines())


def check_shell(command: str, cwd: Path) -> bool:
    """True when the command must be denied."""
    for segment in re.split(r"&&|\|\||;|\|", command):
        try:
            argv = shlex.split(segment.strip(), posix=True)
        except ValueError:
            argv = segment.split()
        if not argv or Path(argv[0]).name != "git":
            continue
        sub = next((a for a in argv[1:] if not a.startswith("-")), "")
        rest = argv[argv.index(sub) + 1 :] if sub else []
        if sub == "add":
            if any(a.split("/")[0] == "scratch" or a.startswith("scratch/") for a in rest):
                return True
            broad = any(a in (".", "-A", "--all", "-u", "--update", ":/") or a.endswith("/.") for a in rest)
            if broad and not scratch_ignored(cwd) and touches_scratch(
                git(cwd, "ls-files", "--others", "--modified", "--exclude-standard", "scratch")
            ):
                return True
        if sub == "commit":
            if touches_scratch(git(cwd, "diff", "--cached", "--name-only")):
                return True
            if any(a in ("-a", "--all") or (a.startswith("-") and not a.startswith("--") and "a" in a) for a in rest):
                if touches_scratch(git(cwd, "diff", "--name-only")):
                    return True
    return False


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        cwd = Path(payload.get("cwd") or (payload.get("workspace_roots") or ["."])[0])
        event = payload.get("hook_event_name", "")
        if event == "preToolUse" and payload.get("tool_name") == "Write":
            ti = payload.get("tool_input") or {}
            target = ti.get("path") or ti.get("file_path") or ti.get("filePath") or ""
            if target and is_owner(target, cwd):
                deny(
                    f"{target} is a living durable owner. Patch in place (StrReplace); never blank-replace. ADR 007.",
                    "Unfurnished: full-file write to a durable owner blocked. Patch in place.",
                )
                return 0
        elif event == "beforeShellExecution":
            if check_shell(payload.get("command", ""), cwd):
                deny(
                    "That git command would commit scratch/. scratch/ is thinking; keep it out of history (add it to .gitignore or unstage). ADR 007.",
                    "Unfurnished: git command touching scratch/ blocked.",
                )
                return 0
    except Exception as exc:  # fail-open; report on stderr for the Hooks channel
        print(f"fence: {exc}", file=sys.stderr)
    allow()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
