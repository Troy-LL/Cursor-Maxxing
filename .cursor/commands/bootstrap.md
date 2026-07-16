# Bootstrap project structure

Scaffold a **new or empty repo** for AI-assisted work, then **optionally distill** a user-provided ideation spec into the right `docs/` files.

Create folders and doc shells first — **no** rule bodies, **no** cursor.directory installs, **no** skills content in those slots.

## Before creating

1. `git status` or list root — note what already exists
2. **Do not overwrite** non-empty files; skip and report conflicts
3. If `.cursor/`, `docs/`, or `.agents/` already exist, only add **missing** paths

## Create this tree

```
.agents/
  README.md              # explains agent context folder (short, 5 lines max)

docs/
  README.md              # index: what each doc is for
  DEVELOPMENT.md         # copy from bootstrap/DEVELOPMENT.md (this toolkit)
  SPEC.md                # empty
  DESIGN.md              # empty
  ARCHITECTURE.md        # empty
  API.md                 # empty
  TESTING.md             # empty
  DEPLOYMENT.md          # empty

.cursor/
  commands/
    .gitkeep
  rules/
    .gitkeep
  skills/
    document-distillator/
      SKILL.md           # Auditor: spec → docs/ (see skill body)
  docs/
    README.md            # points to repo docs/ and native /rules, /commands
```

## File content rules

| File | Content |
|------|---------|
| `docs/DEVELOPMENT.md` | **Copy** from this toolkit's `bootstrap/DEVELOPMENT.md` — skip only if path exists and is non-empty |
| `docs/SPEC.md` etc. | **Empty** (0 bytes) or single newline — no boilerplate paragraphs |
| `docs/README.md` | Short index table only: file → purpose (one line each) |
| `.agents/README.md` | State: human + agent shared context; link to `docs/` |
| `.cursor/**/.gitkeep` | Empty file |
| `.cursor/docs/README.md` | 5–10 lines: `.cursor/commands`, `rules`, `skills`; use Cursor `/rules` and `/commands`; project truth lives in `docs/` |

**Do not** add `.mdc` rules, other `SKILL.md` files, or custom slash commands unless I explicitly ask in this message.

**Include** `.cursor/skills/document-distillator/SKILL.md` — copy from this toolkit’s skill if bootstrapping elsewhere; skip only if that path already exists and is non-empty.

## Phase 2 — Document distillation (recommended)

After scaffold, run the **document-distillator** skill (Auditor).

1. Ask for the **source spec path** if I did not provide it (file can be **outside** this repo or anywhere on disk — not part of the bootstrap tree).
2. Read `.cursor/skills/document-distillator/SKILL.md` and follow it exactly.
3. Audit which `docs/*.md` shells are needed for my plan; **populate** those from the spec.
4. **Delete** unused empty scaffold docs and **delete the source spec** after approval (default **Y**), unless I chose **K** to keep the source.

Do not skip distillation silently — if I gave no spec path, prompt once: *"Path to your ideation spec? (or `skip` to leave empty shells)"*.

## After scaffold (+ distillation if run)

Output:

1. Tree created (paths)
2. Skipped (already existed)
3. Distillation summary (if run): populated docs, deleted shells, source spec fate
4. Suggested next steps:
   - `@docs/DEVELOPMENT.md` for workflow alignment; `@docs/SPEC.md` and other populated docs when prompting
   - `@lean-coder` or project rules when ready (not part of bootstrap)
   - `/find-skills` or `/get-cursor-rules` only if I ask
   - Before GitHub: **`/clean`** to remove local-only scaffold (keeps filled `docs/`)

## Principles

- Structure first — policy and prose come from **my** spec via distillation, not generated slop
- Repo docs (`docs/`) = product truth; `.cursor/` = tooling slots only
- Fewer, fuller docs beat a full set of empty shells
