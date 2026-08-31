"""Deterministic contracts for the Cursor Maxxing pack. Rerun anytime."""
from __future__ import annotations

import argparse
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURSOR = ROOT / ".cursor"
PLUGIN = ROOT / ".cursor-plugin" / "plugin.json"

# Slots soft-off / other-pack yield must mute (model-invoked pack work).
SOFT_OFF_SLOTS = (
    "sdd",
    "sdd-eng",
    "verify",
    "grill",
    "blueprint",
    "ticket",
    "after-compact",
    "thermonuclear",
    "pre-flight",
    "evals",
    "write-skill",
)

SKILLS = (
    "after-compact",
    "blueprint",
    "cursormax",
    "deepen",
    "evals",
    "grill",
    "pre-flight",
    "sdd",
    "sdd-eng",
    "thermonuclear",
    "ticket",
    "verify",
    "write-skill",
)

COMMANDS = (
    "after-compact",
    "blueprint",
    "cursormax",
    "deepen",
    "evals",
    "grill",
    "keep",
    "pre-flight",
    "sdd",
    "sdd-eng",
    "thermonuclear",
    "ticket",
    "verify",
    "voice",
)

RULES = (
    "blast-radius.mdc",
    "cursormax-bias.mdc",
    "tdd.mdc",
    "yagni-bias.mdc",
    "yagni.mdc",
)


def text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def check(name: str, ok: bool, detail: str) -> dict:
    return {"id": name, "ok": ok, "detail": detail}


