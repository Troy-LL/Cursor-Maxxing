---
name: document-distillator
description: >-
  Audits a user-provided monolithic spec (outside bootstrap scaffold), maps content
  onto the allowlist (README.md, AGENTS.md, docs/architecture.md, design.md, eval.md,
  one ADR), removes unused shells, and deletes the source spec. Use with /bootstrap,
  document distillator, auditor, or when distilling an ideation doc into project docs.
---

# Document Distillator (Auditor)

Turn **one external spec** into the allowlisted files the job actually needs. Inverse of bloat. Hard allowlist. Do not invent extra doc types.

## Allowlist

| File | Role |
|------|------|
| `README.md` | Product: what / why / how to run. No `docs/product.md`, no `docs/SPEC.md` |
| `AGENTS.md` | The only map. Thin (ceiling 200 lines, not a target): commands, do-nots, pointers. No architecture pasted in. No `docs/README.md` |
| `docs/architecture.md` | How it works, data flow, how an agent uses the API. Cite the schema path (types / JSON Schema). Do not recap field lists |
| `docs/design.md` | Human look/feel only. Omit if there is no screen |
| `docs/eval.md` | Only if a model is in the loop |
| `docs/decisions/NNN-title.md` | Cite one ADR. Never glob the folder. Superseded-by, not a changelog |

**Not in the map:** `prompts/`, `evals/` (artifacts), dated reports. Schema as code.

**Ladder:** scratch = `README.md` only. Product app = add architecture/design only when those jobs exist. AI system = `docs/eval.md` exists.

## Map stub (write to `AGENTS.md`)

```markdown
# Agent map

Ceiling 200 lines. Pointers only. Do not paste architecture here.

## Load

Per turn: this file + 2 allowlisted files, or + 3 if `docs/eval.md` exists. Cap, not a starter kit. Skip files the job does not need. When loading more than one, order is `README.md` → `docs/architecture.md` → `docs/design.md` → `docs/eval.md`. Cite paths; never paste the spec.

## Allowlist

- `README.md`: product (what / why / how to run)
- `docs/architecture.md`: how it works; cite schema path, no field lists
- `docs/design.md`: look/feel; omit if no screen
- `docs/eval.md`: only if a model is in the loop
- `docs/decisions/NNN-title.md`: cite one ADR; never glob this folder

Not in the map: `prompts/`, `evals/` (artifacts), dated reports. Schema lives in code.

## Do not

- Add `docs/README.md` as a second map
- Create `docs/SPEC.md`, `docs/API.md`, `docs/TESTING.md`, `docs/DEPLOYMENT.md`, or `docs/DEVELOPMENT.md`
- Recap schema fields in markdown
- Glob `docs/decisions/`

## Commands

Project slash commands live in `.cursor/commands/`. Use Cursor `/rules` and `/commands` for local edits.
```

When distillation finishes, keep this stub and only add pointers to files that **exist**. Do not list missing docs as if they were required reading.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| **Source spec path** | Yes | Absolute or repo-relative. May live **anywhere**. Not created by bootstrap |
| **User plan hint** | No | e.g. "no UI", "model in the loop". Overrides inference |

`docs/` may be absent. Do not require bootstrap shells. Create an allowlisted file only when the audit says POPULATE.

If the path is missing, unreadable, or empty: **stop** and ask once. Do not invent a spec.

## Phase 1 — Read and audit (no writes)

1. Read the **entire** source spec.
2. Inventory existing `README.md`, `AGENTS.md`, `docs/**`, and leftover old shells (`SPEC.md`, `API.md`, `TESTING.md`, `DEPLOYMENT.md`, `DEVELOPMENT.md`, `docs/README.md`, uppercase `DESIGN.md` / `ARCHITECTURE.md`).
3. Score each **allowlisted** target **keep** vs **drop**:

| Target | Keep when |
|--------|-----------|
| `README.md` | Product truth (what / why / how to run). **Default keep** if anything is distillable |
| `AGENTS.md` | **Always**. Map with load rule + pointers. Never dump architecture |
| `docs/architecture.md` | A system to describe: data flow, modules, how an agent uses the API. Drop for scratch (README only) |
| `docs/design.md` | Screen / look/feel / branding. Drop if no UI |
| `docs/eval.md` | A model is in the loop. Drop otherwise |
| `docs/decisions/NNN-title.md` | Spec contains one real decision worth an ADR. Do not create a folder of stubs |

**Rules**

- **Keep** only files that will receive **substantive** extracted content (not placeholder headers), except `AGENTS.md` (always the map).
- Default keep is **`README.md`**, not `SPEC.md`.
- API usage belongs in `docs/architecture.md`. Field lists stay in schema code. Do not create `docs/API.md`.
- How to run belongs in `README.md`. Do not create `DEPLOYMENT.md` or `TESTING.md`.
- If two allowlisted targets overlap, merge into the higher-signal file.
- Respect explicit user plan hint: force-keep or force-drop named **allowlisted** files. Do not create files outside the allowlist.
- Empty leftover files on old names (`SPEC.md`, `API.md`, `TESTING.md`, `DEPLOYMENT.md`, `DEVELOPMENT.md`, `docs/README.md`, uppercase `DESIGN.md` / `ARCHITECTURE.md`): **DELETE**. Non-empty old names: skip overwrite, report, ask whether to fold into the allowlist.

4. Produce an audit table (show user before destructive steps):

```markdown
## Distillation plan
| Doc | Action | Rationale (1 line) |
|-----|--------|-------------------|
| README.md | POPULATE | … |
| docs/design.md | SKIP | no UI |
| docs/SPEC.md | DELETE | leftover shell |

**Source:** `<path>` → DELETE after success
```

## Phase 2 — Wait for approval

Stop unless the user already said **`proceed`**, **`Y`**, or included the spec path in the same message as **`/bootstrap`** with no objection to deletion.

Offer:

```
Y — Populate kept files, delete unused shells + source spec
K — Populate kept files, keep source spec (no source delete)
N — Cancel (scaffold unchanged except any prior bootstrap)
```

## Phase 3 — Distill (writes)

For each **POPULATE** file:

1. Write **concise, structured** markdown. Headings, bullets, tables where helpful.
2. **Extract and reorganize** from the source. Do not pad with generic boilerplate.
3. Preserve concrete facts: names, versions, constraints, dates.
4. `docs/architecture.md`: cite the schema path. Do **not** recap field lists.
5. `AGENTS.md`: if missing, empty, or still the Map stub, write/refresh the stub and point only at files that will exist. If a custom non-empty `AGENTS.md` already exists, skip overwrite and report.

**Do not** copy the entire source verbatim into every file.
**Do not** overwrite non-empty allowlisted files unless the user explicitly asked to replace.

## Phase 4 — Prune

1. **Delete** every file marked **DELETE** (empty or unused shells, including leftover old names).
2. **Do not** write `docs/README.md`.
3. **Delete the source spec file** if user chose **Y** (not **K**).
4. If `docs/` is empty after prune, remove the folder.
5. Do not glob or index `docs/decisions/`.

## Phase 5 — Report

```markdown
## Distillation complete
- Populated: …
- Removed shells: …
- Source spec: deleted | kept at …
- Next: @AGENTS.md then the allowlisted files this job needs; /clean before GitHub if needed
```

## Quality bar

- **Auditor mindset.** Every kept file must earn its place for agent `@` reference.
- **No slop.** No "TBD", "TODO: fill in", or lorem ipsum.
- **No overwrite** of non-empty allowlisted files unless the user explicitly asked to replace.
- No second map.

## Pairing

| Command | Role |
|---------|------|
| `/bootstrap` | Writes `AGENTS.md` + slots, then runs this skill. Creates nothing in `docs/` until this audit |
| `/clean` | Strips empty leftover shells and local-only folders before publish |
