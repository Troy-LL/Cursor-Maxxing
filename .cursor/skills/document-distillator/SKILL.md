---
name: document-distillator
description: >-
  Audits a user-provided monolithic spec (outside bootstrap scaffold), maps content
  into docs/SPEC.md and other docs/*.md shells, removes unused scaffold files, and
  deletes the source spec. Use with /bootstrap, document distillator, auditor, or
  when distilling an ideation doc into project docs.
---

# Document Distillator (Auditor)

Turn **one external spec** (ideation dump, PRD, notion export, etc.) into the minimal `docs/` set the project actually needs. Inverse of bloat: keep only shells with real extracted content.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| **Source spec path** | Yes | Absolute or repo-relative. May live **anywhere** (Desktop, `notes/`, repo root) — not created by bootstrap |
| **`docs/` tree** | Yes | From `/bootstrap` or equivalent |
| **User plan hint** | No | e.g. "API-only backend", "keep DEPLOYMENT" — overrides inference |

If the path is missing, unreadable, or empty: **stop** and ask once. Do not invent a spec.

## Phase 1 — Read and audit (no writes)

1. Read the **entire** source spec.
2. Inventory existing `docs/*.md` (bootstrap shells).
3. Score each scaffold file **keep** vs **drop**:

| Target doc | Keep when spec contains (non-exhaustive) |
|------------|------------------------------------------|
| `SPEC.md` | Requirements, scope, goals, user stories, acceptance criteria, constraints — **default keep** if anything is distillable |
| `DESIGN.md` | UI/UX, wireframes, visual system, flows, mockups, branding |
| `ARCHITECTURE.md` | Components, modules, stack, data model, diagrams, integration boundaries |
| `API.md` | REST/GraphQL/RPC, routes, contracts, payloads, auth between services |
| `TESTING.md` | Test strategy, QA, coverage targets, e2e/unit plans |
| `DEPLOYMENT.md` | Hosting, CI/CD, infra, envs, release, observability ops |
| `DEVELOPMENT.md` | **Always keep** — fixed bootstrap template (workflow, etiquette, commands); never DELETE unless user asks |

**Rules**

- **Keep** only docs that will receive **substantive** extracted content (not placeholder headers).
- If two targets overlap heavily, **merge** into the higher-signal file (e.g. API details → `API.md`, not duplicated in `SPEC.md`).
- Respect explicit user plan hint: force-keep or force-drop named files.
- Minimum after distillation: **`docs/SPEC.md`** with distilled product truth unless user forbids.

4. Produce an audit table (show user before destructive steps):

```markdown
## Distillation plan
| Doc | Action | Rationale (1 line) |
|-----|--------|-------------------|
| SPEC.md | POPULATE | … |
| DESIGN.md | DELETE | no UI content |
| … | … | … |

**Source:** `<path>` → DELETE after success
```

## Phase 2 — Wait for approval

Stop unless the user already said **`proceed`**, **`Y`**, or included the spec path in the same message as **`/bootstrap`** with no objection to deletion.

Offer:

```
Y — Populate kept docs, delete unused shells + source spec
K — Populate kept docs, keep source spec (no source delete)
N — Cancel (scaffold unchanged except any prior bootstrap)
```

## Phase 3 — Distill (writes)

For each **POPULATE** doc:

1. Write **concise, structured** markdown — headings, bullets, tables where helpful.
2. **Extract and reorganize** from the source; do not pad with generic boilerplate.
3. Preserve concrete facts: names, versions, endpoints, constraints, dates.
4. Cross-link sibling docs when useful (`See [ARCHITECTURE.md](ARCHITECTURE.md)`).

**Do not** copy the entire source verbatim into every file.

## Phase 4 — Prune

1. **Delete** every scaffold file marked **DELETE** (empty or unused).
2. Rewrite `docs/README.md` as a short index: **only files that remain**, one line each — always include `DEVELOPMENT.md` if it exists.
3. **Delete the source spec file** if user chose **Y** (not **K**).
4. Do not delete `docs/` itself if at least one file remains.

## Phase 5 — Report

```markdown
## Distillation complete
- Populated: …
- Removed shells: …
- Source spec: deleted | kept at …
- Next: @docs/SPEC.md (and siblings) when prompting; /clean before GitHub if needed
```

## Quality bar

- **Auditor mindset** — every kept file must earn its place for agent `@` reference.
- **No slop** — no "TBD", "TODO: fill in", or lorem ipsum.
- **No overwrite** of non-empty `docs/` files unless user explicitly asked to replace.

## Pairing

| Command | Role |
|---------|------|
| `/bootstrap` | Creates empty `docs/` shells, then runs this skill |
| `/clean` | Strips empty scaffold before publish — run after local work |