def run_checks(*, strict_install: bool) -> list[dict]:
    rows: list[dict] = []
    bias = text(CURSOR / "rules" / "cursormax-bias.mdc")
    after = text(CURSOR / "skills" / "after-compact" / "SKILL.md")
    keep = text(CURSOR / "commands" / "keep.md")
    occasion = text(CURSOR / "skills" / "sdd" / "occasion.md")
    sdd_eng = text(CURSOR / "skills" / "sdd-eng" / "SKILL.md")
    sdd = text(CURSOR / "skills" / "sdd" / "SKILL.md")
    cm = text(CURSOR / "skills" / "cursormax" / "SKILL.md")
    ref = text(CURSOR / "skills" / "cursormax" / "reference.md")
    agents = text(ROOT / "AGENTS.md")
    eval_md = text(ROOT / "docs" / "eval.md")
    t1_task = text(ROOT / "docs" / "evals" / "dummies" / "t1-nook" / "EVAL-TASK.md")
    t1_page = text(ROOT / "docs" / "evals" / "dummies" / "t1-nook" / "page.py")
    t1_design = text(ROOT / "docs" / "evals" / "dummies" / "t1-nook" / "docs" / "design.md")

    rows.append(
        check(
            "bias-file-on-disk",
            "File on disk" in bias and "Docs → sdd" not in bias,
            "cursormax-bias routes living owners to sdd-eng",
        )
    )
    rows.append(
        check(
            "bias-soft-off-slots",
            all(s in bias for s in SOFT_OFF_SLOTS),
            "soft-off / yield lists every model-invoked pack slot",
        )
    )
    rows.append(
        check(
            "bias-coexist-yield",
            "poteto" in bias.lower() or "another workflow" in bias.lower(),
            "bias yields when another workflow pack is driving",
        )
    )
    rows.append(
        check(
            "after-compact-default-on",
            "keep-off" in after and "If `scratch/keep-alive` is missing" not in after,
            "after-compact arms unless keep-off",
        )
    )
    rows.append(
        check(
            "keep-opt-out",
            "keep-off" in keep and "Default is on" in keep,
            "/keep off writes keep-off; default on",
        )
    )
    rows.append(
        check(
            "occasion-merge",
            "If the path already exists" in occasion
            and "full-file replace" in occasion.lower()
            and "**Write the owner.**" not in occasion,
            "occasion seats facts; bans full-file replace; no Write-the-owner step title",
        )
    )
    rows.append(
        check(
            "sdd-eng-disk-owner",
            "file already on disk" in sdd_eng.lower()
            and "Patch that owner" in sdd_eng
            and "full-file replace fails" in sdd_eng.lower(),
            "sdd-eng patches owners on disk; bans full-file replace",
        )
    )
    rows.append(
        check(
            "sdd-hands-off-existing",
            ("matching owner already" in sdd.lower() or "exists on disk" in sdd.lower())
            and "glossary / names dump" in sdd.lower(),
            "sdd hands living owners to sdd-eng; glossary is not a missing owner",
        )
    )
    rows.append(
        check(
            "bias-patch-living",
            "patch in place" in bias.lower() and "blank-replace" in bias.lower(),
            "always-on bias bans blank-replace of living durable files",
        )
    )
    distill = text(CURSOR / "skills" / "sdd" / "distill.md")
    owners = text(CURSOR / "skills" / "sdd" / "owners.md")
    adr002 = text(ROOT / "docs" / "decisions" / "002-first-shot-efficiency.md")
    rows.append(
        check(
            "distill-no-full-replace",
            "full-file replace" in distill.lower() and "patch in place" in distill.lower(),
            "distill merges non-empty owners with patches",
        )
    )
    rows.append(
        check(
            "no-glossary-occasion",
            "glossary" in occasion.lower()
            and "twin" in occasion.lower()
            and "| `docs/glossary.md`" not in occasion
            and "| docs/glossary.md" not in occasion,
            "occasion treats a glossary as a twin, not an owner",
        )
    )
    rows.append(
        check(
            "seat-user-name",
            "names a thing" in owners.lower()
            and "names a thing" in occasion.lower()
            and "glossary.md" in owners.lower(),
            "owners + occasion seat the user's name in the owner; no glossary file",
        )
    )
    rows.append(
        check(
            "ask-once-name",
            "ask once" in owners.lower() or "ask once" in occasion.lower(),
            "ambiguous names: one question, then seat",
        )
    )
    rows.append(
        check(
            "distill-fold-definitions",
            "glossary" in distill.lower() or "definitions" in distill.lower(),
            "distill folds a dump Definitions/Glossary heading into owners",
        )
    )
    rows.append(
        check(
            "sdd-eng-seat-name",
            "names a thing" in sdd_eng.lower() or "seat the" in sdd_eng.lower(),
            "sdd-eng seats a new name in the owner",
        )
    )
    rows.append(
        check(
            "002-no-glossary-twin",
            "glossary" in adr002.lower() and "third file" in adr002.lower(),
            "002 rejects a glossary as a third clarifying file",
        )
    )
    rows.append(
        check(
            "pack-no-mint-glossary",
            "do not mint" in owners.lower() and "glossary.md" in owners.lower(),
            "owners.md forbids minting a glossary file",
        )
    )
    reference = text(CURSOR / "skills" / "cursormax" / "reference.md")
    rows.append(
        check(
            "catalog-living-owner",
            "living owner" in reference.lower() and "blank-replace" in reference.lower(),
            "catalog states living owners merge; never blank-replace",
        )
    )
    rows.append(
        check(
            "cursormax-not-pstack",
            "not a pstack" in cm.lower() or "poteto-mode orchestra" in cm.lower(),
            "cursormax states it is not a pstack orchestra",
        )
    )
    rows.append(
        check(
            "cursormax-coexist",
            "coexist" in cm.lower() or "another workflow" in cm.lower() or "yield" in cm.lower(),
            "cursormax skill documents yielding to other packs",
        )
    )
    rows.append(
        check(
            "agents-maps-eval",
            "docs/eval.md" in agents,
            "AGENTS.md bullets docs/eval.md",
        )
    )
    rows.append(
        check(
            "eval-t1-nook",
            "t1-nook" in eval_md,
            "eval.md names t1-nook as qualifying dummy",
        )
    )
    rows.append(
        check(
            "t1-nook-red-start",
            'EMPTY = "Coming soon."' in t1_page and "Coming soon." in t1_design,
            "t1-nook starts red on Coming soon.",
        )
    )
    rows.append(
        check(
            "t1-task-no-keep-leak",
            "Keep every other line" not in t1_task and "keep every" not in t1_task.lower(),
            "EVAL-TASK does not leak the keep-the-file answer",
        )
    )

    for name in SKILLS:
        p = CURSOR / "skills" / name / "SKILL.md"
        rows.append(check(f"skill-{name}", p.is_file(), str(p)))
    for name in COMMANDS:
        p = CURSOR / "commands" / f"{name}.md"
        rows.append(check(f"cmd-{name}", p.is_file(), str(p)))
    for name in RULES:
        p = CURSOR / "rules" / name
        rows.append(check(f"rule-{name}", p.is_file(), str(p)))

    plugin = json.loads(text(PLUGIN) or "{}")
    cmd_list = plugin.get("commands") or []
    rule_list = plugin.get("rules") or []
    for name in COMMANDS:
        needle = f"./.cursor/commands/{name}.md"
        rows.append(
            check(f"plugin-cmd-{name}", needle in cmd_list, needle)
        )
    for name in RULES:
        needle = f"./.cursor/rules/{name}"
        rows.append(check(f"plugin-rule-{name}", needle in rule_list, needle))

    # Persona / description smoke: model-invoked skills have a use trigger.
    for name in ("sdd", "sdd-eng", "after-compact", "verify", "grill"):
        body = text(CURSOR / "skills" / name / "SKILL.md")
        rows.append(
            check(
                f"desc-{name}",
                body.startswith("---")
                and ("Use when" in body or "use when" in body.lower()),
                "frontmatter description present",
            )
        )

    deepen = text(CURSOR / "skills" / "deepen" / "SKILL.md")
    rows.append(
        check(
            "deepen-user-only",
            "disable-model-invocation: true" in deepen,
            "deepen stays user-invoked",
        )
    )

    cache = Path.home() / ".cursor" / "plugins" / "cache" / "troy-ll-cursor-maxxing"
    stale = False
    detail = "no cache"
    if cache.is_dir():
        caches = sorted(cache.glob("cursormax/*/"), key=lambda p: p.stat().st_mtime, reverse=True)
        if caches:
            c_bias = text(caches[0] / ".cursor" / "rules" / "cursormax-bias.mdc")
            stale = "Docs → sdd" in c_bias or "File on disk" not in c_bias
            detail = str(caches[0])
    if strict_install:
        rows.append(
            check(
                "install-matches-repo",
                not stale,
                f"plugin cache must match repo overlays ({detail})",
            )
        )
    else:
        rows.append(
            check(
                "install-lag-noted",
                True,
                f"stale={stale} path={detail} (warn only; re-import to clear)",
            )
        )

    # README and reference agree on after-compact default
    readme = text(ROOT / "README.md")
    rows.append(
        check(
            "readme-after-compact",
            "Opt out with `/keep off`" in readme or "keep off" in readme.lower(),
            "README documents keep off as opt-out",
        )
    )
    rows.append(
        check(
            "ref-after-compact",
            "keep off" in ref.lower() or "Opt out" in ref,
            "reference.md documents after-compact default",
        )
    )
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--strict-install",
        action="store_true",
        help="Fail when the installed plugin cache still teaches Docs → sdd",
    )
    args = ap.parse_args()
    rows = run_checks(strict_install=args.strict_install)
    failed = [r for r in rows if not r["ok"]]
    print(json.dumps({"failed": failed, "n": len(rows), "pass": len(rows) - len(failed)}, indent=2))
    return 1 if failed else 0


