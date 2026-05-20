# Cursor Maxxing — User Manual

Your personal toolkit for rules, skills, slash commands, and docs. Read this when onboarding or when you forget where something lives.

---

## Folder map

```
.cursor/
├── commands/          # Slash commands — type / in chat
├── docs/              # Manuals and guides (this file)
├── rules/             # Project rules (.mdc)
└── skills/            # Agent skills (SKILL.md folders)

~/.cursor/
├── commands/          # Global slash commands (all projects)
└── skills/            # Global skills (all projects)
```

| Artifact | File pattern | Trigger |
|----------|--------------|---------|
| **Rule** | `.cursor/rules/*.mdc` | Auto (by `alwaysApply` / `globs`) |
| **Skill** | `.cursor/skills/*/SKILL.md` | Agent picks by description, or you name it |
| **Command** | `.cursor/commands/*.md` | You type `/` and pick one |
| **Manual** | `.cursor/docs/*.md` | You or agent reads when needed |

---

## Slash commands

### How they work

1. Add a `.md` file under `.cursor/commands/` (project) or `~/.cursor/commands/` (global).
2. Filename = command name: `write-rule.md` → `/write-rule`
3. In Cursor chat or Agent, type **`/`** and select the command.
4. The file contents are injected as your prompt for that turn.

Commands are **explicit** (you run them). Rules are **passive** (Cursor applies them). Skills are **playbooks** the agent can load for multi-step work.

### Command file format

Plain Markdown — no YAML required.

```markdown
# Short title (shown in the / menu)

Instructions for the agent. Be direct and imperative.

## Steps
1. First action
2. Second action

## Output
What you expect back (files created, summary, etc.)
```

**Naming:** lowercase, hyphens, descriptive: `code-review.md`, `write-rule.md`. Avoid `README.md` in `commands/` (it would become `/readme`).

### Project commands (this repo)

| Command | Purpose |
|---------|---------|
| `/write-rule` | Draft or edit a `.mdc` rule |
| `/write-command` | Create a new slash command |
| `/review-rules` | Audit rules in the repo |
| `/manual` | Open this manual and answer setup questions |
| `/toolkit` | List what is installed under `.cursor/` |
| `/slop-review` | Audit uncommitted changes vs main for AI slop; commit or sub-refactor |
| `/find-skills` | Profile this repo, search [skills.sh](https://skills.sh/), recommend tailored installs |
| `/clean-coder` | Opt-in clean code + 200 LOC component cap |

### Global commands

Same names can live in `~/.cursor/commands/` so they work in **every** project. Project commands only apply when that folder is open.

---

## Rules (.mdc)

Rules live in `.cursor/rules/`. Each file has YAML frontmatter:

```yaml
---
description: Shown in rule picker
globs: **/*.ts          # optional — file patterns
alwaysApply: false      # true = every chat
---
```

- **alwaysApply: true** — repo-wide standards
- **globs** — only when matching files are relevant

Use the **`write-cursor-rules`** skill or `/write-rule` to author rules. See `.cursor/skills/write-cursor-rules/` for templates and examples.

### Meta rules (auto when editing toolkit files)

| Rule | Applies when |
|------|----------------|
| `rule-author.mdc` | Editing `.cursor/rules/**/*.mdc` |
| `command-author.mdc` | Editing `.cursor/commands/**/*.md` |

### Opt-in rules (`rules/<name>/`)

Rules in subfolders are **off by default**. Invoke explicitly:

| Rule | How to activate |
|------|-----------------|
| **clean-coder** | `@clean-coder`, say "use clean-coder", or `/clean-coder` |

Standards: 200 LOC per component/module file, clean organization, minimal abstraction. See `.cursor/rules/clean-coder/clean-coder.mdc`.

---

## Skills

Skills are directories with `SKILL.md`:

```
.cursor/skills/my-skill/
├── SKILL.md
├── templates.md   # optional
└── examples.md    # optional
```

Frontmatter:

```yaml
---
name: my-skill
description: What it does. Use when the user mentions X, Y, or Z.
---
```

| Skill | When to use |
|-------|-------------|
| `write-cursor-rules` | Creating or refactoring `.mdc` rules |
| `write-cursor-commands` | Creating or refactoring slash commands (see `command-templates.md`) |

Personal copy: `~/.cursor/skills/<name>/` for use in all repos.

---

## Typical workflows

### Add a new rule

1. `/write-rule` or ask: "Using write-cursor-rules, add a rule for …"
2. Agent writes `.cursor/rules/<name>.mdc`
3. Confirm `description`, `alwaysApply`, and `globs`

### Add a new slash command

1. `/write-command` or ask: "Using write-cursor-commands, add /my-command"
2. Agent writes `.cursor/commands/my-command.md`
3. Type `/` in chat and test it

### Ship to another machine

- Commit `.cursor/` in the repo (commands, rules, skills, docs).
- Copy `~/.cursor/commands/` and `~/.cursor/skills/` for global personal setup.

---

## Rule vs command vs skill

| Need | Use |
|------|-----|
| Always-on or file-scoped agent behavior | **Rule** |
| One-shot workflow you run with `/` | **Command** |
| Long playbook, templates, checklists | **Skill** |
| Human-readable reference | **docs/** (this manual) |

---

## Troubleshooting

**Command does not appear in `/` menu**
- File must be `.md` directly in `.cursor/commands/` or `~/.cursor/commands/` (not nested subfolders unless your Cursor version supports it).
- Restart chat or reload window after adding files.

**Rule not applying**
- Check `alwaysApply` and `globs` in frontmatter.
- Split oversized rules; one concern per file.

**Skill not used**
- Mention the skill by name or describe the task using words from its `description`.

---

## Extending this toolkit

1. Add commands in `.cursor/commands/`.
2. Add rules in `.cursor/rules/`.
3. Add skills in `.cursor/skills/<name>/SKILL.md`.
4. Update this manual when you add something worth documenting.

Last updated: Cursor Maxxing scaffold.
