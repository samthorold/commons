# Lessons

Lessons waiting for Promotion. One file per Lesson, named `YYYY-MM-DD-<slug>.md`, committed straight to `main` in this repo.

```markdown
---
address: guides/python.md#tooling   # the narrowest Guide (and Stance/Convention) it's about; a missing Guide is fine
origin: samthorold/<repo>@<commit-or-PR>   # the evidence; may be a private repo
signal: contradiction | deviation | gap | trap
---

<the claim: what seems to be true, and why>
```

**This repo is public.** Write the claim generically ("a PyO3 build script can't find the venv's Python when…"), with no private project details; the Origin link carries the specifics.

## Lessons are an inbox, not a reference

Nothing loads this directory by default, and agents shouldn't rely on it while working: a Lesson only matters once it's in a Guide. Every Lesson ends deleted; what lasts is the Guide's text, the Revision's commit message and the Origin's evidence (and the Lesson stays in git history).

## When Promotion happens

- **On touch**: before writing or revising a Guide, read every Lesson whose `address` is that Guide (`grep -l "address: guides/<guide>" lessons/*.md`), and resolve them in the same piece of work.
- **Sweep**: a recurring review of the whole inbox, tracked as an issue in the private portfolio repo. Several Lessons with the same Address are the strongest case for acting.

## Promotion

Read the Lesson with its Guide side by side, follow the Origin to the evidence, then:

| Outcome | What lands in the Guide | The Lesson file |
|---|---|---|
| **Promoted** | A new or revised Stance or Convention. | Deleted in the same commit. |
| **Rejected, but worth knowing** | A Stance against it ("don't do X, because…"), or a line under an existing Stance's *what would change our mind*, so nobody proposes it again. | Deleted in the same commit. |
| **Local or trivial** | Nothing (perhaps a note in the Adopter's own docs). | Deleted. |

The reason goes in the commit message.
