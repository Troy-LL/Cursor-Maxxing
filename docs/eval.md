# Eval — cost class for a repo, and the 004 table

Gold for `blueprint/model-plan.md` in [004](decisions/004-blueprint-routing.md) and for a per-repo class card. Skip this file on ordinary kickoff. Skip unless the EVAL-TASK asks for a cost class or model plan.

`docs/evals/dummies/t0-cli` is a **red-health fixture only** (must start failing). It is not a routing arm.

The first qualifying dummy is `docs/evals/dummies/t1-nook`. Its EVAL-TASK asks for a cost class. Success is that dummy's `Red` command exit 0 after the agent stops, and `docs/design.md` still contains every line it had before the run except the one empty-copy fact.

The 004 table stays EXPERIMENT until t1-nook has n ≥ 3 traces per arm in `docs/evals/traces/` (copy `docs/evals/trace-fixture.md`). Do not promote 004 from t0-cli or from one run.

A per-repo class card is the cheapest cost class that hits pass@k on that repo's frozen Red tasks. Same traces fill 004. Map the class to a live picker name at run time. Do not pin a vendor model. Do not wrap Auto.

## Floor

Routed ≥ best fixed arm on success, and cheaper than always-frontier. Fail: delete the table from `model-plan.md`, keep triage + language interview, record why in 004.

## Scrape

Model class and token/cost from Cursor's usage dashboard. Success = that dummy's `Red` command exit 0 after the agent stops, plus the design-file keep rule above when the dummy ships a `docs/design.md`.
