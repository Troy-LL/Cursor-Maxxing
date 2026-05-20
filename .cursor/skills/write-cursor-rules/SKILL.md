---
name: write-cursor-rules
description: >-
  Finds rules on cursor.directory first, then authors or edits .mdc files in
  .cursor/rules/. Use when the user wants a rule, mdc file, write-rule, find-rules,
  or cursor.directory install.
---

# Cursor Rule Writer

You are a specialist for **Cursor project rules** — `.mdc` files in `.cursor/rules/`.

**Directory first:** Prefer installing from [cursor.directory](https://cursor.directory/) before writing new content. See `.cursor/docs/cursor-directory.md`.

## Phase 0 — Cursor Directory (required before authoring)

1. List existing `.cursor/rules/**/*.mdc` — do not duplicate topics
2. Search [cursor.directory](https://cursor.directory/):
   - Browse rules by stack/topic
   - Web search: `site:cursor.directory <framework> <topic>`
   - User-provided slug or `https://cursor.directory/<slug>` URL
3. Present top matches with install command:

   ```bash
   npx cursor-directory rules add <slug-or-url>
   ```

4. **Stop for user approval** before install unless they already said "install from directory"
5. After install: tune `description`, `globs`, `alwaysApply`; trim generic slop

**Author custom `.mdc` only when** no directory rule fits or the user explicitly wants project-specific content.

## Before Writing (custom rules only)

Gather or infer:

| Question | Why |
|----------|-----|
| **Purpose** | What behavior should the agent adopt? |
| **Scope** | Always-on vs file-specific? |
| **Globs** | If file-specific: concrete patterns (`**/*.ts`, `backend/**/*.py`) |
| **One concern?** | Split if the topic spans unrelated stacks |

If scope or globs are unclear, use **AskQuestion** (or ask in chat):

- Always apply vs only for certain files?
- Which glob patterns?

Do not ask redundant questions when the conversation already answers them.

## Output Location

```
.cursor/rules/
  <kebab-case-name>.mdc
```

Filename: lowercase, hyphens, descriptive (e.g. `typescript-error-handling.mdc`). No spaces.

## Rule File Template

Every rule **must** use this structure:

```markdown
---
description: One line shown in the rule picker — what it does
globs: **/*.ts
alwaysApply: false
---

# Rule Title

Actionable guidance here.
```

### Frontmatter rules

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Yes | Short, specific; third-person OK |
| `alwaysApply` | Yes | `true` = every chat; `false` = scoped |
| `globs` | If scoped | Omit only when `alwaysApply: true` |

**Always apply** (project-wide standards):

```yaml
---
description: Core standards for this repo
alwaysApply: true
---
```

**File-scoped** (default):

```yaml
---
description: React component conventions
globs: **/*.{tsx,jsx}
alwaysApply: false
---
```

## Content Style

- **Under ~50 lines** per rule when possible; hard cap **500 lines**
- **One concern per file**
- **Imperative, actionable** bullets
- **❌ BAD / ✅ GOOD** snippets where patterns matter
- Project-specific facts only — not generic "write clean code"

## Workflow

1. Draft frontmatter + sections
2. Run validation checklist (below)
3. Write `.cursor/rules/<name>.mdc`
4. Preserve user **verbatim** wording when provided

Templates: [templates.md](templates.md). Examples: [examples.md](examples.md).

## Validation Checklist

- [ ] `.cursor/rules/*.mdc`
- [ ] Valid frontmatter (`description`, `alwaysApply`, `globs` if scoped)
- [ ] Single concern; under 500 lines
- [ ] No secrets in examples

## Rule vs skill

| Artifact | Path | When |
|----------|------|------|
| Rule | `.cursor/rules/*.mdc` | Persistent agent context |
| Skill | `.cursor/skills/*/SKILL.md` | Multi-step workflows (this file) |

Produce `.mdc` files directly when the user wants a rule — do not only explain format.
