# Development guide

How humans and AI should work on this project — alignment, etiquette, and tooling.

**Audience:** You (the developer) and any agent in Cursor. Read this once after `/bootstrap`, then `@DEVELOPMENT.md` when starting a new feature or onboarding an agent.

---

## Source of truth

| Location | Role |
|----------|------|
| **`docs/`** | Product truth — requirements, design, architecture, API, testing, deployment |
| **`.cursor/rules/`** | Coding standards (auto or `@rule-name`) |
| **`.cursor/skills/`** | Multi-step playbooks the agent discovers or you name in chat |
| **`.cursor/commands/`** | Explicit `/` workflows you trigger |
| **`.agents/`** | Optional shared context for agents (local; removed by `/clean`) |
| **Application code** | `src/`, `app/`, `lib/`, etc. — implementation, not policy |

**Rule:** Decisions live in `docs/` first. Code follows docs. If code and docs disagree, fix the mismatch — do not silently drift.

### Which doc to `@` first

| Task | Start with |
|------|------------|
| New feature or scope question | `@docs/SPEC.md` |
| UI/UX work | `@docs/DESIGN.md` |
| Structure, modules, data model | `@docs/ARCHITECTURE.md` |
| Endpoints, contracts, payloads | `@docs/API.md` |
| Test strategy or coverage | `@docs/TESTING.md` |
| CI/CD, hosting, envs | `@docs/DEPLOYMENT.md` |
| How to work on this repo | `@docs/DEVELOPMENT.md` (this file) |

If a doc does not exist, it was pruned during bootstrap distillation — use the closest remaining doc or ask to restore the shell.

---

## Lifecycle

```
/bootstrap  →  build locally  →  /slop-review  →  commit  →  /clean  →  push
     ↑                              ↑
  spec → docs/                  before every commit
```

1. **`/bootstrap`** — Scaffold `docs/`, `.cursor/` slots, and this file. Distill your ideation spec into the minimal `docs/` set.
2. **Build** — Implement against populated docs. Add rules/skills when the stack is clear.
3. **`/slop-review`** — Audit uncommitted work before commit; fix slop, do not commit noise.
4. **`/clean`** — Strip local-only AI scaffolding before GitHub (keeps filled `docs/` and real source).
5. **Publish** — Push a repo that reads like a normal project, not a prompt dump.

Re-run **`/bootstrap`** locally anytime you need the scaffold back after `/clean`.

---

## Human + AI workflow

### Before asking the agent to code

1. **Anchor context** — `@docs/SPEC.md` plus the relevant sibling doc (architecture, API, etc.).
2. **State the outcome** — What should work when done? What is explicitly out of scope?
3. **Point at examples** — Reference existing files, patterns, or tests to match.
4. **Name constraints** — Performance, security, backwards compatibility, deadline.

### How the agent should behave

| Do | Don't |
|----|-------|
| Read surrounding code and docs before editing | Invent requirements not in `docs/` or your message |
| Smallest correct diff for the task | Refactor unrelated files "while here" |
| Match naming, imports, and patterns in neighbors | Add abstractions used only once |
| Run commands and tests when available | Give up after one failure |
| Ask when intent is ambiguous | Guess and ship speculative behavior |
| Update `docs/` when behavior or contracts change | Leave docs stale after API/schema changes |

### Session patterns

| Mode | Use when |
|------|----------|
| **Plan** (`/plan` or "plan first") | Large feature, unclear tradeoffs, many files touched |
| **Agent** (default) | Clear task with anchored docs |
| **Ask** (`/ask`) | Exploration, architecture questions, no edits |

For "why did we choose X?" use evidence-backed rationale. For "how does X work?" use a walkthrough of runtime flow and ownership.

---

## Commands & skills

Use **Cursor native** tools first, then project/toolkit commands.

### Built into Cursor

| Tool | Use for |
|------|---------|
| **`/rules`** | Create or edit `.cursor/rules/*.mdc` |
| **`/commands`** | Create or edit slash commands |
| **`/plan`** | Design before implementation |
| **`/ask`** | Read-only exploration |

### Recommended project commands

Install or copy from the Cursor Maxxing toolkit as needed.

