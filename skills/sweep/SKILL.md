---
name: sweep
description: Run the recurring Sweep of the Commons: promote, reject or drop the Lessons in the inbox one Guide at a time, review Known traps against their *remove when*, and record the Propagation each Revision needs. Use when user says "sweep", "run the sweep", "process lessons", "clear the inbox", or wants the Commons brought up to date with what Adopters have learned.
---

# Sweep

The recurring review the vocabulary calls a **Sweep** (`~/.claude/commons/CONTEXT.md`), run when the owner chooses. How a Lesson is judged and what each outcome leaves behind is `~/.claude/commons/lessons/README.md` (*Promotion*); this Skill applies it. Where they seem to disagree, the README wins.

The owner is present, so give every verdict as a recommendation the run acts on unless corrected (Agentic development Guide, *decide, record, carry on*), and batch the verdicts per Guide rather than asking Lesson by Lesson.

## Arguments

- none: the whole inbox, then Known traps if the last traps pass is more than a month old.
- a Guide (`model-calls`, `web-apps`, …): only that Guide's Lessons.
- `traps`: only the Known traps pass.

## Startup

1. **Read the findings since the last Sweep.** The recurring sweep's issue is named in the Portfolio (`~/Projects/portfolio/projects.md`). Read its comments back to the last full Sweep: idle sweeps have already judged some Lessons and traps, so start from their verdicts instead of judging again.
2. **Inventory the inbox**, grouped by Address with each Lesson's age:

   ```
   grep -H "^address:" ~/Projects/commons/lessons/2*.md
   ```

   Skip Lessons with a `waiting:` line whose condition still isn't met, and list them separately.
3. **Present the plan**: the Guides in order of how many Lessons each has, most first. Flag any Guide with **five or more** Lessons: a cluster that size means the Guide is still taking shape, and promoting one Lesson at a time would patch it over and over. Recommend a `needs-design` issue for a grill of that Guide (on the Portfolio repo, since it spans Adopters), with the Lessons listed, instead of promoting them here. The owner may take the grill there and then.

## Per Guide

Work through one Guide at a time, and finish each (committed and pushed) before starting the next, so a run stopped halfway leaves nothing half-promoted.

1. **Read side by side**: the Guide, every Lesson addressed to it, and each Lesson's Origin (the commit or PR, via `gh` or the local clone). Then do the README's *on touch* search of the Adopters' docs for Local knowledge about the same Guide that was never recorded as a Lesson.
2. **Decide each Lesson** with the README's table, plus one more outcome:
   - **Promoted**, **Rejected but worth knowing**, **Local or trivial**: as the README says.
   - **Waiting**: true as far as it goes, but its evidence is one Adopter and the Promotion depends on a second, or on a reading not yet taken. Add a `waiting: <condition>` line to its frontmatter. A Lesson that is still waiting **30 days** after it was written is decided at this Sweep, one way or the other: an inbox that keeps Lessons forever has become a reference.
   - Check the Address too: a Lesson may belong to a broader or narrower Guide than the one it names (*one home per rule*), or to a Guide that doesn't exist yet. A missing Guide goes on `MAP.md`'s Known Gaps.
3. **Present the verdicts** for this Guide in one table (Lesson, outcome, the text that will land, in a line), then apply them.
4. **Write the Revision.** Check it against `CONTEXT.md` before committing: a Stance has all four parts, a Known trap has its *remove when*, nothing restates another Guide, and a trap sits as high on the ladder as it can. **The Commons is public**: generic wording, no private project names (they're in the Portfolio), Origins only in the Lesson files being deleted, not in Guide text.
5. **Commit** the Guide change and the deleted Lesson files together, straight to `main`, with each Lesson's outcome and reason in the message. Push.
6. **Note the Propagation**: find the Guide's Adopters by their Import (`grep -rl "commons/guides/<guide>.md" ~/Projects/*/CLAUDE.md`) and say which are now behind. Draft one issue per Adopter, or one Portfolio issue if several need coordinating (Portfolio, *Where work is tracked*), and open them once the owner agrees.

## Known traps

Every Known trap in the Guides and in the dotfiles `CLAUDE.md`:

- **Is its *remove when* met?** Check it against the world rather than recall: the installed tool's version, the upstream issue's state. If met, remove the trap (a Revision).
- **Can it move up the ladder** (`CONTEXT.md`, *Known traps are the weakest fix*)? Name the hook, CI check, Skill step or Convention that would replace it, and draft the issue that would build it.

Commit removals per Guide, as above.

## Completion

1. **Report on the sweep's issue** in one comment: per Guide, what was promoted, rejected, dropped and left waiting (with commits), the grills recommended, the traps reviewed, and the Propagation issues opened.
2. **Do a Lesson pass on the Sweep itself** (the four Signals): where this Skill, the Lessons README or the format got in the way, record a Lesson addressed to it. The next Sweep promotes it.

## Rules

- **One Guide at a time, one commit per Guide.** Never leave a Lesson promoted in the Guide but still in the inbox, or the other way round.
- **Every Lesson ends deleted** (or explicitly waiting). What lasts is the Guide text, the commit message and the Origin.
- **Read the Origin, don't trust the claim.** A Lesson is one agent's account; the evidence decides.
- **Public repo.** Check each diff for private details before pushing.
