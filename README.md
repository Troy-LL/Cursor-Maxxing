# Cursor Maxxing

Toolkit for Cursor — custom commands only where the IDE falls short.

## Start here

**[.cursor/docs/USER-MANUAL.md](.cursor/docs/USER-MANUAL.md)** — or `@USER-MANUAL.md`

**New repo:** **`/bootstrap`** (distill your spec into `docs/`) → work locally → **`/clean`** before GitHub → **`/get-cursor-rules`** / **`/find-skills`** when ready.

## Built into Cursor

| Native | Use for |
|--------|---------|
| **`/rules`** | Local rule create/edit |
| **`/commands`** | Local slash command create/edit |

## Custom commands

| Command | Purpose |
|---------|---------|
| `/get-cursor-rules` | [cursor.directory](https://cursor.directory/) + install |
| `/find-skills` | [skills.sh](https://skills.sh/) |
| `/slop-review` | Pre-commit slop audit |
| `/bootstrap` | `docs/` scaffold + spec distillation via **document-distillator** |
| `/clean` | Remove AI clutter before publishing to GitHub |
| `/pr-review` | PR review vs default branch |
| `/toolkit` | Inventory this repo |

## Skills

| Skill | Role |
|-------|------|
| **`get-cursor-rules`** | Directory-first rules (`.cursor/skills/get-cursor-rules/`) |
| **`document-distillator`** | Auditor: external spec → minimal `docs/`, prune bloat (`.cursor/skills/document-distillator/`) |

## Opt-in rules

**`@lean-coder`** — 200 LOC cap, lean organized code

## Install rules from directory

```bash
npx cursor-directory rules add <slug-or-url>
```

See [.cursor/docs/cursor-directory.md](.cursor/docs/cursor-directory.md).
