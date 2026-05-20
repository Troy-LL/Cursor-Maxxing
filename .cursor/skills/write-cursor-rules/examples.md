# Rule writing examples

## Example 1: User request → file

**User:** "Add a rule so the agent always uses our logger and never console.log in TypeScript."

**Output:** `.cursor/rules/typescript-logging.mdc`

```markdown
---
description: Use project logger instead of console in TypeScript files
globs: **/*.{ts,tsx}
alwaysApply: false
---

# Logging

- Use `logger` from `@/lib/logger` — never `console.log`, `console.warn`, or `console.error` in application code.
- Include structured context objects: `logger.info('user created', { userId })`.
- Exception: scripts under `scripts/` may use console for CLI output.
```

---

## Example 2: Splitting a bloated rule

**Before:** `full-stack.mdc` (120 lines) covers React, Python, and SQL.

**After:**

| File | globs |
|------|-------|
| `react-ui.mdc` | `**/*.{tsx,jsx}` |
| `python-api.mdc` | `backend/**/*.py` |
| `sql-migrations.mdc` | `db/migrations/**/*.sql` |

Each file gets a focused `description` and under ~50 lines.

---

## Example 3: Bad vs good rule body

**Bad** (vague, wastes tokens):

```markdown
# Code quality

Write high-quality, maintainable code. Follow best practices. Think about edge cases.
```

**Good** (specific, verifiable):

```markdown
# API handlers

- Return `{ error: string, code: string }` for 4xx/5xx; never raw Error objects.
- Authenticate with `requireSession()` before any mutation.
- Paginate list endpoints with `cursor` + `limit` (max 100).
```

---

## Example 4: alwaysApply decision

| User intent | Config |
|-------------|--------|
| "Only when editing Go files" | `globs: **/*.go`, `alwaysApply: false` |
| "Every conversation in this repo" | `alwaysApply: true`, omit `globs` |
| "When working on docs" | `globs: **/*.md`, `alwaysApply: false` |
