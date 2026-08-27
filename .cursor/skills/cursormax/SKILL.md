---
name: cursormax
description: >-
  Orients to the Cursor Maxxing pack and runs a job that arrives after
  /cursormax — including messy, meta, or vague prompts. Use when the user
  says cursormax, /cursormax, Cursor Max, asks what this pack ships, or
  asks what to type next. Use when doing /sdd or /sdd-eng with this pack
  installed so product docs stay on the map. Do not use for a one-line
  edit, rename, or format pass that never invoked this pack.
---

# Cursor Maxxing

This pack is a small Cursor-native kit. It is not a Claude Code pack and not a pstack / poteto-mode orchestra.

## Load

1. If `docs/decisions/001-native-first.md` exists in the workspace, read `AGENTS.md`, then at most two owners. Cite paths. Do not paste.
2. Otherwise read `reference.md` beside this skill. That is the portable constitution and catalog.
3. If the host has `AGENTS.md`, still load it as the project map (at most two owners). Do not treat this pack as a second map.

Do not dump those files into the reply. Follow them.

## Entry

Most people type `/cursormax` (or "Cursor Max") and paste a job — often a meta-prompt, a wish list, or noise. That paste **is** the job. Do not ask "what is the job?" when they already gave one. Do not dump the catalog.

| What they sent | Do this |
|----------------|---------|
| Exactly `off` | Already handled in the command. Do not Intake. |
| Exactly `on` | Already handled in the command. Do not Intake. |
| Slash only, no job | Orient in one short line. Report soft-off if `scratch/cursormax-off` exists. Ask for the job. Stop. |
| Slash + any job text | Run **Intake**, then **Offer**, then work or wait. Do not treat leftover `on`/`off` inside a sentence as the knob. |

### Intake

From the paste, keep the real ask. Drop role-play, "act as", persona stacks, tool inventories, and filler. Restate the job in one sentence before you branch. If you cannot name a checkable done-line, intent is not locked — go to `/grill` (or offer Plan once). Do not invent scope they did not state.

Then apply the priors this pack already ships: `yagni-bias` is on; for a feature or fix use `tdd` (red before theory); for a claim that might break neighbors use `@blast-radius` (prove by running). End a multi-file change with `verify` when the job is "done."

### Offer

Name the pack slot and the Cursor native for this job. First matching row wins, cheaper first. If they already named the native, skip the offer and do that. Otherwise offer the matching fork once. Wait. Do not pick. Do not re-offer every turn.

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

This is an offer, not a mode. Do not wrap those natives. Do not spawn a named-agent roster. Do not re-read a router skill for every turn.

When they pick Task: name the `subagent_type` from `reference.md` Task matrix. `inherit` the model unless they named one. If they named a slug Task does not list, say so. Write the `prompt` from the Task prompt contract. Do not invent a named agent.

## Slots

| Kind | Use |
|------|-----|
| Skill | Workflow. Host `.cursor/skills/` for new ones; this pack's skills arrive via the plugin |
| Command | Knob. `/voice`, `/keep`, `/cursormax on` \| `off` |
| Rule | Constraint. `@yagni`, `tdd`, `@blast-radius`. `yagni-bias` and `cursormax-bias` are always-on. |

A new add must name a gap Cursor does not ship, work on a project we have never seen, and beat a rewrite if a battle-tested upstream already exists. No router. No second marketplace. No stack skill. `/sdd` and `/sdd-eng` are adopted from troysdd — edit upstream, then re-adopt.

## When the job is SDD

- Creating or distilling product docs → `/sdd`
- Implementing a change against an existing owner → `/sdd-eng`
- Aligning intent first → `/grill`. `/grill docs` then `/sdd`
- Authoring a skill → `/create-skill` plus `write-skill`

Park thinking in `scratch/`. Do not map it. Do not commit it.

## Done

- Slash only: oriented, waiting on a job, no catalog. Soft-off reported if the file exists.
- Exactly `on` / `off`: knob already applied in the command. Stop.
- Slash + job: one-sentence restatement, fork offered once (or skipped), then working or grilling — without restating the README.