| Command | When |
|---------|------|
| **`/bootstrap`** | New repo or re-scaffold after `/clean` |
| **`/slop-review`** | Before every commit — slop, scope creep, consistency |
| **`/clean`** | Before first push to GitHub — remove local AI clutter |
| **`/get-cursor-rules`** | Add stack-specific rules from [cursor.directory](https://cursor.directory/) |
| **`/find-skills`** | Discover skills for your stack on [skills.sh](https://skills.sh/) |
| **`/pr-review`** | Branch vs main — reviewer narrative before opening a PR |

### Skills

| Skill | When |
|-------|------|
| **`document-distillator`** | Runs with `/bootstrap` — spec → minimal `docs/` |
| **`get-cursor-rules`** | Directory-first rule install + custom `.mdc` authoring |

Name a skill in chat when the task matches its description (e.g. "Using get-cursor-rules, add a TypeScript logging rule").

### Opt-in rules

| Rule | When |
|------|------|
| **`@lean-coder`** | You want a 200 LOC cap per module and strict lean structure |

Rules are opt-in unless marked `alwaysApply` in frontmatter. Do not assume `@lean-coder` unless you or this doc explicitly enable it for the project.

---

## Development etiquette

### Scope

- **One concern per change** — easier review, easier revert.
- **Fix the root cause** — prefer delete over comment over abstract wrapper.
- **No drive-by edits** — typos in untouched files can wait unless you are already there for a related reason.

### Code quality

- Read neighboring files before writing; match the repo's voice.
- Functions stay focused; extract when nesting or branching deepens.
- Handle errors at boundaries — no blanket try/catch.
- No dead code, debug logs, or placeholder `TODO`s left behind.
- Comments explain **why**, not **what**.

### AI-specific anti-patterns (slop)

Treat these as bugs, not style:

- Scope creep and unrelated refactors
- Generic names (`data`, `handleStuff`, `utils.ts` for one call site)
- Tutorial comments and changelog prose in source files
- Duplicate logic that already exists in the project
- Tests that assert implementation details only
- Markdown or docs the user did not ask for in that change
- Over-engineering — factories, wrappers, "helper" layers for single use

Run **`/slop-review`** when any of the above might be present.

### Documentation

- **Product docs** (`docs/*.md`) — update when requirements, APIs, or architecture change.
- **This file** — update when team workflow or tooling choices change.
- Do not add README sections, ADRs, or new doc files unless the task calls for it.

### Dependencies & secrets

- Never commit `.env`, credentials, or API keys.
- Prefer `.env.example` with dummy values for required vars.
- Do not add libraries without a clear use — match the stack already in the repo.

---

## Git workflow

| Action | Guidance |
|--------|----------|
| **Branch** | Short, descriptive (`feat/auth-callback`, `fix/rate-limit`) |
| **Commits** | Only when you explicitly ask the agent to commit |
| **Messages** | Imperative, focused on *why* ("fix session expiry on refresh" not "update files") |
| **Pre-commit** | `/slop-review` → fix BLOCK/SLOP → commit |
| **Pre-push** | `/clean` if publishing; ensure filled `docs/` are kept |
| **PR** | `/pr-review` for reviewer summary; align with `docs/SPEC.md` |

The agent must **not** force-push, skip hooks, or amend commits unless you explicitly request it.

---

## Testing & verification

Follow `@docs/TESTING.md` when it exists. Otherwise:

1. Run the project's existing test/lint/build commands before calling work done.
2. Add tests only when they cover real behavior — not theater.
3. Manual checks: list concrete steps in PR description or chat.

---

## Before publishing to GitHub

1. Run **`/clean`** — approve the plan; keep non-empty `docs/` and any rules you want contributors to share.
2. Confirm root **`README.md`** describes the product, not the bootstrap process.
3. Optional: add `.gitignore` entries for `.agents/`, `.claude/`, `.gemini/` so clutter does not return.

---

## Alignment checklist

Use before merging or handing off:

- [ ] Behavior matches `@docs/SPEC.md` and relevant sibling docs
- [ ] No AI slop (run **`/slop-review`** if unsure)
- [ ] Docs updated if API, schema, or architecture changed
- [ ] No secrets or env files staged
- [ ] Tests/lint pass (per `@docs/TESTING.md` or project scripts)
- [ ] Diff is minimal and reviewable — split if scope grew

---

## Quick prompts (copy-paste)

**Start a feature**

> `@docs/SPEC.md` `@docs/ARCHITECTURE.md` — Implement [X]. Out of scope: [Y]. Match patterns in `[path/to/similar/file]`.

**Pre-commit**

> `/slop-review`

**Add stack rules**

> `/get-cursor-rules` — I need rules for [language/framework].

**Publish**

> `/clean` — keep filled docs and `.cursor/rules/` if we use shared rules.
