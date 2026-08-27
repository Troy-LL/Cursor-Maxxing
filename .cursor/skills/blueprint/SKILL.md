---
name: blueprint
description: >-
  Blueprints a job before it starts: triages complexity and interviews
  language for greenfield. Use when starting a new project or a whole-job
  kickoff. Do not use mid-task or for one-line edits.
---

# Blueprint

Set the plan for a whole job before coding. Per-call routing stays with Auto.

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

## 4. Model plan (skip unless asked)

If they did not ask about models, cost, tokens, or the picker: skip. Do not name vendors. Otherwise Read [model-plan.md](model-plan.md) and follow it.

## 5. Execution fork

Offer once: run inline in this chat, or dispatch via Task (`/create-subagent`). Done when: the user picked a lane or declined.

## Handoff

Write the blueprint block (tier, language rationale, fork; model plan only if section 4 ran) to `scratch/`. Then offer one matching next step and wait: `/grill` if intent opened up mid-planning, `tdd` for feature work, `@blast-radius` for wide claims, `/verify` at the end of a multi-file change.
