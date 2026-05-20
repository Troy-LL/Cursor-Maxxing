# Slash command templates

---

## Code review

```markdown
# Code review

Review the selected or recently changed files.

## Steps
1. Focus on correctness, security, and regressions
2. Note style only when it violates project rules in `.cursor/rules/`
3. Cite file:line for issues

## Output
- Critical (must fix)
- Suggestions (should consider)
- Optional nitpicks
```

---

## Explain selection

```markdown
# Explain code

Explain the highlighted or open file section for a mid-level developer.

## Steps
1. What it does (one paragraph)
2. How it fits the surrounding module
3. Non-obvious behavior or edge cases

## Output
No drive-by refactor offers unless I ask.
```

---

## Scaffold rule

```markdown
# Quick rule

Directory-first: search cursor.directory, then `npx cursor-directory rules add <slug>` or custom .mdc via **write-cursor-rules**.

## Output
Source (directory slug or custom path), frontmatter, next step.
```

---

## Git commit message

```markdown
# Commit message

Propose a commit message for staged changes.

## Steps
1. `git diff --staged` (and status if needed)
2. Follow repo commit style from recent `git log -5`

## Output
Subject line + body (ready to paste). Do not run commit unless I say.
```

---

## Docs from manual

```markdown
# Manual help

Read `.cursor/docs/USER-MANUAL.md` and answer my question about this toolkit.
```
