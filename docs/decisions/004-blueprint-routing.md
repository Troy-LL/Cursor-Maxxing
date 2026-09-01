# 004: /blueprint — kickoff triage, language interview, and tier-based model planning

Status: Accepted (model-tier table = EXPERIMENT until routing evidence lands)

## Context

Cursor's Auto routes each call; nothing in the pack or the IDE helps a developer set a deliberate model plan for a whole job before it starts, and greenfield projects get whatever language the agent defaults to unless someone asks. Two gaps, one workflow.

Research grounding:

- Cursor bills two pools — an included-usage pool for its own models and API-rate billing for frontier models (docs/models-and-pricing). Names and rates change often; the pack stores cost *classes*, not model names.
- SWE-Router (arXiv:2607.00053): prompt-only routing has an information-theoretic floor; cheap-first exploration with escalation on trajectory evidence cuts cost at matched resolution → "start one tier down, escalate after two failures."
- Harness-Bench (arXiv:2605.27922) and Claw-SWE-Bench (arXiv:2606.12344): capability is a property of model × harness configuration, and harness choice alone moves outcomes up to ~27 pp → plans must name where work runs (inline vs Task), not just which model.
- Router-eval literature (e.g. arXiv:2608.14641): many routers are near-constant selectors; fixed-arm baselines are mandatory controls → our claims stay EXPERIMENT until routed beats fixed arms under `scratch/evals/routing-experiment.md`.

## Decision

1. Ship `.cursor/skills/blueprint/SKILL.md` + `/blueprint` command: complexity triage (T0–T3), intent gate to `/grill`, language interview for greenfield only, inline-vs-Task fork offered once. The model-tier table lives in `model-plan.md` and loads only when they asked about cost, tokens, or the picker.
2. The skill advises; per-call routing stays with Auto. No wrapper. Ordinary kickoff does not name models. Not always-on: the description excludes mid-task, one-line edits, and unsolicited model picking.
3. Evidence for the opt-in table is `docs/eval.md` in this guidebook (traces in `docs/evals/traces/`). Product installs do not load that file.
4. Model names are resolved from the live picker at run time; the pack records cost classes only.

## Alternatives considered

- **Runtime router skill** — rejected: wraps Auto, violates [001](001-native-first.md), and router evals show naive routers lose to constant policies.
- **Ship tier table as fact** — rejected by Data Engineer: zero local traces exist; benchmark scores are not deployment evidence.
- **Fold into `/unfurnished` intake** — deferred: intake runs every job; blueprint is kickoff-scoped and would add tax to routine edits.

## Council record

| Role | Verdict | Key point |
|------|---------|-----------|
| AI Engineer | SHIP | On-demand; raises first-shot odds on multi-phase jobs via upfront tiering; no context tax between runs |
| Software Engineer | SHIP | Passes write-skill conventions post-revision; ~70 lines; done-lines on every step; catalog wired (plugin.json, README) |
| Data Engineer | SHIP framework / EXPERIMENT content | Protocol has fixed arms, controls, n≥3 rule; no traces yet, so the tier table carries no evidentiary weight |
| Devil's Advocate | REVISE→SHIP | Found 2 blockers (billing facts stated as certainty; T3 answer key leaked to the evaluated agent) plus 5 minors; all fixed before ship |

Overall: **SHIP** the workflow; **EXPERIMENT** the model-tier recommendations until `scratch/evals/routing-experiment.md` has a filled matrix.

## Consequences

- `/blueprint` joins the command surface; README documents it.
- Promotion path: fill the routing matrix from real Cursor runs; if routed ≥ best fixed arm on success and cheaper than always-frontier, promote the tier table to Accepted and cite the traces here.
- Eviction trigger: if the experiment shows routing never beats the best fixed arm, delete the tier table and keep only the triage + language interview.
