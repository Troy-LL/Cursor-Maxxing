# Cursor Maxxing — User Manual

Toolkit for rules, skills, and custom slash commands. Open this file or `@USER-MANUAL.md` in chat.

---

## Folder map

```
.cursor/
├── commands/          # Custom slash commands (only what Cursor doesn't ship)
├── docs/              # Manuals and guides (this file)
├── rules/             # Project rules (.mdc)
└── skills/            # Agent skills (SKILL.md folders)

~/.cursor/
├── commands/          # Global custom commands
└── skills/            # Global skills
```

| Artifact | Trigger |
|----------|---------|
| **Rule** | Auto (`alwaysApply` / `globs`) or `@rule-name` |
| **Skill** | Agent discovery or name it in chat |
| **Custom command** | Type `/` and pick (yours only) |

---

## Built into Cursor (use these first)

| Native | Use for |
|--------|---------|
| **`/rules`** | Create or edit project rules locally |
| **`/commands`** | Create or edit slash commands locally |
| **`/plan`** | Plan before coding |
| **`/ask`** | Read-only exploration |

---

## Custom commands

| Command | Purpose |
|---------|---------|
| `/get-cursor-rules` | [cursor.directory](https://cursor.directory/) search + install + custom author |
| `/find-skills` | Profile repo, search [skills.sh](https://skills.sh/) |
| `/slop-review` | Uncommitted vs `main` — slop audit |
| `/bootstrap` | Starter tree: `docs/`, `.agents/`, empty `.cursor/` slots |
| `/pr-review` | Branch vs base — reviewer narrative |
| `/toolkit` | Inventory `.cursor/` (this meta repo) |

Global: `~/.cursor/commands/` for all except `/toolkit`.

---

## Rules (.mdc)

```bash
npx cursor-directory rules add <slug-or-url>
```

Skill: **get-cursor-rules**. Command: **`/get-cursor-rules`**. Guide: [cursor-directory.md](cursor-directory.md). Local edit: **`/rules`**.

### Meta rules

| Rule | When |
|------|------|
| `rule-author.mdc` | Editing `.cursor/rules/**/*.mdc` |
| `command-author.mdc` | Editing `.cursor/commands/**/*.md` |

### Opt-in: clean-coder

**`@clean-coder`** — `.cursor/rules/clean-coder/clean-coder.mdc`

---

## Skills

| Skill | When |
|-------|------|
| `get-cursor-rules` | Fetch/install rules from cursor.directory; custom `.mdc` fallback |

---

## Workflows

### Get rules

1. **`/get-cursor-rules`** or "Using get-cursor-rules, …"
2. Or **`/rules`** for a quick local-only rule

### New repo

1. **`/bootstrap`** → fill `docs/SPEC.md`
2. **`/get-cursor-rules`** + **`/find-skills`** when ready

### Audit rules

Ask: "Audit `.cursor/rules` using get-cursor-rules" or use **`/rules`**.

---

## Troubleshooting

**Custom command missing** — reload window; check `.cursor/commands/` or `~/.cursor/commands/`.

**cursor.directory 429** — use `npx cursor-directory rules add`, not repeated API calls.
