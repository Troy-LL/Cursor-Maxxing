# Next steps — /blueprint evidence loop (deferred)

Notes for the dev. The `/blueprint` workflow is shipped; its model-tier
recommendations are **EXPERIMENT** on purpose. We cannot run the routing
experiment yet because Cursor is not installed/set up. Nothing here blocks
using the pack today — only promoting the tier table to Accepted.

## Where we stopped

- Shipped: `.cursor/skills/blueprint/SKILL.md`, `/blueprint` command,
  catalog wiring, [ADR 004](decisions/004-blueprint-routing.md).
- Parked uncommitted-by-design: `scratch/dummies/` (3 graded fixtures) and
  `scratch/evals/` (trace template + experiment protocol).
- Zero traces captured. Every tier→model claim is a default, not evidence.

## When Cursor is available

1. Install the pack (Customize → Plugins → import `Troy-LL/Cursor-Maxxing`).
2. Open `scratch/dummies/t0-cli` as a project. Paste its EVAL-TASK line
   verbatim. Run each arm per `scratch/evals/routing-experiment.md`:
   routed (`/blueprint` first), always-cheap, always-frontier.
3. After every run, copy `scratch/evals/trace-fixture.md` and fill it from
   the usage dashboard + checkpoint history.
4. Repeat for `t1-api` (deterministic grading) and `t3-spec` (grade the
   interview against `GRADER.md` — never show it to the agent).
5. n ≥ 3 per cell. Single runs are anecdotes; do not update the ADR from one.

## Decision gate (from ADR 004)

- Routed ≥ best fixed arm on success AND cheaper than always-frontier →
  promote tier table to Accepted, cite traces here.
- Routing never beats the best fixed arm → delete the tier table from the
  skill, keep triage + language interview, record why in ADR 004.

## Smaller follow-ups

- Watch Cursor's model picker for pool/name changes; the skill stores cost
  classes only, so no edit should be needed unless pool structure changes.
- If `/grill` handoff from blueprint feels like double interviewing on real
  projects, tighten section 2 of the skill and note it in ADR 004.
