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

Do not duplicate these with custom commands.

---

## Custom commands (this repo)

| Command | Purpose |
|---------|---------|
| `/write-rule` | [cursor.directory](https://cursor.directory/) search + `npx cursor-directory rules add` + custom author |
| `/find-skills` | Profile repo, search [skills.sh](https://skills.sh/), recommend installs |
| `/slop-review` | Uncommitted vs `main` — slop audit, commit or sub-refactor |
| `/toolkit` | Inventory `.cursor/` in this repo |
| `/bootstrap` | Empty starter tree: `docs/`, `.agents/`, `.cursor/{commands,rules,skills}` — no rule content |
| `/pr-review` | Branch vs base — reviewer narrative (risks, test plan) |

Global copies: `~/.cursor/commands/` for `write-rule`, `find-skills`, `slop-review`, `bootstrap`, `pr-review` (no `/toolkit` globally).

---

## Rules (.mdc)

```yaml
---
description: Shown in rule picker
globs: **/*.ts
alwaysApply: false
---
```

**Directory first:**

```bash
npx cursor-directory rules add <slug-or-url>
```

Then tune `globs` / `alwaysApply`. Guide: [cursor-directory.md](cursor-directory.md). Skill: **write-cursor-rules**. Quick local edit: Cursor **`/rules`**.

### Meta rules

| Rule | When |
|------|------|
| `rule-author.mdc` | Editing `.cursor/rules/**/*.mdc` |
| `command-author.mdc` | Editing `.cursor/commands/**/*.md` |

### Opt-in: clean-coder

Activate with **`@clean-coder`** or "use clean-coder" — not automatic.  
`.cursor/rules/clean-coder/clean-coder.mdc` — 200 LOC cap, clean organization.

---

## Skills

| Skill | When |
|-------|------|
| `write-cursor-rules` | Rules + cursor.directory workflow |
| `write-cursor-commands` | Reference when using native **`/commands`** to add commands |

---

## Typical workflows

### Add a rule

1. **`/write-rule`** or "Using write-cursor-rules, add a rule for …"
2. Or **`/rules`** for a quick local rule only
3. Prefer `npx cursor-directory rules add` over writing from scratch

### Add a slash command

1. Cursor **`/commands`** (built-in)
2. **command-author** rule applies when editing `.cursor/commands/*.md`

### Audit rules

Ask in chat: "Audit `.cursor/rules` using write-cursor-rules" — or use **`/rules`** to review in UI.

### Clean code mode

**`@clean-coder`** on the files you're working on.

### Bootstrap a new repo

1. **`/bootstrap`** in the new project root
2. Fill `docs/SPEC.md`, then `ARCHITECTURE.md` / `DESIGN.md`
3. Prompt with `@SPEC.md`, `@ARCHITECTURE.md`
4. Add rules/skills later via **`/write-rule`**, **`/find-skills`**, or Cursor **`/rules`**

### Ship toolkit

Commit `.cursor/`; copy `~/.cursor/skills/` and `~/.cursor/commands/` for global tools.

---

## Rule vs command vs skill

| Need | Use |
|------|-----|
| Passive agent behavior | **Rule** (`/rules` or directory install) |
| One-shot workflow Cursor lacks | **Custom command** |
| Long playbook | **Skill** |
| Reference | **docs/** (this file) |

---

## Troubleshooting

**Custom command missing from `/` menu** — `.md` in `.cursor/commands/` or `~/.cursor/commands/`; reload window.

**Rule not applying** — check `alwaysApply` and `globs`.

**cursor.directory 429** — use `npx cursor-directory rules add`, not repeated raw API calls.
