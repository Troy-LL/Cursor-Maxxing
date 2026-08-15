# Distill

A _dump_ is a jumbled PRD, idea note, or spec paste. Distill extracts product truth into owners. It does not plant a docs tree.

If the path is missing, unreadable, or empty: stop and ask once.

## Steps

1. **Read the dump.** Entire file. Inventory existing `README.md`, `AGENTS.md`, `docs/*`. Done when you can name every job the dump actually states.
2. **Score occasion.** For each row in [occasion.md](occasion.md): keep only if the dump made that job true. Default omit. Endpoint lists stay in OpenAPI/proto/types when code exists — not `docs/api.md`. Still-maybe residue is [promote.md](promote.md), not architecture. Done when every keep/omit has a one-line reason.
3. **Plan, then write.** Show the plan (create / edit / omit / dump fate). Then write owners using [owners.md](owners.md) and [map.md](map.md). Do not overwrite non-empty files; merge into the owner. Done when each kept job has one owner and the map bullets only files that exist.
4. **Dispose the dump.** Default **delete**. If the user said keep: move to `scratch/dump-<stem>-YYYYMMDD.md` and ensure `scratch/` is gitignored. Never leave the dump on the map. Done when the dump path is gone from product docs and from `AGENTS.md`.

Stop if the dump is only a wish list with no runnable product: write `README.md` only, dispose the dump.
