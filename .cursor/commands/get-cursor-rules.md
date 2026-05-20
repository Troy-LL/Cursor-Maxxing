# Get Cursor rules (directory-first)

Use **get-cursor-rules** skill. For quick local edits, Cursor **`/rules`** works — this command fetches from [cursor.directory](https://cursor.directory/) first.

## Phase A — Project context

Read manifests, README, `.cursor/rules/`, stack, and needed globs. List installed rules — skip duplicates.

## Phase B — Search cursor.directory

1. Browse [cursor.directory](https://cursor.directory/) by topic
2. Web search: `site:cursor.directory <stack> <topic>`
3. User slug/URL if provided

Collect **3–8 candidates** with link, slug, and one-line fit.

## Phase C — Recommend or install

| Situation | Action |
|-----------|--------|
| Directory match | `npx cursor-directory rules add <slug-or-url>` |
| Partial match | Install + tune `globs` / `alwaysApply` |
| No match | Custom `.mdc` per **get-cursor-rules** skill |

**Wait for approval** before `npx cursor-directory rules add`.

## Phase D — Custom author (last resort)

Write `.cursor/rules/<kebab-case>.mdc` only when no directory rule fits.

## Output

- **Source:** cursor.directory (slug + link) OR custom path
- **Frontmatter:** description, alwaysApply, globs

If I gave a directory URL/slug, prefer install + tune over writing new.
