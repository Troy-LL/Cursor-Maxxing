---
name: write-skill
description: >-
  Author or edit an Agent Skill (SKILL.md) for this repo. Use when creating a
  skill, changing a skill, or the user asks how to write a skill. Do not use
  for User Rules, .mdc files, or slash-command stubs — those are different
  slots. Do not wrap /create-skill; that is the authoring UI.
---

# Write a skill

A skill is a workflow with a pointer. It is not a rule and not a knob.

## Before writing

1. Name the gap Cursor does not already ship. If Plan, Task, Bugbot, `/sdd`, or `/create-skill` covers it, stop.
2. Ask: does this raise the probability the first attempt is the accepted attempt, net of its context tax?
3. Does this work unchanged on a project we have never seen? If it needs a language, framework, database, or vendor, stop.
4. Is this already battle-tested upstream? If yes and it passes 001/002/003, adopt with attribution. Do not extract. Do not rewrite.
5. Put it in `.cursor/skills/<name>/SKILL.md`.

## Pointer

The `description` is the pointer. Third person. What it does and when to use it. Front-load the trigger word. One trigger per distinct case.

- User-only workflow: set `disable-model-invocation: true`.
- Agent should pull it when the task matches: omit that field.

## Body

- Steps with a checkable done-line each.
- In-file only what every run needs. Link one level down for reference.
- Prompt the positive. Do not steer by naming the forbidden behaviour.
- Keep SKILL.md under 500 lines. Prefer under 80.
- No always-on tax. No router that picks other skills for every chat.

## Done

The skill is done when a stranger can `@` or `/` it and the agent takes the same process every run, without a clarifying round about the skill itself.
