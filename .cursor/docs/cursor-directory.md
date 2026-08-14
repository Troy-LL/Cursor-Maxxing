# Cursor Directory — rule source

Use [cursor.directory](https://cursor.directory/) first. Write a custom `.mdc` only when nothing fits. Local edits: Cursor **`/rules`**.

## Install

```bash
npx cursor-directory rules add <slug>
npx cursor-directory rules add https://cursor.directory/<slug>
```

CLI: [cursor-directory-cli](https://github.com/ericzakariasson/cursor-directory-cli). Direct API calls may **429**.

## After install

1. Open the new `.mdc`
2. Set `globs` and `alwaysApply`
3. Remove generic noise; one concern per file
4. Opt-in packs stay in subfolders (e.g. `rules/lean-coder/`)

## vs skills.sh

| Source | Package | Use for |
|--------|---------|---------|
| [cursor.directory](https://cursor.directory/) | `npx cursor-directory` | `.mdc` **rules** |
| [skills.sh](https://skills.sh/) | `npx skills` | Agent **skills** |
