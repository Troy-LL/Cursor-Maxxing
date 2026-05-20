# Cursor Maxxing

Toolkit for Cursor — rules, skills, and **custom commands only where the IDE falls short**.

## Folder layout

```
.cursor/
├── commands/     # Custom / commands (not built into Cursor)
├── docs/         # USER-MANUAL.md, cursor-directory.md
├── rules/        # .mdc project rules
└── skills/       # Agent skill playbooks
```

## Start here

**[.cursor/docs/USER-MANUAL.md](.cursor/docs/USER-MANUAL.md)** — or `@USER-MANUAL.md` in chat.

## Use Cursor built-ins first

| Native | Instead of custom |
|--------|-------------------|
| **`/rules`** | Creating/editing rules locally |
| **`/commands`** | Creating/editing slash commands |

## Custom commands (kept)

| Command | Why kept |
|---------|----------|
| `/write-rule` | [cursor.directory](https://cursor.directory/) discovery + install — not in IDE |
| `/find-skills` | [skills.sh](https://skills.sh/) — separate ecosystem |
| `/slop-review` | Git slop audit vs `main` — not in IDE |
| `/toolkit` | Inventory this meta repo |

## Opt-in rules

**`@clean-coder`** — `.cursor/rules/clean-coder/` (200 LOC cap, clean code). No slash command; use `@` mention.

## Skills

- `write-cursor-rules` — directory-first rules
- `write-cursor-commands` — reference for native `/commands`

## Rules from directory

```bash
npx cursor-directory rules add <slug-or-url>
```

See [.cursor/docs/cursor-directory.md](.cursor/docs/cursor-directory.md).
