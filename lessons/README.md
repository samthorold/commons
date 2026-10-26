# Lessons

Lessons waiting for Promotion. One file per Lesson, named `YYYY-MM-DD-<slug>.md`, committed straight to `main` in this repo.

```markdown
---
address: guides/python.md#tooling   # the narrowest Guide (and Stance/Convention) it's about; a missing Guide is fine
origin: samthorold/<repo>@<commit-or-PR>   # the evidence: where the claim is shown, when such a place exists; may be a private repo
signal: contradiction | deviation | gap | trap
waiting: <condition>   # optional, added by a Sweep: what Promotion waits on
---

<the claim: what seems to be true, and why>
```

**One claim per Lesson.** A second claim, above all one for another Guide, is a second Lesson, so each can be promoted on its own.

**This repo is public.** Write the claim generically ("a PyO3 build script can't find the venv's Python when…"), with no private project details; the Origin link carries the specifics.

## Lessons are an inbox, not a reference

Nothing loads this directory by default, and agents shouldn't rely on it while working: a Lesson only matters once it's in a Guide. Every Lesson ends deleted; what lasts is the Guide's text, the Revision's commit message and the Origin's evidence (and the Lesson stays in git history).

## When Promotion happens

- **On touch**: before writing or revising a Guide or Skill, read every Lesson whose `address` is it (`grep -l "address: guides/<guide>" lessons/*.md`), and resolve them in the same piece of work. Also search the Adopters' own docs for Local knowledge about it that was never recorded as a Lesson, e.g. known traps mentioning the Skill (`grep -rli "<name>" ~/Projects/*/CLAUDE.md ~/Projects/*/docs`), and promote what passes the filter. Once the general part is in the Commons, the Adopter's own copy can be cut down to what's specific to it (in that Adopter's own workflow, e.g. its next PR touching those docs).
- **Sweep**: a recurring review of the whole inbox, run by the owner when they choose with the `sweep` Skill, and tracked as an issue in the private portfolio repo. Idle sweeps (Agentic development Guide) report findings on that issue between sweeps; the sweep starts from them. Several Lessons with the same Address are the strongest case for acting. The sweep also reviews every Known trap (in the Guides and the dotfiles `CLAUDE.md`): is its *remove when* met, and can it move up the ladder in `CONTEXT.md`?

## Promotion

Read the Lesson with its Guide side by side, follow the Origin to the evidence, then:

| Outcome | What lands in the Guide | The Lesson file |
|---|---|---|
| **Promoted** | A new or revised Stance or Convention. | Deleted in the same commit. |
| **Rejected, but worth knowing** | A Stance against it ("don't do X, because…"), or a line under an existing Stance's *what would change our mind*, so nobody proposes it again. | Deleted in the same commit. |
| **Local or trivial** | Nothing (perhaps a note in the Adopter's own docs). | Deleted. |
| **Split** (claims for different Guides, or only part ready) | The ready part, as one of the rows above. | Rewritten to the remainder, with its new Address and a line saying what went where, in the same commit. |

The reason goes in the commit message.
