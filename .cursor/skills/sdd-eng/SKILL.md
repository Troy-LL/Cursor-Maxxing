---
name: sdd-eng
description: >-
  Implements a behavior change in a product that already has (or is getting) an
  SDD map: edit the owning durable file and the code it points at, load only
  what this turn needs, and do not mint a per-feature spec/plan/tasks tree. Use
  when the user is coding a feature, fix, or refactor against an existing
  README, architecture, design, eval, or ADR. Do not use when creating or
  omitting product docs, distilling a PRD or idea dump, promoting scratch or a
  Proposed line, scaffolding Spec Kit / OpenSpec / Kiro, dual-writing
  CLAUDE.md, writing a markdown twin of OpenAPI or schema, or deciding whether
  a new durable file should exist.
disable-model-invocation: true
---

A change. `/sdd-eng`. Load stays on the product `AGENTS.md`. Authoring is `/sdd`.

Import this file into a product. Do not copy the guidebook.

## Steps

1. **Name the change.** One falsifiable sentence. Pause. Put that intent in the file you will edit. Do not start `spec.md` / `plan.md` / `tasks.md`.
2. **Owner or handoff.** Owner missing, or the user pointed at a dump / RFC / spike / `Proposed:` / spec tree → stop; that is `/sdd`. Otherwise name the existing path from the product `AGENTS.md` bullets.
3. **Load.** Read the product `AGENTS.md`. Open only the owner this turn needs. If loading more than one extra, pin README → architecture → design → eval. An ADR counts as one extra. Ceiling: this map + at most 2, or +3 if this turn needs `eval.md`. Skip unused. Cite paths. Do not paste. Do not open `docs/files.md` in a product.
4. **Edit.** Change that owner and the code, schema, or tests it points at. No markdown twin. Thinking goes in `scratch/` (or the PR body). Do not map scratch.
5. **Re-occasion.** If the edit made a new durable job true (a screen, topology left compose, a decision that would look right if violated) → `/sdd` for that file only. Stop.
6. **Verify.** Run the check the product `AGENTS.md` names. Do not skip.
