# Cursor Directory — rule source

Use [cursor.directory](https://cursor.directory/) as the **first** place to get rules. Write custom `.mdc` files only when nothing fits.

## Install a rule

```bash
npx cursor-directory rules add <slug>
npx cursor-directory rules add https://cursor.directory/<slug>
```

- Fetches from `https://cursor.directory/api/<slug>`
- Saves to `.cursor/rules/<name>.mdc`
- CLI: [cursor-directory-cli](https://github.com/ericzakariasson/cursor-directory-cli)

**Note:** Use the CLI for installs. Direct `cursor.directory/api/...` calls may return **429** if rate-limited.

## Discover rules

| Method | Example |
|--------|---------|
| Browse | [cursor.directory](https://cursor.directory/) → Rules |
| By topic | [Rules → API](https://cursor.directory/rules/api), React, TypeScript, etc. |
| Web search | `site:cursor.directory nextjs` |
| Chat | `/find-rules` or `/write-rule` |

## After install

1. Open the new `.mdc`
2. Set `globs` and `alwaysApply` for your repo
3. Remove generic noise; keep one concern per file
4. Opt-in packs stay in subfolders (e.g. `rules/clean-coder/`)

## Command in this toolkit

| Command | Role |
|---------|------|
| `/write-rule` | Search directory + install + custom author |

For quick local rule edits without directory search, use Cursor **`/rules`**.

## vs skills.sh

| Source | Package | Use for |
|--------|---------|---------|
| [cursor.directory](https://cursor.directory/) | `npx cursor-directory` | `.mdc` **rules** |
| [skills.sh](https://skills.sh/) | `npx skills` | Agent **skills** |
