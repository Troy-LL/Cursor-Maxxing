# Cursor Maxxing

Toolkit for Cursor — custom commands only where the IDE falls short.

## Start here

**[.cursor/docs/USER-MANUAL.md](.cursor/docs/USER-MANUAL.md)** — or `@USER-MANUAL.md`

**New repo:** **`/bootstrap`** → fill `docs/SPEC.md` → **`/get-cursor-rules`** / **`/find-skills`** when ready.

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
| `/bootstrap` | Empty `docs/`, `.agents/`, `.cursor/` scaffold |
| `/pr-review` | PR review vs default branch |
| `/toolkit` | Inventory this repo |

## Skill

**`get-cursor-rules`** — directory-first rules (`.cursor/skills/get-cursor-rules/`)

## Opt-in rules

**`@clean-coder`** — 200 LOC cap, clean code

## Install rules from directory

```bash
npx cursor-directory rules add <slug-or-url>
```

See [.cursor/docs/cursor-directory.md](.cursor/docs/cursor-directory.md).
