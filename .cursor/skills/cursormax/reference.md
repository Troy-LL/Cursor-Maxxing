# Cursor Maxxing pack

Portable constitution. Use this when the guidebook repo files are not in the workspace (plugin install). If `docs/decisions/001-native-first.md` exists here, prefer those owners over this file.

## Constitution

- Gap or out. Do not add graph, session, memory, or auto-routing tools. Cursor already searches, remembers, routes, checkpoints, and compact.
- First attempt accepted, net of tax. Expertise is on-demand. `AGENTS.md` (the host repo) stays a map: read it, then at most two owners. Do not paste.
- Workflow, not stack. A piece must work unchanged on a project we have never seen. Adopt a battle-tested upstream with attribution; do not rewrite it.
- A new add must name a gap Cursor does not ship.

## Catalog

| Kind | What |
|------|------|
| `/cursormax` | Orient to this pack and offer the Cursor native for this job |
| `/grill` | Frontier interview. `/grill docs` then `/sdd` |
| `/deepen` | List deepening candidates, wait, then grill the pick |
| `thermonuclear` | In-session adversarial review & loop auditor |
| `verify` | In-turn Definition-of-Done verification gate |
| `pre-flight` | Pre-launch build, secret & deployment audit |
| `evals` | Scaffolds hybrid evals and distills incident traces |
| `write-skill` | Author a skill. Do not wrap `/create-skill` |
| `after-compact` | Rehydrate from `scratch/keep-alive` if present |
| `/voice` | `plain` \| `ste` \| `off` |
| `/keep` | Write or delete `scratch/keep-alive` |
| `yagni-bias` | Always-on, ~40 words |
| `@yagni` | 7-rung ladder |
| `tdd` | Red-green. Skip only if you say why |
| `@blast-radius` | Said → cited → walked → ran |

Product docs: `/sdd`. Implementation: `/sdd-eng`. Those live in the troysdd plugin. Do not copy them into this pack.

## Cursor surface

Type the native. Do not wrap it.

| Type this | When |
|-----------|------|
| Plan / Ask / Debug | Design gate, lookup, or red-repro. Agent is the default loop. |
| Task, `/create-subagent` | Fresh context, isolated implementer or reviewer |
| `/best-of-n`, `/worktree` | Parallel attempts; pick a winner |
| `/loop`, Cloud Agents, Automations | Unattended or recurring |
| Bugbot, Security Review | Review a diff out of this chat |
| `/rewind`, checkpoints | Undo an agent turn |
| `/summarize` | Compact the window |
| Browser, `/canvas`, Design Mode | Click the app or a mock |
| `/babysit` | Watch a PR |
| `/create-skill`, `/create-rule`, `/commands` | Author a slot. Then `write-skill` if it is a workflow. |
| `/create-hook`, `hooks.json` | Hard stop, not a rule |
| Explore, Grep, Glob, Read | Find code. No graph plugin. |

`/cursormax` offers the one or two rows that match. It does not pick. It does not stay on.

## Task matrix

Spawn with Task. Pick the type. Do not invent a named agent. Do not wrap Bugbot or Security Review in a skill.

| Job | Type | Model |
|-----|------|-------|
| Map a tree, find files | `explore` | inherit. Fast only if they asked for cheap fan-out. |
| One command, git, install | `shell` | inherit |
| "In Cursor, how do I…?" | `cursor-guide` | inherit |
| One failing PR check | `ci-investigator` | inherit |
| Bug review of a diff | `bugbot` | inherit |
| Security review of a diff | `security-review` | inherit |
| Isolated parallel attempts | `best-of-n-runner` | inherit |
| Multi-step research or implement | `generalPurpose` | inherit |

`inherit` is Auto: same model as this chat. Use another slug only when the user named it or asked for a class:

- Fast fan-out: `composer-2.5-fast`, `gemini-3.7-flash-high`, `cursor-grok-4.6-high-fast`
- Deep: inherit, or the slug they named
- API / open-source / other Gemini: only if that slug is in the Task list this session. If it is not, say unavailable. Do not substitute.

Slugs rot. Types do not. Read the Task tool list this session before passing `model`.

## Task prompt

The type is not enough. Write the `prompt` before spawn. Do not paste a playbook. Do not tell them to read a router skill first.

Every spawn, in this order:

1. **Job** — one sentence. The user's actual job, not a template. What they return, not how they feel.
2. **Read** — paths or owners. Cite. Do not paste the files.
3. **Done** — one checkable line.
4. **Return** — the shape (table, paths, verdict). No transcript dump.
5. **Stop** — do not spawn children. Do not commit unless the job says so.

Type extras:

| Type | Extra in the prompt |
|------|---------------------|
| `explore` | Find. Do not edit. Thoroughness: quick / medium / very thorough. |
| `shell` | Commands only. Report exit codes. |
| `cursor-guide` | Product how-to. No repo edits. |
| `ci-investigator` | One failing check. Root cause, not a fix tour. |
| `bugbot` / `security-review` | Use those Task types. Do not rewrite their rubric. |
| `best-of-n-runner` | Same job, isolated tree. |
| `generalPurpose` | If they implement: failing test first when `tdd` is on. If they only survey: say so. |

A blank "look at this repo" prompt is a miss. Improve it, then spawn.

## Leave out

If Cursor ships it, do not wrap it: graph/codegraph, session or memory plugins, auto-routers, hook frameworks, checkpoint wrappers, cost CLIs, compact packs, output-style plugins, statusline themes, permission MCP, worktree managers, review-agent packs, Ralph loops, a second skill marketplace, rule or slash-command authoring playbooks, Browser/Playwright MCP, canvas taste packs, Plan wrappers, `/babysit` loops.

If it assumes a stack, leave it out: framework guides, service integrations, language-specific runners. If a battle-tested upstream already passes, adopt it; do not rewrite it.
