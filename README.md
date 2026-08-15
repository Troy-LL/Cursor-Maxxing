# Cursor Maxxing

Cursor-native setup for people who already live in the IDE. Not a Claude Code pack.

Claude Code "maxxing" repos add graph indexes, memory, session files, routers, hook frameworks, and overnight loops because that host needs them. Cursor already searches the tree, keeps the session, remembers, routes, checkpoints, compact, and runs Task subagents. Those layers are bloat here. Codegraph went out for that reason.

Clone it and the agent is equipped: a few on-demand skills, knobs, and short priors. A new add still has to name a gap the IDE does not cover. See [docs/decisions/001-native-first.md](docs/decisions/001-native-first.md).

We are not a token-golf pack. Efficiency is first-attempt correctness. See [docs/decisions/002-first-shot-efficiency.md](docs/decisions/002-first-shot-efficiency.md).

We do not know what you are building—and do not need to. Cursor Maxxing routes the community's battle-tested workflow skills into one Cursor-native pack that works identically whether you build a Rust CLI, a Next.js SaaS, or a data pipeline. Stack guides and framework integrations stay out. See [docs/decisions/003-workflow-not-stack.md](docs/decisions/003-workflow-not-stack.md).

Product docs: **`/sdd`**. Implementation: **`/sdd-eng`**. Those two skills live in the troysdd plugin. This repo does not copy them.

## What this ships

| Kind | Path | When it loads |
|------|------|----------------|
| Skills | `.cursor/skills/cursormax`, `grill`, `deepen`, `thermonuclear`, `verify`, `pre-flight`, `evals`, `write-skill`, `after-compact` | `/cursormax` orients to the pack and offers the Cursor native for this job (also when `/sdd` runs here). `/grill`, `/deepen` are user-only. `thermonuclear`, `verify`, `pre-flight`, `evals`, `write-skill`, and `after-compact` are on-demand / model-invoked. |
| Commands | `.cursor/commands/` | `/cursormax`, `/voice`, `/keep`, `/after-compact`, `/thermonuclear`, `/verify`, `/pre-flight`, `/evals`, plus stubs for `/grill` and `/deepen` |
| Rules | `.cursor/rules/` | `yagni-bias` always-on (~40 words). `@yagni`, `tdd`, `@blast-radius` are opt-in. |

Import: install the plugin. Manifest: [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json).

- This repo: open it in Cursor. Project `.cursor/` loads without a marketplace step.
- Another repo: Cursor Settings → Plugins → add GitHub `Troy-LL/Cursor-Maxxing`, or add this folder as a local plugin. Then `/cursormax`.
- Publish: [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish) with this repository link.

Do not `npx` a Claude pack to get these files. Do not copy `.cursor/` by hand unless you cannot install plugins.

## Not this

If Cursor ships it, we do not wrap it. If it assumes your stack, it belongs in your project rules.

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
| Rewrites of battle-tested community skills | Adopt verbatim with upstream attribution ([003](docs/decisions/003-workflow-not-stack.md)) |

## What an MDC is

An `.mdc` in `.cursor/rules/` is a **constraint** injected into Agent context. It is not a skill, not a slash command, not `AGENTS.md`, and not a User Rule.

Cursor's [rules docs](https://cursor.com/docs/rules.md) give four attach modes. Pick one. The frontmatter is the mode.

| Mode | Frontmatter | When it loads |
|------|-------------|---------------|
| Always | `alwaysApply: true` | Every chat. Globs and description ignored. Expensive. |
| Files | `alwaysApply: false` plus `globs` | Matching files are in context. Default for stack conventions. |
| Intelligent | `alwaysApply: false` plus `description`, no globs | Agent pulls it when the description matches the task. |
| Manual | `alwaysApply: false`, no globs, no description | Only when you `@rule-name`. |

Official bar: keep them short, one concern, concrete examples or `@` a file instead of pasting it. Add a rule when Agent makes the **same mistake repeatedly**. Do not copy a style guide the linter already owns. Do not document npm and git. Plain `.md` in `.cursor/rules/` is ignored. Use `AGENTS.md` if you want unscoped markdown.

### Write an MDC when

- The fact is project-specific and Agent will violate it without a prompt
- It belongs on a glob (`**/*.tsx`, `src/api/**`) or on `@` mention
- It is not already in README, `AGENTS.md`, User Rules, or a shipped skill

### Do not write an MDC when

- `/create-rule` or Customize → Rules is the authoring UI (do not wrap that)
- The text is routing (`AGENTS.md`) or personal voice (User Rules)
- The text is a workflow (skill) or a user-invoked `/` (command)
- The text is a hard stop (`beforeShellExecution` hook). Rules do not block `git reset --hard`
- You want it in every chat and it already lives in README. Point at the file.

This guidebook ships only the priors in `.cursor/rules/`. When an app needs a stack convention, type `/create-rule` or add it in Customize. Prefer `npx cursor-directory rules add <slug>` before writing from scratch. Use `write-skill` when the add is a workflow, not a constraint.

```bash
npx cursor-directory rules add <slug-or-url>
```

Skills: [skills.sh](https://skills.sh/) / `npx skills`. Do not install a Claude pack to get a marketplace.
