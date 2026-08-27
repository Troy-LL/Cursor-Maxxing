# Model plan (opt-in)

Read this file only when they asked which model, which cost class, or how to spend tokens. Skip on ordinary kickoff. Auto still routes each call.

Cursor prices two pools: included-usage for its own models and API-rate for frontier models. Check the live picker for names and rates. Map the already-named tier to a cost class, not a brand:

| Tier | Plan |
|------|------|
| T0 | Cheapest included-usage class, inline chat. No ceremony. |
| T1 | Included-usage standard effort; a Task subagent only when parallel attempts pay. |
| T2 | High-effort included-usage flagship or mid-tier API-rate class; Task subagents for isolated modules. |
| T3 | One top-tier architecture pass once intent is locked; mechanical edits drop back down-tier afterward. |

When uncertain, start one tier below your guess and escalate after two failed attempts. Name where each phase runs (picker vs Auto). Done when: every planned phase names its model source.

Do not name a vendor. Gold for this table is guidebook-only (`docs/eval.md`) — do not load it in a product repo.
