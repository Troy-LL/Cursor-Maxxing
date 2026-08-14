# PR review

Review the **branch vs default branch** for human reviewers. Not a slop-only pass — use **`/slop-review`** before commit if you need slop/LOC cleanup first.

## Phase 1 — Gather

1. Default branch: `main` or `master`
2. `git log <default>..HEAD --oneline`
3. `git diff <default>...HEAD --stat`
4. `git diff <default>...HEAD` (read key hunks; sample large diffs by area)
5. Read `AGENTS.md` if present, then `README.md`, `docs/architecture.md`, `docs/design.md` if they exist (that order). Do not glob `docs/decisions/`. Cite one ADR path if the diff needs it. Missing `docs/api.md` / `SPEC.md` is correct — review the owner, not a twin.

## Phase 2 — Review lens

| Area | Look for |
|------|----------|
| **Correctness** | Logic bugs, edge cases, race conditions |
| **Security** | AuthZ, injection, secrets, unsafe defaults |
| **Breaking changes** | API/schema/config changes without migration notes |
| **Tests** | Missing coverage on new behavior; brittle tests |
| **Design fit** | Matches `docs/architecture.md` / `docs/design.md` if present |
| **Ops** | Deploy, env vars, migrations called out in diff |

Do **not** focus on style nits unless they violate project rules in `.cursor/rules/`.

## Phase 3 — Report

```markdown
## Summary
[2–4 bullets for the reviewer]

## Scope
- Branch / base / commits / files (+/- lines)

## What changed (by area)
[Features | Fixes | Refactor | Chore — bullet per area]

## Risks
[Must understand before merge — ranked]

## Test plan
[ ] concrete checks for QA or author

## Questions for author
[Only if blocking or ambiguous]
```

Severity tags: **BLOCK** (must fix), **SHOULD** (fix before or right after merge), **NIT** (optional).

## Phase 4 — Wait

Do not change code or push unless I ask. Offer:

```
F) Fix BLOCK items
S) Suggest commit/message split if scope is too large
N) No changes — review only
```

## Principles

- Reviewer voice, not rewrite-the-PR
- Cite `file:line` for BLOCK/SHOULD
- If diff is huge, prioritize high-risk paths first
