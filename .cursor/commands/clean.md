# Clean repo for GitHub (remove AI clutter)

Strip **local-only** AI scaffolding so the repo looks lean on GitHub. Inverse of **`/bootstrap`** — deletes placeholders and agent folders, not application source.

## Phase 1 — Inventory (no deletes yet)

Scan repo root and report what exists:

### Tier A — remove by default (when approved)

| Path | Typical contents |
|------|------------------|
| `.agents/` | Agent context from bootstrap |
| `.claude/` | Claude Code / project settings |
| `.gemini/` | Gemini CLI / project config |
| `.aider*` / `.aider.conf.yml` | Aider |
| `.continue/` | Continue config |
| `.copilot/` | Copilot workspace files |
| `.windsurf/` | Windsurf |
| `.codex/` | Codex |
| `AGENTS.md` | Only if **empty** or bootstrap placeholder (≤5 lines, no product spec) |

### Tier B — `docs/` scaffold (empty placeholders only)

From bootstrap — delete **only** if file is empty or whitespace-only:

- `docs/SPEC.md`, `DESIGN.md`, `ARCHITECTURE.md`, `API.md`, `TESTING.md`, `DEPLOYMENT.md`
- `docs/README.md` if only the bootstrap index table

**Keep** any `docs/` file with real product content (non-empty paragraphs, diagrams, API specs).

### Tier C — `.cursor/` (ask every time)

| Subpath | Default on publish-clean |
|---------|-------------------------|
| `.cursor/commands/` | Remove (slash prompts — local workflow) |
| `.cursor/skills/` | Remove |
| `.cursor/rules/` except user may want to **keep** rules for contributors | Ask |
| `.cursor/docs/` | Remove (toolkit manuals) |

If `.cursor/` is the **main purpose** of this repo (e.g. Cursor Maxxing toolkit), **skip Tier C** unless I say `include-cursor`.

### Never delete

- `src/`, `app/`, `lib/`, `packages/`, `tests/`
- `package.json`, lockfiles, `pyproject.toml`, `go.mod`, etc.
- Root `README.md` with real project description
- `LICENSE`, `.github/`, CI configs
- `.env.example`, `docker-compose*`
- Filled `docs/` (Tier B exception above)

## Phase 2 — Report

```markdown
## Clean plan
| Path | Tier | Size / note | Action |
|------|------|-------------|--------|
| .agents/ | A | … | DELETE |
| docs/SPEC.md | B | empty | DELETE |
| .cursor/ | C | … | SKIP (unless include-cursor) |

**Estimated:** N files, M folders
```

Flag anything ambiguous (non-empty `docs/`, custom rules worth keeping).

## Phase 3 — Wait for approval

Stop. Present:

```
Y  — Delete everything in the plan (default tiers)
K  — Keep .cursor/ (delete A + B only)
A  — Aggressive: also delete non-empty docs/ placeholders I name
N  — Cancel
```

Parse my reply for: `include-cursor`, `keep-rules`, `keep-docs`, or paths to **never** touch.

**Do not** `git rm`, `Remove-Item`, or delete until I choose **Y**, **K**, or **A**.

## Phase 4 — Execute

1. `git status` before deletes
2. Delete approved paths (folders recursive)
3. Remove empty parent dirs
4. If `docs/` is empty after clean, remove `docs/` folder
5. `git status` after — list deleted paths

## Phase 5 — Git hygiene (suggest only)

If `.gitignore` exists, suggest lines to add so clutter does not return:

```gitignore
.agents/
.claude/
.gemini/
.aider*
```

Offer to append — **do not** edit `.gitignore` unless I say yes.

## Principles

- **Publish-ready** — what remains should look like a normal app/library repo
- **Reversible** — remind me deletes are local until commit; use git to restore if needed
- **No source damage** — when unsure, skip and ask
- Pairing: use **`/bootstrap`** again to recreate scaffold locally
