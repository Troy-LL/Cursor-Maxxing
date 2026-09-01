# Upstream

Adopted verbatim from [Troy-LL/troysdd](https://github.com/Troy-LL/troysdd) (`sdd` plugin).

- Upstream: https://github.com/Troy-LL/troysdd
- Pin: `b8728f34367e6d39c938daf9b9a9644a381e15ca` (2026-08-15)

Do not rewrite here. Prefer upstream fixes, then re-adopt. See `docs/decisions/003-workflow-not-stack.md`.

Pack overlay: create only when the path is empty or missing; an existing owner is Read then merged with in-place patches. A full-file replace of a living owner fails. When the user names a thing, seat it in the owner; do not mint `docs/glossary.md`. Do not map a glossary. Even if they asked, do not map scratch. Do not delete a do-not-map line to satisfy a map request. Re-adopt does not drop those sentences. The description also hands an existing-on-disk owner to `/sdd-eng`.
