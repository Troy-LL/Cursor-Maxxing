# Review Cursor rules

Audit every `.mdc` file under `.cursor/rules/` (and nested rules if any).

## For each rule, report

- **File** and **description** (from frontmatter)
- **Scope:** `alwaysApply` and `globs`
- **Size:** line count (flag if over ~50 lines)
- **Issues:** vague bullets, mixed concerns, missing examples, duplicate user-rule content

## Output format

1. Summary table (file | scope | lines | status OK / split / tighten)
2. Top 3 recommended fixes (concrete — offer to apply if I say yes)
3. Optional: run **write-cursor-rules** to split or rewrite the worst offender

Do not delete or edit files unless I ask you to apply fixes.
