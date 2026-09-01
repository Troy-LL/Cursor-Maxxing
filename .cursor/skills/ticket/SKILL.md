---
name: ticket
description: >-
  Writes a local work item that points TDD at a path and a first red command.
  Use when a feature or fix has no pointer to the code to change or no named
  failing test. Do not use for one-line edits. Do not open GitHub or Linear
  unless they named that tracker.
---

# Ticket

A ticket is a TDD pointer, not a product tracker. Open items live in `scratch/tickets/` (do not commit, do not map, even if they asked). Durable decisions still go through `/sdd` as one ADR.

## Open

If `scratch/tickets/` already has an open item for this change, use it. Do not mint a second.

Otherwise write `scratch/tickets/<slug>.md`:

```
# <slug>
Done: <one falsifiable line>
Look: <paths>
Red: <command that must fail first>
Status: open
```

Done when: that file exists and `Red` is a real command.

## Red

Run the `Red` command. Watch it fail. Then implement (`sdd-eng` + `tdd`). Do not write production code before that fail.

## Close

When Done is true and verify passed: set `Status: closed` or delete the file.

If a decision survived that would look right if violated → `/sdd` for one ADR. If a scored probe survived → `docs/eval.md`. Do not promote the ticket itself into `docs/`.

## Named tracker

Only if they said GitHub, Linear, or another tracker: open the same Done/Look/Red there with the CLI already on the machine. Local `scratch/tickets/` still exists. Do not add a tracker dependency.

## Done

Open, red, implement, close. One ticket per change.
