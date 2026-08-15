# /keep

Arm or disarm compact rehydrate for this workspace.

- `/keep on` — write `scratch/keep-alive` (one line: `on`). The `after-compact` skill may then run when the chat looks summarized.
- `/keep off` — delete `scratch/keep-alive`.
- `/keep` — report whether the file exists.

Do not commit `scratch/keep-alive`. Do not write a session diary. The rehydrate body is `.cursor/skills/after-compact/SKILL.md`.
