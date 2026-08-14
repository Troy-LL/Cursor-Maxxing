# Cursor Maxxing — User Manual

Custom commands only where the IDE falls short. `@USER-MANUAL.md` in chat.

## Folder map

```
.cursor/
├── commands/     # slash commands
├── docs/         # this file
└── rules/        # .mdc (opt-in lean-coder; authoring globs)

~/.cursor/commands/   # global copies of /slop-review and /pr-review
```

Native first: **`/rules`**, **`/commands`**, **`/plan`**, **`/ask`**.

Product files: **`/sdd`**. Rules from the web: `npx cursor-directory rules add <slug>`. Skills: [skills.sh](https://skills.sh/) / `npx skills`.

## Custom commands

| Command | Purpose |
|---------|---------|
| `/slop-review` | Uncommitted vs `main` — slop audit |
| `/pr-review` | Branch vs base — reviewer narrative |
| `/toolkit` | Inventory `.cursor/` (this repo) |

`/toolkit` stays project-local. The other two belong in `~/.cursor/commands/`.

## Rules

| Rule | When |
|------|------|
| `rule-author.mdc` | Editing `.cursor/rules/**/*.mdc` |
| `command-author.mdc` | Editing `.cursor/commands/**/*.md` |
| `@lean-coder` | Opt-in 200 LOC cap |

Guide: [cursor-directory.md](cursor-directory.md).

## Troubleshooting

**Command missing** — reload window; check `.cursor/commands/` or `~/.cursor/commands/`.

**cursor.directory 429** — use `npx cursor-directory rules add`, not repeated API calls.
