# Cursor Maxxing

Cursor-native setup for people who already live in the IDE. Not a Claude Code pack.

A few on-demand skills, a few knobs, a few short priors. Nothing that wraps something Cursor already ships.

## Start here

1. Install the plugin — Cursor Settings → Plugins → add GitHub `Troy-LL/Cursor-Maxxing`. Or open this repo in Cursor and the project `.cursor/` loads with no marketplace step.
2. Type **`/cursormax`**.
3. Type anything else from the table below when you need a specific workflow.

### `/cursormax` two ways

| You type | What happens |
|----------|--------------|
| `/cursormax` alone | Orients the agent to this pack. Fine. No job required. |
| `/cursormax` plus a job | Takes the paste (messy and meta prompts are fine), strips fluff, names the Cursor native, then works or asks one fork. |

Manifest: [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json). Publish with [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

Do not `npx` a Claude pack to get these files. Do not copy `.cursor/` by hand unless you cannot install plugins.

## What you type

| Type this | What it does |
|-----------|--------------|
| `/cursormax` | Alone: orient. With a paste: intake the job and name the Cursor native |
| `/sdd` | Product docs: README, AGENTS.md, architecture, design, eval, one ADR |
| `/sdd-eng` | Implement a behavior change against that map |
| `/grill` | Frontier interview. `/grill docs` then `/sdd` |
| `/deepen` | List deepening candidates, wait, grill the pick |
| `/thermonuclear` | In-session adversarial review and loop auditor |
| `/verify` | Definition-of-Done gate before the turn ends |
| `/pre-flight` | Build, secret, and deployment audit before you ship |
| `/evals` | Scaffold hybrid evals, distill incident traces |
| `/voice` | `plain` \| `ste` \| `off` |
| `/keep`, `/after-compact` | Park a keep-alive, rehydrate after a compact |

Product docs are **`/sdd`**. Implementation is **`/sdd-eng`**. Both ship in this pack, adopted from [Troy-LL/troysdd](https://github.com/Troy-LL/troysdd) (see `.cursor/skills/sdd/UPSTREAM.md`). You do not need a second plugin for them. If you already installed the troysdd plugin, turn one of them off so `/sdd` is not doubled.

Also on board: `write-skill` (author a skill — model-invoked), and the priors in `.cursor/rules/` — `yagni-bias` is always on at ~40 words, while `@yagni`, `tdd`, and `@blast-radius` are opt-in.

## Why it looks like this

Three decisions do most of the work.

- **Native first.** Claude Code packs add graph indexes, memory, session files, routers, and overnight loops because that host needs them. Cursor already searches, remembers, routes, checkpoints, and compacts. Codegraph went out for that reason. A new add has to name a gap the IDE does not cover. → [001](docs/decisions/001-native-first.md)
- **First-shot correctness, not token golf.** Efficiency here means getting it right on the first attempt. → [002](docs/decisions/002-first-shot-efficiency.md)
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
