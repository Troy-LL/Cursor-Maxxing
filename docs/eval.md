# Eval — opt-in model-plan table

Gold for `blueprint/model-plan.md` in [004](decisions/004-blueprint-routing.md). Skip this file on ordinary kickoff. Skip unless the EVAL-TASK asks for a cost class or model plan. `docs/evals/dummies/t0-cli` is a **red-health fixture only** (must start failing). It is not a routing arm.

The table stays EXPERIMENT until a dummy whose EVAL-TASK asks for a cost class has n ≥ 3 traces per arm in `docs/evals/traces/` (copy `docs/evals/trace-fixture.md`). Do not promote 004 from t0-cli or from one run.

## Floor

Routed ≥ best fixed arm on success, and cheaper than always-frontier. Fail: delete the table from `model-plan.md`, keep triage + language interview, record why in 004.

## Scrape

Model class and token/cost from Cursor's usage dashboard. Success = that dummy's `Red` command exit 0 after the agent stops.
