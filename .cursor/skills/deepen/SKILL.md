---
name: deepen
description: >-
  Survey a codebase for deepening opportunities (more behaviour behind a
  smaller interface) and wait for the user to pick one. Use when the user
  says deepen, deepening, or improve codebase architecture. Do not start a
  rewrite. Do not run this unprompted.
disable-model-invocation: true
---

# Deepen

Find candidates. Do not fix them.

## Survey

Read the modules the current task touches. List 3–7 deepening opportunities.

For each candidate:

- What is shallow today (wide interface, leaked guts, or a god file)
- What "deeper" would mean in one sentence
- Risk if left alone

Do not implement. Do not open a second survey file. Put the list in the chat.

## After they pick

If they pick one, run the `grill` skill on that candidate only. If they said grill docs, use the docs flag. Stop after grill unless they ask to implement — that is `/sdd-eng`.
