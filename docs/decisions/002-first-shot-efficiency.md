# First-shot correctness is the efficiency strategy

Status: Accepted

## Context

Token-efficient packs compress prompts, force terse output, and trim context every turn. That scores the wrong loop. A wrong first attempt burns the window twice and the human's reread. Per-message golf looks cheap and pays on the retry.

Always-on lean can still win on a rename, a format pass, or a throwaway script. More upfront context can still lose when docs are stale or rules contradict. The thesis is a bias, not a law.

## Decision

We optimize for the first attempt being the accepted attempt, net of its context tax. That is the question every intake prompt inherits.

How:

1. Expertise is on-demand. A skill or Manual `@` loads when the task matches. It is not an always-on tax.
2. `AGENTS.md` stays a map. The agent reads this file and at most two owners. Disposable thinking stays in `scratch/` and is not mapped.
3. A `/` command or prompt we keep must carry enough intent that a clarifying round is rare.

A short always-on prior (tens of words, one repeated miss) is allowed. A terse-output pack is not. See [001-native-first.md](001-native-first.md) for what we refuse to clone.

This does not apply to cheap reversible work: one-line edits, renames, format/lint, throwaway scripts, or a session where the user is already in the loop and will correct immediately. Do not load a skill or a second owner for those.

## Consequences

`.cursor/` stays the small set we ship. New rules, commands, and skills must beat a blank project on first-shot rate, not on tokens in the first message. If two owners disagree, delete or fix the stale one — do not add a third file to "clarify."

Future audits ask: does this raise the probability the first attempt is the accepted attempt, net of its context tax?
