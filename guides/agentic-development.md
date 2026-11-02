# Agentic development Guide

**Scope:** every Stack, every Archetype. The topic is how agents change a repo: branches, PRs, merging, and agents working in parallel.

Each Stance's *How to apply* and the full text of its Why, and the Conventions for one job, live in their own files under `~/.claude/commons/guides/agentic-development/`, and this Guide says when to read each. Links are relative to this file.

## Stance: agents implement test-first

- **Stance:** an agent implements a change through test-driven development, in vertical slices: one failing test, the code to pass it, refactor, repeat (the `/tdd` Skill). Never all the tests first, never the code first.
- **Why:** an agent working unattended needs an objective signal of done that it didn't shape to fit its own code.
- **How to apply:** before implementing a feature or fixing a bug, inside a Skill-driven run or not, read [test-first](agentic-development/test-first.md).
- **What would change our mind:** work where a failing test can't express the intent before the code exists, such as throwaway prototypes (the `prototype` Skill) and exploratory spikes whose output is a finding, not code to keep. Those are exempt as long as their code isn't merged as-is. If a kind of change keeps needing that exemption, record a Lesson.

## Stance: decide, record, carry on

- **Stance:** an agent makes reversible calls itself and records each one where the next reader will look (the PR body, the issue, the commit message), rather than stopping to ask. At natural boundaries (a PR, half an epic) it reports a short status and carries on by default.
- **Why:** the owner delegates heavily: a question that waits for an answer stalls the run, while a recorded call costs at worst one revert.
- **How to apply:** when a Skill or a task says to confirm with the owner or wait for their approval or verdict, or a step seems to need their say (a spend, an expensive run, a merge), read [decide, record, carry on](agentic-development/decide-record-carry-on.md).
- **What would change our mind:** recorded calls of one kind keep being reverted. That kind should stop and ask, and its boundary goes here. Beyond expense, which calls are not the agent's to make at all is still to be settled (the structure agent autonomy rests on).

## The PR workflow

- Every change goes through a branch and a PR, never straight to `main`.
- **Before merging a PR, read [merging](agentic-development/merging.md).** It decides that a PR whose checks all pass is squash-merged without asking, release PRs included, and that agents merge only on green, never with failing or pending checks; and that merge authority is granted per repo, never globally.
- **When a branch falls behind `main` or merging `main` into it conflicts, and before pushing a branch you merged `main` into, read [catching up with `main`](agentic-development/catching-up-with-main.md).** It decides that `main` is merged in, never rebased, that conflicts are resolved hunk by hunk, and the checks against `origin/main` before pushing.
- **Before a change to an Adopter whose system design states an end state, read [Due hypotheses](agentic-development/due-hypotheses.md).** It decides that the change starts by reviewing the Due hypotheses it could affect.

## Agents in parallel

**Before launching an agent or writing its brief, when one hands back, or, as a sub-agent, before opening an issue or saving a document, read [agents in parallel](agentic-development/agents-in-parallel.md).** It decides one worktree and branch per agent, what a brief carries (the workflow rules, the detail files its job triggers, any act gated on the owner's say, with its cap), when slices run in parallel or in sequence, what goes back on a returned PR, and that the launcher opens follow-ups and cleans up.

## Idle sweeps

**When you are waiting on a background process (CI, a long test run or reading, a Monitor) with nothing else of your own to do, read [idle sweeps](agentic-development/idle-sweeps.md).** It decides that a wait longer than a minute or two goes on one read-only slice of the sweep, which is reported, not acted on.

## Known traps

- **GitHub closes `#N` wherever a closing keyword sits directly before it**: `close`, `closes`, `fix`, `fixes`, `resolve` or `resolves` (any case), anywhere in a PR body or commit message, even inside a quoted table cell or a sentence about another issue. Merging then closes that issue unintended. Write "#N closes" or "the row closing #N" unless you mean it, and check a PR body's references before merging (`grind-issues` does this). *Remove when:* GitHub stops treating keywords in quoted text as closing, or a check enforces it on every PR.
- **A delegated agent can outlive its hand-back.** A sub-agent can report done while work it started is still running: its own sub-agent, which goes on to commit, open a PR or overwrite a shared file, or background processes (long test or simulation runs). Before touching a branch after a delegated agent hands back: wait for every completion notification, check `gh pr list --head <branch>` and running processes, and confirm the branch head is stable. Give every file a delegated agent writes outside its worktree (PR bodies, helper scripts, notes in a shared scratchpad) a name unique to that agent, and don't let delegated agents spawn agents of their own. Running agents in parallel makes this more likely, not less. *Remove when:* the harness stops reporting a sub-agent done while its own work runs; `grind-issues` already applies the check, so this entry covers delegation outside it.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit a workflow problem another project would also hit, record a Lesson addressed to this Guide (to the detail file, where the Lesson is about how to apply a Stance or a job's Conventions), as described in `~/.claude/commons/lessons/README.md`.
