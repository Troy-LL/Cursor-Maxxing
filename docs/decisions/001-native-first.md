# Native-first: do not clone Cursor builtins

Status: Accepted

## Context

People copy Claude Code maxxing packs into Cursor: graph indexes, extra grep, session files, memory plugins, auto-routers. That looks like more agent power. On Cursor it is duplicate machinery. File search, sessions, memory, and routing already run in the product. Codegraph was the loudest example. It cost tokens and attention for a job Grep, Glob, and Read already do.

## Decision

We will not add graph, session, memory, or auto-routing tools. Cursor Maxxing only fills jobs the IDE does not ship (review workflows, authoring rules, product SDD).

## Consequences

`.cursor/` stays small: on-demand skills, a few knobs, short priors. Agents use built-in search and the session they are in. Someone coming from a Claude pack will still call this empty. That is the point. A new add has to name a gap Cursor does not cover, or it stays out.
