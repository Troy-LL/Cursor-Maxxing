# Map

`AGENTS.md` is routing, not a second spec. Write it only when a product doc exists.

## Inside

- One bullet per file that exists. Front-load the job word. One trigger per branch (see writing-for-agents).
- Load _ceiling_: this file + at most 2 extras, or +3 if this turn needs `eval.md`. Ceiling, not quota. Skip unused.
- Commands and never-dos that differ from defaults.
- Two lines that permit `scratch/` without listing it.

## Hosts

One `AGENTS.md`. `CLAUDE.md` is `@AGENTS.md` plus Claude-only deltas. Gemini: `context.fileName` → `AGENTS.md`, or the same import. Copilot Chat: `.github/copilot-instructions.md` as a stub. Root `copilot-instructions.md` is dead.

An `@import` of architecture is still always-on. Live tools come from the host session.

Product maps omit `files.md`. Nested maps only where commands or never-dos differ. Closest file wins; do not clone the root into every package.
