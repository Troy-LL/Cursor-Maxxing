---
name: evals
description: >-
  Scaffold deterministic assertions, calibrated LLM-as-a-judge eval suites, or
  distill raw JSON production traces into reproducible test fixtures. Use when
  building or testing non-deterministic AI pipelines, prompts, RAG retrieval, or
  converting incident traces (Langfuse, Arize, Braintrust, Sentry) into pytest or vitest
  regression tests. Do not use for purely deterministic code where standard TDD applies.
---

# Evals

Build eval suites for non-deterministic AI pipelines and distill failure traces into regression tests.

## 1. Scaffolding Hybrid Eval Suites

When testing an LLM pipeline, extraction task, or agent step:

1. **Deterministic Bounds First**:
   - Schema validation (Pydantic / Zod).
   - Tool call presence and parameter type checks.
   - Latency thresholds and token/cost caps.
   - Exact substring / regex negative assertions (e.g. no leaked system prompts or placeholder tokens).

2. **Calibrated LLM-as-a-Judge**:
   - Use binary pass/fail outcomes with explicit rubrics. Avoid 1–5 scales to prevent grade inflation.
   - Require quote evidence extraction: judge must cite exact substrings from input and output before rendering a verdict.
   - Mitigate position bias: swap sample ordering in pairwise comparisons.

3. **Statistical Aggregations**:
   - Define pass@k thresholds, accuracy, or recall targets across a test dataset rather than a single stochastic sample.

## 2. Trace Distillation Mode (Trace-to-Fixture)

When converting a production failure trace (e.g. from Langfuse, Arize, or Sentry) into a test fixture:

1. Extract the raw user input, system prompt version, and tool execution history from the trace payload.
2. Isolate the exact point of failure (schema violation, tool argument hallucination, bad reasoning, ungrounded claim).
3. Generate a minimal, standalone, parameterized test fixture in `pytest` or `vitest` mocking all upstream tool calls up to the failure point.

## Done

The eval is done when the test suite or regression fixture runs in the project's test runner and produces a deterministic pass/fail exit code with structured failure explanations.
