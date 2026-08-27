---
name: blueprint
description: >-
  Blueprints a job before it starts: triages complexity, interviews language
  for greenfield, and sets a model plan. Use when starting a new project, a
  whole-job kickoff, or they ask how to spend the model budget. Do not use
  mid-task or for one-line edits.
---

# Blueprint

Set the deliberate plan for a whole job before spending tokens. Cursor's Auto routes each call; this decides the tier up front so per-call routing has a target.

## 1. Triage

Scan the repo first. Classify the job into one tier; ask only what scanning cannot answer.

| Tier | Shape |
|------|-------|
| T0 | One file, reversible, obvious done-line (small fix, rename, format pass) |
| T1 | Multi-file but scoped; tests pin behavior; conventions are clear |
| T2 | Cross-module change, wide blast radius, perf/security stakes |
| T3 | Ambiguous intent or greenfield — requirements need distilling before code |

Done when: the tier is named with one sentence of evidence.

## 2. Intent gate

T3 with unlocked intent → stop here and offer `/grill` once. Interview for language only after intent is locked (by `/grill`, Plan mode, or an already-clear brief).

## 3. Language (greenfield only)

If the repo already has an established language, confirm it in one line and move on. Otherwise interview:

- What is this project for — ship fast, learn something, long-lived, or the joy of it?
- Runtime constraints — startup, memory, distribution target?
- Ecosystem must-haves?
- Which languages do you know today, or want to learn?

State the pick with its rationale in three sentences or fewer, including at least one cost you accept. Done when: the language is named with reasoning, or the existing language is confirmed.

## 4. Model plan

Cursor prices two pools: an included-usage pool of its own models and an API-rate pool for frontier models — check the current model picker for exact names and rates, they change often. Map the tier to cost classes:

| Tier | Plan |
|------|------|
| T0 | Cheapest included-usage class, inline chat. No ceremony. |
| T1 | Included-usage standard effort; a Task subagent only when parallel attempts pay. |
| T2 | High-effort included-usage flagship or mid-tier API-rate class; Task subagents for isolated modules. |
| T3 | One top-tier architecture pass once intent is locked; mechanical edits drop back down-tier afterward. |

When uncertain, start one tier below your guess and escalate after two failed attempts rather than pre-paying frontier rates. Name where each phase runs (model picker vs Auto). Done when: every planned phase names its model source.

## 5. Execution fork

Offer once: run inline in this chat, or dispatch via Task (`/create-subagent`). Done when: the user picked a lane or declined.

## Handoff

Write the blueprint block (tier, language rationale, model plan, fork) to `scratch/`. Then offer one matching next step and wait: `/grill` if intent opened up mid-planning, `tdd` for feature work, `@blast-radius` for wide claims, `/verify` at the end of a multi-file change.
