# 006: Always-on is a kernel, not a slot map

Status: Accepted

## Context

A frozen if-then table in `unfurnished-bias` (kickoff → blueprint, no done-line → grill, file on disk → sdd-eng…) is a generic static harness. Research on dynamic composition says that shape loses: static workflows stay generic because they must cover every edge case ([A harness for every task](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)); stuffing every tool in context loses to search-then-load; programmatic tool use beats rigid JSON calling on BFCL v4 ([The Bitter Lesson of Tool Calling](https://arxiv.org/html/2608.06370)). Cloning Claude Code’s per-task JavaScript workflow runtime, a router, or extra MCP would still violate [001](001-native-first.md). Cursor already ships Task, `/create-subagent`, and dynamic tool discovery. Leaner scaffolds can beat heavier ones; dynamic does not mean more furniture.

## Decision

We will keep always-on Unfurnished as a **kernel of constraints** (natives, one slot, no extra probes, soft-off, yield to an attached pack, do not map scratch). Which skill runs is **per-task**, from that skill’s description. We will not ship a Claude-style workflow runtime, a router, or extra MCP. Fan-out and adversarial check go to Task (`bugbot`, `security-review`, `best-of-n-runner`) or `/create-subagent`.

## Consequences

`unfurnished-bias` drops the slot table. Skill descriptions keep the pull triggers. README names this decision. The map bullets this file when a static slot map, workflow clone, or tool-search MCP looks useful.
