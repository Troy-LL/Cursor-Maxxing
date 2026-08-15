# Promote

_Scratch_ is working memory. The _owner_ is product truth. Promote is distill, then delete — not rename.

## Steps

1. **Seat.** Write `scratch/<topic>-YYYYMMDD.md` (gitignored) or the PR body. Title it as hypothesis. Ensure `scratch/` is in `.gitignore`. Done when the journal exists and `AGENTS.md` does not bullet it.
2. **Think there.** Options, dissent, “we might.” Architecture stays what is true _now_. Done when the durable owner has no `Proposed:` line.
3. **Dispose.**
   - **Accepted:** distill each fact into its owner — Read [occasion.md](occasion.md) for which file. One ADR if violating the choice would look right. Then delete the scratch file.
   - **Rejected or expired:** delete.
   - **Merge of the spike/PR:** delete whatever is still scratch.

Done when scratch is gone (or archived off the map), the owner states current topology, and no spec/plan/tasks tree remains as a second spec.

OpenSpec archive-into-`specs/` is a twin, not promote. A model card belongs next to the weights, not in product `docs/`.
