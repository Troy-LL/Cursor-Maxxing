# Occasion

Create the _owner_ of a fact. Absence is correct. A _twin_ (markdown recap of schema, OpenAPI, or topology) is the same job under a new name — edit the owner instead.

Intent stays in the file that changed. Job still many-valued → Read [promote.md](promote.md). Do not fill a durable template to look busy.

## Steps

1. **Name the job.** One sentence: what an agent with _only this file_ would do. Done when that sentence is falsifiable this turn (“there is a screen”, “topology is not in compose”).
2. **Match occasion.** Use the table below. Default omit. Done when every path you would create has a true job, or you create none.
3. **Write the owner.** One fact, one file. Point at schema/types; leave contracts in OpenAPI / proto / SQL. If the file is `AGENTS.md`, Read [map.md](map.md). If the file is a durable doc, Read [owners.md](owners.md) for that heading. Done when the fact lives in one place and the map bullets only files that exist.
4. **Stop.** One owner per fact.

## Occasion (default omit)

| Job | Owner |
| --- | --- |
| Front door, how to run | `README.md` |
| Agent routing, and a product doc exists | `AGENTS.md` |
| Topology not in compose / schema / mains | `docs/architecture.md` |
| There is a screen | `docs/design.md` |
| Model + scored probe | `docs/eval.md` |
| Decision that would look right if violated | one `docs/decisions/NNN-*.md`, mapped |
| Published contract | OpenAPI / proto / types in code |
| Same checklist, sometimes | `SKILL.md` (name + description always; body on match) |
| Package commands differ | nested `AGENTS.md` |
| You ship weights or a dataset | card next to that artifact (Hub README) |

Would an agent with only this file do a **different** job? If not, you are writing a twin.

GitHub health files (`LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`) wait for a host UI, a lawyer, or outsiders. `GOVERNANCE.md` waits for a real decision body. A runbook waits for a paging alert.
