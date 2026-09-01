# Agent map

Load this file. Then at most two others this turn. Skip unused. Cite paths. Do not paste.

- `README.md` — what Unfurnished is, what we refuse to clone, and when an `.mdc` exists
- `docs/decisions/001-native-first.md` — a graph, memory, session, or router plugin looks useful; read before installing one
- `docs/decisions/002-first-shot-efficiency.md` — a token-golf or always-on lean pack looks useful; read before adding one
- `docs/decisions/003-workflow-not-stack.md` — a stack-specific skill, framework guide, or rewritten upstream looks useful; read before adding one
- `docs/decisions/005-tickets-as-tdd-pointers.md` — a GitHub or Linear ticket skill looks useful; local scratch pointers instead
- `docs/eval.md` — a cost class, model plan, or routing dummy looks useful; read before promoting 004

Pack is on (`unfurnished-bias`) unless `scratch/unfurnished-off` exists. Other plugins may run alongside. `/unfurnished off` / `on` is the workspace knob. Orientation: `/unfurnished`. Marketplace: `.cursor-plugin/marketplace.json` (plugin: `plugin.json`). Workflow skills: `.cursor/skills/` (includes `/sdd` and `/sdd-eng`, adopted from [Troy-LL/troysdd](https://github.com/Troy-LL/troysdd)). Knobs: `.cursor/commands/`. Priors: `.cursor/rules/`. Pack contract check: `python tools/pack-check.py` (add `--strict-install` after a Customize re-import). Do not add MCP that duplicates Grep, Glob, or Read. Do not add a router skill.

Park thinking in `scratch/`. Do not map it, even if they asked. Do not commit it.
