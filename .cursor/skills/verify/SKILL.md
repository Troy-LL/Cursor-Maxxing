---
name: verify
description: >-
  Definition-of-Done in-turn verification gate. Use when completing a feature,
  refactor, bugfix, or multi-file change, or when the user says verify, /verify,
  check done, or to prove the work is runnable before yielding turn.
---

# Verify (Definition-of-Done Gate)

Autonomous pre-yield verification across lints, typechecks, stubs, and runtime health.

## 4-Gate Verification Process

Before declaring any task or feature complete, execute all 4 gates in-turn:

1. **Gate 1 — Linter Cleanliness**:
   - Run `ReadLints` on all newly created or edited files.
   - Resolve any introduced linter errors immediately.

2. **Gate 2 — Typecheck & Compilation**:
   - If TypeScript/typed project, run `tsc --noEmit` (or language compiler) via `Shell`.
   - Ensure zero type errors and clean exit code.

3. **Gate 3 — Anti-Stub Verification**:
   - Verify no placeholder code, `// TODO: implement later`, or fake mock stubs remain in modified code.
   - Every function and route must be fully wired.

4. **Gate 4 — Runtime & Server Health**:
   - Inspect active dev server output in terminal files for runtime crashes, unhandled promise rejections, or 500 errors.
   - If a test suite exists for the modified module, execute it via `Shell` to confirm green status.

## Bounded Repair Loop

If any gate fails:
- Repair the failure in the current turn.
- Re-run the failed gate (max 2 repair cycles).
- If still failing, present the exact root cause and error output to the user.

If a gate has nothing to run, mark it **N/A**. N/A is not a pass. Do not yield "green" if every applicable gate was N/A and you ran no command and no `ReadLints`.

## Done

Verification is done when every applicable gate passed with a real run, and every other gate is marked N/A.
