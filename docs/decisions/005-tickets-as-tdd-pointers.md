# 005: Tickets are local TDD pointers, not a tracker product

Status: Accepted

## Context

TDD is weak when the agent does not know where to look or which command must go red first. Issue trackers (GitHub, Linear) and Matt Pocock's `to-tickets` look like the fix. They assume a host and a stack. Cursor already has Plan, GitHub/Linear integrations, and `scratch/`. Wrapping a tracker violates [001](001-native-first.md) and [003](003-workflow-not-stack.md). Leaving only `tdd.mdc` leaves no pointer.

## Decision

We will keep open work items as `scratch/tickets/<slug>.md` with four fields: Done, Look, Red, Status. They are not mapped and not committed. `tdd` runs the `Red` command before production code. A decision that would look right if violated is still one ADR via `/sdd`. A scored probe is still `docs/eval.md`. We will not open GitHub or Linear unless the user named that tracker.

## Consequences

The `ticket` skill ships. Soft-off skips it with the other pack slots. GitHub/Linear stay optional and host-owned.
