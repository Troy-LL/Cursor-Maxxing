# Find skills for this project

Discover installable agent skills from [skills.sh](https://skills.sh/) tailored to **this repo's** stack, workflows, and gaps — not generic guesses.

Inspired by [vercel-labs/skills/find-skills](https://www.skills.sh/vercel-labs/skills/find-skills). Optional upstream install:

`npx skills add https://github.com/vercel-labs/skills --skill find-skills`

## Phase 1 — Project context (required)

Build a **Project Profile** before searching. Do not skip files.

### Stack & tooling

Read and summarize:

- Root manifests: `package.json`, `pnpm-workspace.yaml`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `Gemfile`, `composer.json`, etc.
- Config: `tsconfig.json`, `next.config.*`, `vite.config.*`, `docker-compose.*`, CI under `.github/workflows/`
- Lockfiles or package manager hints (npm, pnpm, yarn, bun, poetry, uv)

### Docs & intent

- `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `docs/**`, `.cursor/docs/**`
- Existing `.cursor/rules/*.mdc`, `.cursor/skills/**/SKILL.md` — list what is **already** covered (do not recommend duplicates)

### Codebase shape

- Top-level tree and main source roots (`src/`, `app/`, `lib/`, `packages/`, `backend/`, etc.)
- Dominant languages and frameworks from file extensions and imports
- Inferred workflows: testing, deploy, design system, DB, auth, mobile, monorepo, etc.

### Output: Project Profile (short)

```markdown
## Project Profile
- **Type:** (e.g. Next.js monorepo, Python API, etc.)
- **Stack:** languages, frameworks, test runners, package manager
- **Workflows:** what this repo actually does (CI, deploy, e2e, etc.)
- **Gaps:** areas with no rule/skill coverage that external skills might fill
- **Already installed:** local + global skills if visible under `.cursor/skills/` or `~/.cursor/skills/`
```

## Phase 2 — Derive search queries

From the profile, write **3–6 specific** `npx skills find` queries (not vague).

| Profile signal | Example query |
|----------------|---------------|
| Next.js + React | `nextjs react performance` |
| Playwright in repo | `playwright e2e testing` |
| PR-heavy / no skill | `pr review` |
| Design/UI focus | `frontend design ui` |
| Docs sparse | `readme changelog api-docs` |

Add queries for the user's **stated goal** in this message if they gave one.

## Phase 3 — Search the ecosystem

Run searches (network required):

```bash
npx skills find <query>
```

Run **each** derived query. If a query fails or returns nothing, try one alternate keyword set.

Also check [skills.sh](https://skills.sh/) leaderboard mentally for the domain (React, testing, deploy) — prefer well-known official packs when they match the profile.

## Phase 4 — Verify before recommending

**Do not recommend from search output alone.** For each candidate:

| Check | Guidance |
|-------|----------|
| **Relevance** | Must match this project's stack/task, not generic buzzwords |
| **Install count** | Prefer 1K+; caution under 100 |
| **Source** | Prefer `vercel-labs`, `anthropics`, `microsoft`, known orgs |
| **Not duplicate** | Skip if equivalent skill already in `.cursor/skills/` |
| **Security** | Mention if audit badges exist on skills.sh; flag unknown authors |

Drop poor fits even if they rank high in CLI output.

## Phase 5 — Report

### Recommended skills (max 5)

| Priority | Skill | Why it fits this repo | Installs | Install command |
|----------|-------|----------------------|----------|-----------------|
| 1 | … | tied to Profile gap | … | `npx skills add …` |

Each row must include:

- **Install command** (exact, copy-pasteable)
- **Link:** `https://skills.sh/<owner>/<repo>/<skill>` when known

### Also ran

List queries executed: `npx skills find …`

### No good match?

Say so honestly. Offer:

1. Help the task directly without a skill
2. `npx skills init <name>` if they do this often
3. `/write-command` or **write-cursor-rules** for a project-local rule/skill

## Phase 6 — Wait for my decision

Stop after the report. Present:

```
I) Install skill #N globally (-g)
P) Install skill #N in this project only
S) Search again with different keywords (tell me what)
N) None — proceed without installing
```

**Do not run `npx skills add` unless I choose I or P.**  
For install: use `-y` only with my confirmation; prefer project install unless I said global.

After install, note path (`.cursor/skills/` or `~/.cursor/skills/`) and suggest `/toolkit` or reopening skills list.

## Principles

- **Context first, search second** — reading the repo beats guessing from chat
- **Tailored** — every recommendation cites a Profile line ("you use X, so Y")
- **Quality over quantity** — 2 great skills beat 10 mediocre ones
- **No slop installs** — never batch-install without approval
