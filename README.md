# Unfurnished

Cursor-native workflow pack. Don't attach Claude furniture to Cursor. The room looks empty. That is the point. Was Cursor Maxxing.

This is not a token-golf optimizer. It points Agent at Plan, Ask, Debug, Task, Grep, Browser, and compact — the Cursor plan you already pay for — instead of cloning graph, memory, or router furniture. Skills fill gaps the IDE does not ship. Install it and talk; slash names are optional. Other plugins may run alongside. Not a Claude Code pack.

We landed t1-nook in-session (Red green, `docs/design.md` kept Keyboard and Retry, fixture restored red). That is one transcript, scored as user turns and extra tool calls — not a cost class, not n ≥ 3, not a 004 promote. Re-import the plugin or live chats still load the old `cursormax` cache.

A few skills, a few knobs, a few short priors. Nothing that wraps something Cursor already ships. Stack-agnostic: same pack on a CLI, a SaaS, or a pipeline.

## Start here

1. Customize → Plugins → Import marketplace, paste GitHub `Troy-LL/Cursor-Maxxing`. Each push to this repo updates the install.
2. Chat. The pack is on. Docs, features, kickoff, verify, and ship can pull themselves. A job with no checkable done-line gets an interview. You do not need `/unfurnished` first.
3. **`/unfurnished off`** mutes pack slots in this workspace (`scratch/unfurnished-off`; do not commit). **`/unfurnished on`** turns them back on. Customize → disable plugin is the hard off. Other plugins may run alongside; use soft-off only when you want Unfurnished quiet.

Open this repo only to edit the pack. If you already imported the plugin, do not also open this repo as the project — every skill loads twice.

Do not `npx` a Claude pack to get these files. Do not copy `.cursor/` by hand unless you cannot install plugins.

Catalog: [`.cursor-plugin/marketplace.json`](.cursor-plugin/marketplace.json) (what Customize import reads). Plugin: [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json).

### `/unfurnished` if you want it

| You type | What happens |
|----------|--------------|
| `/unfurnished` alone | Orients. Reports if this workspace is soft-off. Fine. No job required. |
| `/unfurnished` plus a job | Takes the paste (messy and meta prompts are fine), strips fluff, names the Cursor native, then works or asks one fork. |
| `/unfurnished off` / `on` | Workspace pack knob. Default is on (no file). Soft-off only — plugin skills may still list. |

## What fires without you typing it

The test: could the agent usefully reach for this on its own? If yes, it is model-invoked. You can still type the `/` if you want that session by name.

| Skill | When it should pull |
|-------|---------------------|
| `sdd` | Product docs: README, AGENTS.md, architecture, design, eval, one ADR |
| `sdd-eng` | A feature, fix, or refactor against that map |
| `grill` | No checkable done-line, align / stress-test a plan. `/grill docs` then `sdd` |
| `blueprint` | New project or whole-job kickoff. Not mid-task. No model picking unless they asked |
| `verify` | Multi-file work about to be called done |
| `thermonuclear` | Adversarial in-session review |
| `pre-flight` | About to ship |
| `ticket` | Feature/fix with no path or no named failing test. Local scratch pointer, not GitHub |
| `evals` | Pipelines, traces into fixtures, cost class for this repo. Do not pin a vendor model |
| `write-skill` | Authoring a skill |
| `after-compact` | Chat was compacted. Opt out with `/keep off` |
| `unfurnished` | They asked what this pack is, or pasted a job after `/unfurnished` |

`tdd` is the same idea as a prior: feature or fix, not a throwaway script.

## What only you start

These must not run unprompted.

| Type this | What it does |
|-----------|--------------|
| `/deepen` | List deepening candidates, wait, grill the pick |
| `/voice` | `plain` \| `ste` \| `off` |
| `/keep` | Opt out of after-compact (`/keep off`). Default is on |
| `/unfurnished off` / `on` | Mute or restore pack slots in this workspace |

