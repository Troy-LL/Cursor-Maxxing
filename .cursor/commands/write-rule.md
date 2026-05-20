# Write a Cursor rule (directory-first)

Use **write-cursor-rules** skill. For simple local create/edit, Cursor **`/rules`** also works — this command adds [cursor.directory](https://cursor.directory/) discovery and install.

## Phase A — Project context

Read manifests, README, `.cursor/rules/`, stack, and needed globs. List installed rules — skip duplicates.

## Phase B — Search cursor.directory

1. Browse [cursor.directory](https://cursor.directory/) by topic (e.g. [API](https://cursor.directory/rules/api), React, TypeScript)
2. Web search: `site:cursor.directory <stack> <topic>`
3. User slug/URL if provided

Collect **3–8 candidates** with link, slug, and one-line fit for this repo.

## Phase C — Recommend or install

| Situation | Action |
|-----------|--------|
| Directory match | `npx cursor-directory rules add <slug-or-url>` |
| Partial match | Install + tune `globs` / `alwaysApply` |
| No match | Custom `.mdc` per skill checklist |

Present install commands. **Wait for approval** before `npx cursor-directory rules add`.

After install: tune frontmatter, trim generic slop, update `USER-MANUAL.md` if needed.

## Phase D — Custom author (last resort)

Write `.cursor/rules/<kebab-case>.mdc` only when no directory rule fits.

## Output

- **Source:** cursor.directory (slug + link) OR custom path
- **Frontmatter:** description, alwaysApply, globs
- How to enable in Cursor

If I gave a directory URL/slug, prefer install + tune over writing new.
