---
name: write-cursor-commands
description: >-
  Authors and edits Cursor slash commands (.md files in .cursor/commands/ or
  ~/.cursor/commands/). Use when the user wants a custom / command, slash command,
  or asks to create or update command prompts.
---

# Cursor Slash Command Writer

You author **slash commands** — plain Markdown files that appear when the user types `/` in chat.

## Locations

| Scope | Path |
|-------|------|
| Project | `.cursor/commands/<name>.md` |
| Global | `~/.cursor/commands/<name>.md` |

**Filename = command name:** `lint-fix.md` → `/lint-fix`

Do not put `README.md` in `commands/` (becomes `/readme`). Put guides in `.cursor/docs/`.

## Before Writing

| Question | Default |
|----------|---------|
| Command name? | kebab-case from user intent |
| Project or global? | project unless user wants all repos |
| One workflow per file? | yes — split if multiple unrelated flows |
| Update manual? | add row in `.cursor/docs/USER-MANUAL.md` if user-facing |

## Command File Template

```markdown
# Short title for the / menu

One paragraph: what this command does.

## Steps
1. First concrete action for the agent
2. Second action

## Output
What to return or which files to create.
```

No YAML frontmatter required. Optional second heading sections: Context, Constraints, Examples.

## Style

- **Imperative** steps — "Read X", "Write Y", not "You might want to…"
- **Scoped** — one job per command; link to a skill for heavy playbooks
- **Explicit output** — files, format, or "ask before deleting"
- **Reference skills** by name when the workflow is large: "Use **write-cursor-rules** skill"
- Under **~80 lines** per command; split if longer

## Pairing with skills and rules

| Pattern | When |
|---------|------|
| Command → skill | User runs `/write-rule`; body says "use write-cursor-rules skill" |
| Command only | Short one-off prompt, no extra files |
| Rule + command | Rule sets passive standards; command runs an audit or scaffold |

## Workflow

1. Infer name, scope, and steps from the user message
2. Write the `.md` file
3. Tell user: "Type `/name` in chat to run it"
4. Update `USER-MANUAL.md` command table if this is a permanent project command

## Validation

- [ ] File is `.md` in `commands/` (not nested unless user confirms support)
- [ ] Filename lowercase with hyphens
- [ ] `#` title present
- [ ] Clear steps and output section
- [ ] No secrets in the prompt text

## Examples

**`/pr-summary`** — summarize PR for review

```markdown
# PR summary

Summarize the current branch vs main for review.

## Steps
1. Run `git log main..HEAD --oneline` and `git diff main...HEAD --stat`
2. Group changes by area (features, fixes, chores)
3. List risks and test gaps

## Output
- ## Summary (3 bullets)
- ## Changes by area
- ## Test plan checklist
```

**`/write-command`** — meta; points at this skill (already in project commands).

## Command vs skill migration

Cursor can migrate commands to skills (`disable-model-invocation: true`). **Keep commands** when the user should explicitly type `/`. **Use skills** for long reference + templates. Do not migrate unless the user asks.

See [command-templates.md](command-templates.md) for more starters.