Product docs are **`sdd`**. Implementation is **`sdd-eng`**. Both ship in this pack, adopted from [Troy-LL/troysdd](https://github.com/Troy-LL/troysdd) (see `.cursor/skills/sdd/UPSTREAM.md`). You do not need a second plugin for them. If you already installed the troysdd plugin, turn one of them off so `/sdd` is not doubled.

Priors in `.cursor/rules/`: `yagni-bias` (~40 words) and `unfurnished-bias` (natives + one slot). Both always on. `@yagni`, `tdd`, and `@blast-radius` attach when the task matches, or when you `@` them.

## Why it looks like this

Three decisions do most of the work.

- **Native first.** Claude Code packs add graph indexes, memory, session files, routers, and overnight loops because that host needs them. Cursor already searches, remembers, routes, checkpoints, and compacts. Codegraph went out for that reason. A new add has to name a gap the IDE does not cover. → [001](docs/decisions/001-native-first.md)
- **Few first shots, not token golf.** Efficiency here means the first few attempts are accepted, out of the box, on whatever model the host picked. Not one-shot perfection. Cursor often does not show tokens — we count shorter sessions and fewer extra tool calls. → [002](docs/decisions/002-first-shot-efficiency.md)
- **Workflow, not stack.** We do not know what you are building and do not need to. Everything works the same on a Rust CLI, a Next.js SaaS, or a data pipeline. Stack guides and framework integrations stay out. → [003](docs/decisions/003-workflow-not-stack.md)

<details>
<summary><strong>What we deliberately leave out</strong> — if Cursor ships it, we do not wrap it</summary>

If it assumes your stack, it belongs in your project rules instead.

| Leave out | Cursor already ships / Where it belongs |
|-----------|-----------------------------------------|
| Graph indexes, codegraph, extra grep | Instant Grep, embeddings, Explore |
| Session or memory plugins | Chat resume, rules, Automation Memories |
| Auto-routers / named-agent orchestrators | Task, `/create-subagent`, Plan/Ask/Debug, best-of-n |
| Hook frameworks, hook observability dashboards | `hooks.json`, `/create-hook` |
| Checkpoint / rewind wrappers | Agent checkpoints, `/rewind` |
| ccusage-style cost CLIs | Usage dashboard, statusline token % |
| Caveman / rtk compact packs | Product compact, `/summarize` |
| Output-style plugins | User Rules, Agent/Plan/Ask/Debug modes |
| Statusline theme packs | `cli-config.json` `statusLine` |
| Permission MCP / safety-net plugins | Auto-review, `permissions.json`, sandbox |
| Worktree desktop managers | `/worktree`, `/best-of-n`, `git worktree` |
| Review-agent packs | Bugbot, Security Review |
| Ralph overnight loops | `/loop`, Cloud Agents, Automations |
| A second skill marketplace | Plugins, [skills.sh](https://skills.sh/), cursor.directory |
| Rule-authoring playbooks | `/create-rule`, Customize → Rules |
| Slash-command authoring playbooks | `/commands`, Customize → Commands |
| Browser / Playwright verify MCP | Native Browser |
| Canvas / design-to-code taste packs | `/canvas`, Design Mode |
| Plan / `/autoplan` wrappers | Plan mode |
| PR babysit loops | `/babysit` |
| Stack skills, framework guides, service integrations | App-specific `.cursor/rules/`, `cursor-directory` |
| Rewrites of battle-tested community skills | Adopt verbatim with upstream attribution ([003](docs/decisions/003-workflow-not-stack.md)); `/sdd` is the troysdd adopt |

</details>

<details>
<summary><strong>What an MDC is</strong> — and when to write one</summary>

An `.mdc` in `.cursor/rules/` is a **constraint** injected into Agent context. It is not a skill, not a slash command, not `AGENTS.md`, and not a User Rule.

Cursor's [rules docs](https://cursor.com/docs/rules.md) give four attach modes. Pick one. The frontmatter is the mode.

| Mode | Frontmatter | When it loads |
|------|-------------|---------------|
| Always | `alwaysApply: true` | Every chat. Globs and description ignored. Expensive. |
| Files | `alwaysApply: false` plus `globs` | Matching files are in context. Default for stack conventions. |
| Intelligent | `alwaysApply: false` plus `description`, no globs | Agent pulls it when the description matches the task. |
| Manual | `alwaysApply: false`, no globs, no description | Only when you `@rule-name`. |

Official bar: keep them short, one concern, concrete examples or `@` a file instead of pasting it. Add a rule when Agent makes the **same mistake repeatedly**. Do not copy a style guide the linter already owns. Do not document npm and git. Plain `.md` in `.cursor/rules/` is ignored. Use `AGENTS.md` if you want unscoped markdown.

**Write one when**

- The fact is project-specific and Agent will violate it without a prompt
- It belongs on a glob (`**/*.tsx`, `src/api/**`) or on `@` mention
- It is not already in README, `AGENTS.md`, User Rules, or a shipped skill

**Do not write one when**

- `/create-rule` or Customize → Rules is the authoring UI (do not wrap that)
- The text is routing (`AGENTS.md`) or personal voice (User Rules)
- The text is a workflow (skill) or a user-invoked `/` (command)
- The text is a hard stop (`beforeShellExecution` hook). Rules do not block `git reset --hard`
- You want it in every chat and it already lives in README. Point at the file.

This guidebook ships only the priors in `.cursor/rules/`. When an app needs a stack convention, type `/create-rule` or add it in Customize. Reach for an existing one before writing from scratch:

```bash
npx cursor-directory rules add <slug-or-url>
```

Skills: [skills.sh](https://skills.sh/) / `npx skills`. Use `write-skill` when the add is a workflow, not a constraint. Do not install a Claude pack to get a marketplace.

</details>
