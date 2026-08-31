# Next steps — opt-in model-plan evidence

Protocol: [docs/eval.md](eval.md). T0 dummy [docs/evals/dummies/t0-cli](evals/dummies/t0-cli) is red-health only, not a routing cell.

## Where we are

- Ordinary kickoff: triage + language + fork. Model plan loads only if they asked about cost.
- Tier table = EXPERIMENT. Qualifying dummy is `docs/evals/dummies/t1-nook`. Zero traces yet. t0-cli stays red-health only.
- Tickets: `scratch/tickets/` ([ADR 005](decisions/005-tickets-as-tdd-pointers.md)).

## Decision gate (from ADR 004)

- Routed ≥ best fixed arm AND cheaper than always-frontier → promote the table in `model-plan.md`.
- Routing never beats the best fixed arm → delete that table, keep triage + language.
