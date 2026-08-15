---
name: after-compact
description: >-
  Rehydrate after context compact. Use when the chat shows a summarized
  conversation, a compact banner, or the user says after-compact or keep-alive.
  Use if scratch/keep-alive exists and history looks compacted. Do not dump
  the old transcript back into context.
---

# After compact

Restore significance only. Do not restore the window.

## Arming

If `scratch/keep-alive` is missing and the user did not ask for this skill, stop.

## Card

State, in this order, and nothing else:

1. One-line job
2. Last locked decision
3. Open todos
4. Re-run `/voice plain` or `/voice ste` if a register was on
5. `@yagni` if the ladder was on
6. Re-`@` or `/` any skill that was in force (grill, deepen, write-skill, sdd, sdd-eng)

Then continue the work. Do not paste prior tool output. Do not write a session diary.
