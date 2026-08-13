# Bootstrap project structure

Scaffold a **new or empty repo** for AI-assisted work, then **optionally distill** a user-provided ideation spec onto the allowlist. Create slots first. No rule bodies, no cursor.directory installs, no extra skills unless asked.

Do **not** create `docs/SPEC.md`, `docs/API.md`, `docs/TESTING.md`, `docs/DEPLOYMENT.md`, `docs/DEVELOPMENT.md`, or `docs/README.md`. Do **not** pre-create `docs/` shells. Distillation decides which allowlisted docs exist.

## Before creating

1. `git status` or list root. Note what already exists.
2. **Do not overwrite** non-empty files; skip and report conflicts.
3. If `.cursor/`, `docs/`, `.agents/`, or `AGENTS.md` already exist, only add **missing** paths.

## Create this tree

```
AGENTS.md                # the only map (stub from document-distillator)

.agents/
  README.md              # short; points at AGENTS.md

.cursor/
  commands/
    .gitkeep
  rules/
    .gitkeep
  skills/
    document-distillator/
      SKILL.md
  docs/
    README.md            # tooling slots; points at AGENTS.md
```

Create **nothing** under `docs/` until distillation. Do not copy a per-project `DEVELOPMENT.md`.

## File content rules

| File | Content |
|------|---------|
| `AGENTS.md` | If missing or empty: write the **Map stub** from `.cursor/skills/document-distillator/SKILL.md`. Thin. Load cap + pointers. No architecture pasted in. |
| `.agents/README.md` | Human + agent shared notes. Map is `AGENTS.md`. Product is `README.md`. `/clean` removes this folder. 5 lines max. |
| `.cursor/**/.gitkeep` | Empty file |
| `.cursor/docs/README.md` | 5–10 lines: `commands`, `rules`, `skills`; use Cursor `/rules` and `/commands`; map is `AGENTS.md`; do not add `docs/README.md` |

**Do not** add `.mdc` rules, other `SKILL.md` files, or custom slash commands unless I explicitly ask in this message.

**Include** `.cursor/skills/document-distillator/SKILL.md`. Copy from this toolkit’s skill if bootstrapping elsewhere; skip only if that path already exists and is non-empty.

## Phase 2 — Document distillation (recommended)

After scaffold, run the **document-distillator** skill (Auditor).

1. Ask for the **source spec path** if I did not provide it (file can be **outside** this repo or anywhere on disk).
2. Read `.cursor/skills/document-distillator/SKILL.md` and follow it exactly.
3. Map spec content onto the **allowlist** only. Create a docs file only when that job exists.
4. **Delete** unused empty shells (including leftover SPEC/API/TESTING/DEPLOYMENT/DEVELOPMENT/`docs/README.md`) and **delete the source spec** after approval (default **Y**), unless I chose **K** to keep the source.

Do not skip distillation silently. If I gave no spec path, prompt once: *"Path to your ideation spec? (or `skip` to leave AGENTS.md only)"*.

## After scaffold (+ distillation if run)

Output:

1. Tree created (paths)
2. Skipped (already existed)
3. Distillation summary (if run): populated files, deleted shells, source spec fate
4. Suggested next steps:
   - `@AGENTS.md` then allowlisted files the job needs (`README.md`, `docs/architecture.md`, …)
   - `@lean-coder` or project rules when ready (not part of bootstrap)
   - `/find-skills` or `/get-cursor-rules` only if I ask
   - Before GitHub: **`/clean`** (keeps `AGENTS.md` and filled allowlisted docs)

## Principles

- Structure first. Policy and prose come from **my** spec via distillation, not generated slop.
- `AGENTS.md` is the only map. `README.md` is the product. `.cursor/` is tooling slots.
- No second map (`docs/README.md`). Fewer, fuller docs beat empty shells.
