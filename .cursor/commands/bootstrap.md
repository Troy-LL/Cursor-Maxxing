# Bootstrap project structure

Scaffold a **new or empty repo** for AI-assisted work. Create folders and **empty** doc shells only — **no** rule bodies, **no** cursor.directory installs, **no** skills content.

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
    .gitkeep
  docs/
    README.md            # points to repo docs/ and native /rules, /commands
```

## File content rules

| File | Content |
|------|---------|
| `docs/SPEC.md` etc. | **Empty** (0 bytes) or single newline — no boilerplate paragraphs |
| `docs/README.md` | Short index table only: file → purpose (one line each) |
| `.agents/README.md` | State: human + agent shared context; link to `docs/` |
| `.cursor/**/.gitkeep` | Empty file |
| `.cursor/docs/README.md` | 5–10 lines: `.cursor/commands`, `rules`, `skills`; use Cursor `/rules` and `/commands`; project truth lives in `docs/` |

**Do not** add `.mdc` rules, `SKILL.md`, or custom slash commands unless I explicitly ask in this message.

## After scaffold

Output:

1. Tree created (paths)
2. Skipped (already existed)
3. Suggested next steps:
   - Fill `docs/SPEC.md` first
   - `@SPEC.md` / `@ARCHITECTURE.md` when prompting
   - `@clean-coder` or project rules when ready (not part of bootstrap)
   - `/find-skills` or `/get-cursor-rules` only if I ask

## Principles

- Structure only — no policy, no slop, no generated specs
- Repo docs (`docs/`) = product truth; `.cursor/` = tooling slots only