class TestT1NookRed(unittest.TestCase):
    def test_starts_red(self) -> None:
        import importlib.util

        page_path = ROOT / "docs" / "evals" / "dummies" / "t1-nook" / "page.py"
        spec = importlib.util.spec_from_file_location("t1_page", page_path)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(mod.EMPTY, "Coming soon.")


class TestNameSeating(unittest.TestCase):
    """Fail cases: minting a glossary, asking forever, seating in the wrong owner."""

    def _cursor_text(self) -> str:
        parts = []
        for p in (ROOT / ".cursor").rglob("*"):
            if p.suffix in {".md", ".mdc"} and p.is_file():
                parts.append(p.read_text(encoding="utf-8"))
        return "\n".join(parts)

    def test_occasion_table_has_no_glossary_owner(self) -> None:
        occasion = (ROOT / ".cursor" / "skills" / "sdd" / "occasion.md").read_text(
            encoding="utf-8"
        )
        in_table = False
        for line in occasion.splitlines():
            if line.startswith("| Job"):
                in_table = True
                continue
            if in_table and line.startswith("|") and "glossary" in line.lower():
                self.fail(f"occasion table minted a glossary owner: {line}")
            if in_table and not line.startswith("|"):
                in_table = False

    def test_no_skill_use_when_glossary(self) -> None:
        for p in (ROOT / ".cursor" / "skills").glob("*/SKILL.md"):
            body = p.read_text(encoding="utf-8")
            head = body.split("---", 2)
            desc = head[1] if len(head) > 2 else ""
            self.assertNotIn(
                "glossary",
                desc.lower(),
                f"{p.name} description must not pull on glossary",
            )

    def test_create_glossary_only_as_forbid(self) -> None:
        blob = self._cursor_text().lower()
        for needle in (
            "create `docs/glossary.md`",
            "create docs/glossary.md",
            "write docs/glossary.md",
            "mint docs/glossary.md",
        ):
            if needle in blob:
                self.assertIn(
                    "do not mint",
                    blob,
                    f"pack mentions {needle} without a do-not-mint rule",
                )


    def test_persona_fail_matrix(self) -> None:
        owners = (ROOT / ".cursor" / "skills" / "sdd" / "owners.md").read_text(
            encoding="utf-8"
        ).lower()
        occasion = (ROOT / ".cursor" / "skills" / "sdd" / "occasion.md").read_text(
            encoding="utf-8"
        ).lower()
        distill = (ROOT / ".cursor" / "skills" / "sdd" / "distill.md").read_text(
            encoding="utf-8"
        ).lower()
        sdd_eng = (ROOT / ".cursor" / "skills" / "sdd-eng" / "SKILL.md").read_text(
            encoding="utf-8"
        ).lower()
        adr002 = (ROOT / "docs" / "decisions" / "002-first-shot-efficiency.md").read_text(
            encoding="utf-8"
        ).lower()
        # A: "we need a glossary" → not an occasion row
        self.assertNotIn("| `docs/glossary.md`", occasion)
        self.assertIn("a glossary is a twin", occasion)
        # B: user word for UI / topology → seat in that owner, ask once if both
        self.assertIn("names a thing", owners)
        self.assertIn("ask once", owners)
        # C: dump with Definitions heading → fold, don't mint
        self.assertIn("definitions", distill)
        self.assertIn("do not mint", distill)
        # D: feature rename during implement → sdd-eng seats synonym
        self.assertIn("names a thing", sdd_eng)
        # E: glossary as third clarifying file → 002
        self.assertIn("glossary.md", adr002)
        self.assertIn("third file", adr002)
        owners = (ROOT / ".cursor" / "skills" / "sdd" / "owners.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("even if they asked for a glossary", owners.lower())
        sdd = (ROOT / ".cursor" / "skills" / "sdd" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("glossary / names dump is not a missing owner", sdd.lower())
        mapping = (ROOT / ".cursor" / "skills" / "sdd" / "map.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("do not map a glossary", mapping.lower())


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "unittest":
        sys.argv = [sys.argv[0]]
        raise SystemExit(unittest.main())
    raise SystemExit(main())
