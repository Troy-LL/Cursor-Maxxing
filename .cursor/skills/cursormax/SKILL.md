---
name: cursormax
description: >-
  Orients to the Cursor Maxxing pack and the Cursor natives this job should
  use. Use when the user says cursormax, /cursormax, asks what this pack
  ships, or asks what to type next in Cursor. Use when doing /sdd or
  /sdd-eng with this pack installed so product docs stay on the map. Do not
  use for a one-line edit, rename, or format pass.
---

# Cursor Maxxing

This pack is a small Cursor-native kit. It is not a Claude Code encyclopedia.

## Load

1. If `docs/decisions/001-native-first.md` exists in the workspace, read `AGENTS.md`, then at most two owners. Cite paths. Do not paste.
2. Otherwise read `reference.md` beside this skill. That is the portable constitution and catalog.
3. If the host has `AGENTS.md`, still load it as the project map (at most two owners). Do not treat this pack as a second map.

Do not dump those files into the reply. Follow them.

## Offer

Name the pack slot and the Cursor native for this job. Offer the matching fork once. Wait. Do not pick. Do not re-offer every turn.

| Job | This chat | Native to type |
|-----|-----------|----------------|
| Cheap reversible edit | Yes | Stay. No skill. |
| Intent not locked | No | `/grill`, or switch to Plan |
| Multi-file implement | Ask | This chat, or Task (`/create-subagent`) |
| Spawn workers | Ask | Task. Name the type from the matrix. |
| Parallel attempts | No | `/best-of-n` + `/worktree` |
| Need a red repro | No | Debug |
| Overnight / unattended | No | `/loop`, Cloud Agents |
| Review a diff | `thermonuclear` | Bugbot, Security Review |
| What can I type? | — | `reference.md` Cursor surface. Do not paste it. |

This is an offer, not a mode. Do not wrap those natives.

When they pick Task: name the `subagent_type` from `reference.md` Task matrix. `inherit` the model unless they named one. If they named a slug Task does not list, say so. Do not invent a named agent.

## Slots

| Kind | Use |
|------|-----|
| Skill | Workflow. Host `.cursor/skills/` for new ones; this pack's skills arrive via the plugin |
| Command | Knob. `/voice`, `/keep` |
| Rule | Constraint. `@yagni`, `tdd`, `@blast-radius`. `yagni-bias` is the only always-on. |

A new add must name a gap Cursor does not ship, work on a project we have never seen, and beat a rewrite if a battle-tested upstream already exists. No router. No second marketplace. No copy of `/sdd` or `/sdd-eng` into this tree. No stack skill.

## When the job is SDD

- Creating or distilling product docs → `/sdd` (troysdd plugin).
- Implementing a change against an existing owner → `/sdd-eng`.
- Aligning intent first → `/grill`. `/grill docs` then `/sdd`.
- Authoring a skill → `/create-skill` plus `write-skill`.

Park thinking in `scratch/`. Do not map it. Do not commit it.

## Done

The agent is oriented when it has named the pack slot and the Cursor native for this job, offered any matching fork once, and is waiting or working — without restating the README.
