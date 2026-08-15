---
name: pre-flight
description: >-
  Universal pre-launch build, secret leak, and deployment readiness audit. Use
  when the user says pre-flight, /pre-flight, deploy check, pre-deploy, ready to ship,
  or is preparing to deploy or release code to production.
---

# Pre-Flight Launch Audit

Universal pre-launch verification pass to ensure zero deployment surprises.

## Checklist

Execute these checks across the project:

1. **Production Build & Compiler**: Run the project's build command via `Shell` (`npm run build`, `cargo build`, `go build`, etc.). Verify `exit_code == 0` with zero compilation errors.
2. **Secret & Credential Scan**: Verify `.gitignore` ignores `.env*` and local credential files. Scan codebase for hardcoded private tokens, API keys, or leaked credentials.
3. **Environment Variable Parity**: Verify all environment variables accessed in source code are documented in `.env.example` or configuration schemas.
4. **Dependency Sync**: Verify all imported packages/modules are declared in project manifests (`package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, etc.).
5. **Anti-Stub Scrubber**: Scan codebase for unhandled `// TODO` stubs, placeholder returns, or fake mock data on critical paths.
6. **Error & Fallback Handling**: Verify top-level error boundaries, 404/fallback routes, or global exception handlers exist.
7. **Test Suite Status**: Run the project's test suite via `Shell` to confirm all tests pass cleanly before shipping.

## Output Format

Emit a concise scorecard:

```
### Pre-Flight Launch Scorecard

| # | Check | Status | Action Required |
|---|-------|--------|-----------------|
| 1 | Production Build | PASS / FAIL / N/A | <fix if fail> |
| 2 | Secret & Env Scan | PASS / FAIL / N/A | <fix if fail> |
| 3 | Dependency Sync | PASS / FAIL / N/A | <fix if fail> |
| 4 | Anti-Stub Check | PASS / FAIL / N/A | <fix if fail> |
| 5 | Test Suite | PASS / FAIL / N/A | <fix if fail> |
```

N/A is not PASS. If a check has no runner, no env, or no suite, write N/A.

## Done

Pre-flight is done when every applicable check is PASS, and every N/A is named. Do not say ship if the only statuses are N/A.
