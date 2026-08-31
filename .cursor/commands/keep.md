# /keep

Opt out of compact rehydrate for this workspace. Default is on.

- `/keep off` — write `scratch/keep-off` (one line: `off`). `after-compact` will not auto-run.
- `/keep on` — delete `scratch/keep-off` (and leftover `scratch/keep-alive`). Default restored.
- `/keep` — report whether opt-out is on.

Do not commit `scratch/keep-off`. Do not write a session diary. The rehydrate body is the `after-compact` skill.
