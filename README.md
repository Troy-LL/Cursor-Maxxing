# Cursor Maxxing

Toolkit for getting more out of Cursor — **commands**, **rules**, **skills**, and a **user manual**.

## Folder layout

```
.cursor/
├── commands/     # Slash commands — type / in chat
├── docs/         # USER-MANUAL.md and guides
├── rules/        # .mdc project rules
└── skills/       # Agent skill playbooks
```

Global (all projects): `~/.cursor/commands/`, `~/.cursor/skills/`

## User manual

**[.cursor/docs/USER-MANUAL.md](.cursor/docs/USER-MANUAL.md)** — start here for onboarding, folder map, and troubleshooting.

Quick help in chat: type **`/manual`**.

## Slash commands

| Command | What it does |
|---------|----------------|
| `/write-rule` | Create or edit a `.mdc` rule |
| `/write-command` | Create a new slash command |
| `/review-rules` | Audit rules in the repo |
| `/manual` | Answer questions from the user manual |
| `/toolkit` | List commands, rules, skills, docs |
| `/slop-review` | Audit uncommitted vs `main` for slop; commit or fix |
| `/find-skills` | Context-aware skill discovery via `npx skills find` |
| `/clean-coder` | Opt-in: 200 LOC cap, clean organized code |

### Opt-in rules

`.cursor/rules/clean-coder/` — not auto-applied. Use `@clean-coder` or `/clean-coder`.

Add more: drop a `.md` file in `.cursor/commands/` (name = `/command`).

## Skills

| Skill | Purpose |
|-------|---------|
| `write-cursor-rules` | Author `.mdc` rules |
| `write-cursor-commands` | Author slash commands |

Available in this repo and under `~/.cursor/skills/` for global use.

## Rules

- **Meta:** `.cursor/rules/rule-author.mdc` — guidance when editing rules
- Create via `/write-rule` or the `write-cursor-rules` skill

## Rule vs command vs skill

| | Rules | Commands | Skills |
|--|-------|----------|--------|
| **Trigger** | Automatic (scope) | You type `/` | Agent or you name it |
| **Format** | `.mdc` + YAML | `.md` prompt | `SKILL.md` + optional refs |
| **Best for** | Ongoing standards | One-shot workflows | Long playbooks + templates |
