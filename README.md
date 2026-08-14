# Cursor Maxxing

Custom slash commands only where Cursor does not already ship the job.

Product docs are **`/sdd`** (Troy's SDD). Rules: native **`/rules`** or `npx cursor-directory`. Skills: [skills.sh](https://skills.sh/).

## Commands

| Command | Purpose |
|---------|---------|
| `/slop-review` | Uncommitted vs `main` — slop audit before commit |
| `/pr-review` | Branch vs default — reviewer narrative |
| `/toolkit` | Inventory this repo's `.cursor/` |

Install the first two globally: copy into `~/.cursor/commands/`.

## Opt-in

**`@lean-coder`** — 200 LOC cap, lean organized code.

## Directory

```bash
npx cursor-directory rules add <slug-or-url>
```

[.cursor/docs/cursor-directory.md](.cursor/docs/cursor-directory.md) · [USER-MANUAL](.cursor/docs/USER-MANUAL.md)
