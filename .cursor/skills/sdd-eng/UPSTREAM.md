# Upstream

Adopted verbatim from [Troy-LL/troysdd](https://github.com/Troy-LL/troysdd) (`sdd` plugin).

- Upstream: https://github.com/Troy-LL/troysdd
- Pin: `b8728f34367e6d39c938daf9b9a9644a381e15ca` (2026-08-15)

Do not rewrite the body here. Prefer upstream fixes, then re-adopt. See `docs/decisions/003-workflow-not-stack.md`.

Pack overlay: model-invocation is on so a feature/fix loads this loop without `/sdd-eng`. Re-adopt does not restore `disable-model-invocation`.
Pack overlay: a file on disk is the owner even when the map omitted the bullet. Patch in place; a full-file replace of a living owner fails. If this change names a thing, seat the synonym in that owner; do not mint `docs/glossary.md`. Re-occasion only when that path does not exist yet. Re-adopt does not drop these sentences.
