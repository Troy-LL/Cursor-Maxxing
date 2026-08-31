---
name: after-compact
description: >-
  Rehydrate after context compact. Use when the chat shows a summarized
  conversation, a compact banner, or the user says after-compact or keep-alive.
  Do not use when scratch/keep-off exists unless the user asked. Do not dump
  the old transcript back into context.
---

# After compact

Restore significance only. Do not restore the window. Default is on.

## Arming

If `scratch/keep-off` exists and the user did not ask for this skill, stop.
If they asked, or the chat looks compacted, run the card. `scratch/keep-alive` is leftover; ignore it.

## Card

State, in this order, and nothing else:

1. One-line job
2. Last locked decision
3. Open todos
4. Re-run `/voice plain` or `/voice ste` if a register was on
5. `@yagni` if the ladder was on
6. Re-`@` or `/` the skill the summary still names

Then continue the work. Do not paste prior tool output. Do not write a session diary.
