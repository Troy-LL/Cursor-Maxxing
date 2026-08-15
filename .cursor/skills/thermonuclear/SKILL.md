---
name: thermonuclear
description: >-
  In-session adversarial code review and auditor node for agent loops, graph
  workflows, and deep code audits. Use when the user says thermonuclear, /thermonuclear,
  adversarial review, or needs an in-session auditor node during loop/graph engineering
  without switching modes or spawning expensive external review subagents.
---

# Thermonuclear Review

Adversarial in-session code auditor across invariants, edge cases, security, data loss, and performance.

## Process

Audit modified files or targeted modules across four adversarial angles:

1. **Angle 1 — Invariants & Contracts**:
   - Check null/undefined dereferences, unhandled async promise rejections, and missing error returns.
   - Verify that all state machine transitions and message sequences preserve invariants.

2. **Angle 2 — Edge Cases & Concurrency**:
   - Trace race conditions in async operations, duplicate submissions, and out-of-order events.
   - Check timeout handling, retry backoffs, and recovery from partial failures.

3. **Angle 3 — Security & Data Loss**:
   - Check authorization checks, tenant boundary isolation (`user_id` filters), and injection risks.
   - Verify that no data is permanently deleted or overwritten without recovery paths.
   - Ensure secrets, API keys, and PII are never logged or exposed to client bundles.

4. **Angle 4 — Performance & Cost**:
   - Detect N+1 database queries, unindexed table scans, and unbounded in-memory array operations.
   - Check for un-cached LLM/API calls, missing rate limits, and memory leaks in event listeners.

## Output Format

```
### Thermonuclear Audit Report

- **Critical** (Blocks merge/run): <one-line summary>
  - Line: `path/to/file.ts:42`
  - Exploit / Failure: <what breaks and how>
  - Fix: <exact replacement code>

- **Major** (Degrades reliability/cost): <summary and fix>
- **Minor / Clean**: <noted issues or clean bill>
```

## Done

The audit is done when all Critical and Major findings have explicit, runnable fixes applied or are verified clean.
