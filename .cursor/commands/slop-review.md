# Slop review — uncommitted changes vs main

Audit all uncommitted work against `main` (or `master` if that is the default branch). Find AI slop, inconsistency, and real bugs. Then either **commit clean changes** or **sub-refactor** the underlying problems — never commit slop to get it off the plate.

## Phase 1 — Gather diffs

Run in parallel where possible:

1. `git status`
2. `git branch --show-current`
3. Detect default branch: `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null` or try `main` then `master`
4. `git diff` (unstaged)
5. `git diff --staged` (staged)
6. `git diff <default-branch>...HEAD` (committed on branch but not in main)
7. `git diff <default-branch>` (everything different from main including uncommitted)
8. `git log <default-branch>..HEAD --oneline` (if on a feature branch)

If there are **no** uncommitted or branch-local changes, say so and stop.

Read touched files for **surrounding context** — match naming, patterns, and imports already in the repo.

## Phase 2 — Slop & quality audit

Review every changed hunk. Flag issues with severity:

| Severity | Meaning |
|----------|---------|
| **BLOCK** | Wrong, insecure, broken, or would embarrass in review — must fix before commit |
| **SLOP** | AI-typical noise or inconsistency — fix in sub-refactor or drop |
| **NIT** | Style only — fix only if trivial |

### AI slop signals (check each)

- **Scope creep** — unrelated refactors, drive-by renames, or "while I'm here" edits
- **Over-engineering** — new helpers/abstractions used once; unnecessary wrappers or factories
- **Comment slop** — obvious comments, tutorial tone, "Initialize variable" style noise
- **Defensive excess** — try/catch around impossible paths; redundant null/undefined guards
- **Inconsistency** — mixed naming, import style, error handling, or patterns vs neighboring files
- **Duplicate logic** — reimplemented utilities that already exist in the project
- **Placeholder residue** — `TODO`, `FIXME`, mock data, `console.log`, debug prints left in
- **Generic mush** — vague names (`data`, `result`, `handleStuff`), dead code, unused imports
- **Copy-paste drift** — boilerplate from another stack that does not match this codebase
- **Test theater** — tests that assert implementation or add no meaningful behavior coverage
- **Doc/changelog bloat** — markdown or comments the user did not ask for in this change

### Compare to main

- Does the change **belong** in one focused commit, or should it be split?
- Does behavior match intent implied by the diff (no silent behavior changes)?
- Any conflict with `.cursor/rules/` or project conventions?

## Phase 3 — Report (required before any edits)

Produce this structure:

### Summary
- Branch, default branch, files changed (count), lines +/- (approx)
- One sentence: **ready to commit** / **refactor first** / **do not commit**

### Findings table

| File | Severity | Issue | Suggested fix |
|------|----------|-------|---------------|

### Verdict

- **CLEAN** — no BLOCK/SLOP; nits only → offer commit
- **REFACTOR** — BLOCK or SLOP present → list ordered fix plan (smallest diff first)
- **STOP** — change is wrong direction → explain and ask before reverting anything

## Phase 4 — Wait for my decision

Present exactly these options and **stop until I choose**:

```
A) Commit as-is (only if CLEAN or I explicitly accept nits)
B) Sub-refactor — fix BLOCK + SLOP, then re-run this review
C) Show me the proposed commit message first (no commit yet)
D) Discard / revert specific files (I will name them)
```

**Do not** `git add`, `git commit`, or `git push` unless I reply with **A** or **C then A**.

## Phase 5 — Sub-refactor (only if I choose B)

When refactoring:

1. Fix **root cause**, not symptom — prefer deleting slop over wrapping it
2. **Minimal diff** — only files/hunks flagged BLOCK/SLOP; no new features
3. Reuse existing project helpers; align with surrounding code
4. Remove debug logs, unused imports, and spurious comments you added
5. Re-run Phase 1–3 and report new verdict

Repeat until **CLEAN** or I choose A.

## Phase 6 — Commit (only if I choose A or approve after C)

1. Stage only intentional files — never stage `.env`, credentials, or accidental artifacts
2. Propose message from `git log -5 --oneline` style, then commit when I confirm
3. `git status` after commit to verify clean

## Principles

- Be blunt about slop; praise what is genuinely good
- Prefer **delete** over **comment** over **abstract**
- If unsure whether something is intentional, **ask** — do not guess
- One concern per commit when splitting would make review easier
