# Rule templates

Copy a block, replace placeholders, delete unused sections.

---

## Always apply — repo standards

```markdown
---
description: Core coding and change discipline for this repository
alwaysApply: true
---

# Repository standards

- Minimize diff scope; do not refactor unrelated code in the same change.
- Match existing naming, imports, and patterns in touched files.
- Prefer extending existing helpers over new abstractions.
- Comments only for non-obvious business logic.
- Do not commit secrets, `.env`, or credential files.
```

---

## TypeScript / JavaScript

```markdown
---
description: TypeScript conventions for this project
globs: **/*.{ts,tsx}
alwaysApply: false
---

# TypeScript

## Error handling

\`\`\`typescript
// ❌ BAD
try { await fetchData(); } catch (e) {}

// ✅ GOOD
try {
  await fetchData();
} catch (e) {
  logger.error('fetch failed', { error: e });
  throw new DataFetchError('Unable to retrieve data', { cause: e });
}
\`\`\`

## Types

- Prefer explicit return types on exported functions.
- Avoid `any`; use `unknown` + narrowing at boundaries.
```

---

## React / UI

```markdown
---
description: React component and hook patterns
globs: **/*.{tsx,jsx}
alwaysApply: false
---

# React

- Functional components only; no class components.
- Colocate component-specific hooks in the same file or `use*.ts` next to the component.
- Props interfaces named `{ComponentName}Props`.
- Avoid prop drilling past two levels — use context or composition.
```

---

## Backend / API path-scoped

```markdown
---
description: API route and service conventions
globs: backend/**/*.{py,ts,go}
alwaysApply: false
---

# Backend API

- Validate input at the boundary; return typed errors.
- Log request id on every handler entry.
- Do not expose stack traces in production responses.
```

---

## Testing

```markdown
---
description: Test style and coverage expectations
globs: **/*.{test,spec}.{ts,tsx,py,js}
alwaysApply: false
---

# Tests

- Test behavior, not implementation details.
- One logical assertion theme per test; descriptive names (`should reject expired token`).
- No snapshot tests for large DOM trees unless reviewing UI contracts.
```

---

## Negative constraints

```markdown
---
description: Forbidden patterns in this codebase
globs: **/*
alwaysApply: false
---

# Do not

- Import from deprecated `legacy/` package paths.
- Use `eval`, dynamic `Function`, or inline script in templates.
- Add new dependencies without matching the package manager lockfile workflow.
```

---

## Monorepo package scoped

```markdown
---
description: Conventions for the web app package only
globs: apps/web/**/*
alwaysApply: false
---

# Web app (apps/web)

- Use the shared `@repo/ui` components; do not duplicate button/modal markup.
- Environment variables must go through `lib/env.ts` validation.
```
