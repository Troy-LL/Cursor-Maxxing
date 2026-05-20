---
name: get-cursor-rules
description: >-
  Gets rules from cursor.directory first, then installs or authors .mdc in
  .cursor/rules/. Use for get-cursor-rules, rules, mdc, or cursor.directory install.
---

# Get Cursor Rules

**Directory first:** [cursor.directory](https://cursor.directory/) → `npx cursor-directory rules add <slug-or-url>` before custom authoring. See `.cursor/docs/cursor-directory.md`.

## Phase 0 — Cursor Directory (required before authoring)

1. List existing `.cursor/rules/**/*.mdc` — do not duplicate topics
2. Search [cursor.directory](https://cursor.directory/):
   - Browse rules by stack/topic
   - Web search: `site:cursor.directory <framework> <topic>`
   - User-provided slug or URL
3. Present top matches with install command; **stop for approval** before install
4. After install: tune `description`, `globs`, `alwaysApply`; trim generic slop

**Author custom `.mdc` only when** no directory rule fits.

## Before writing (custom only)

Gather: purpose, scope (`alwaysApply` vs `globs`), one concern per file.

## Output location

`.cursor/rules/<kebab-case>.mdc`

## Content style

- Under ~50 lines when possible; cap 500
- Imperative bullets; ❌/✅ examples where useful
- Project-specific only

Templates: [templates.md](templates.md). Examples: [examples.md](examples.md).

## Validation

- [ ] Valid frontmatter
- [ ] Single concern
- [ ] No secrets in examples

Produce `.mdc` files directly when the user wants a rule.
