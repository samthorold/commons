# Global Guide

**Scope:** every Stack, every Archetype.

Conventions used only when setting up a repo or changing its settings, CI or hooks live in their own files under `~/.claude/commons/guides/global/`, and each section says when to read its file. Links are relative to this file.

## GitHub repo settings and branch protection

- **When creating a GitHub repo, or changing its merge settings, its `main` ruleset or its CI job names, read [repo settings](global/repo-settings.md).** It decides squash-only merges whose commit is the PR's title and body, and a `main` ruleset requiring the CI job names (none on a free private repo, recorded as a Deviation).

## Checks and CI

- **When setting up a repo's checks or CI, or changing its pre-commit hooks or workflows, read [checks and CI](global/checks-and-ci.md).** It decides that the checks are the pre-commit hooks, which ones every repo has, and that CI is one `pre-commit` job running exactly them; the Stack's Guide completes it.
- **Files a program writes and checks back are written as the hooks would leave them** (recorded fixtures, generated files: ending in a newline, no trailing whitespace). *Why:* otherwise a hook rewrites the file on commit, and anything that hashes it, compares it byte for byte or checks it is unchanged breaks. Fix the writer; excluding the files from the hooks is the fallback.

## Issues

- **Work is tracked in the repo's GitHub Issues**, through `gh`. A repo that tracks it elsewhere, or labels differently, records a Deviation in its `CLAUDE.md`.
- **An open issue is in one of three states**, by what it needs next, not by who does it:
  - `ready`: specified well enough to work on, by an agent or by the owner.
  - `needs-design`: needs a design session with the owner (a grill) before it can be `ready`.
  - no state label: the backlog, not yet looked at or not scheduled. Nothing picks it up.
- **An issue that won't be done is closed as *not planned*.** If the reason is worth knowing, it goes into the system-design docs, as part of why the design has its shape.
- **An epic** (a whole feature, broken into slices) says "Epic" in its title and carries no state label, so it is never picked up as work; its slices are.
- **A slice's body is its contract**: *Parent* (the epic, if any), *What to build* (behaviour end to end, not layer by layer; no file paths, which go stale), *Acceptance criteria* (each independently checkable), *Out of scope*, *Blocked by* (issue references, or "None"). When discussion changes the contract, rewrite the body rather than leaving the change in comments.
- `bug` and `enhancement` are optional categories, not states.

## Known traps

- `actionlint-py` ships only an sdist that downloads the binary on build. On macOS with python.org Python that fails with `CERTIFICATE_VERIFY_FAILED` until `Install Certificates.command` has run; one-off workaround `SSL_CERT_FILE=/etc/ssl/cert.pem` before the install. *Remove when:* actionlint-py ships wheels, or the Guides drop it for another way to get actionlint.
- pre-commit only sees tracked files: stage a new file before expecting a hook (e.g. shellcheck) to check it. *Remove when:* pre-commit checks untracked files (by design it doesn't, so probably never).

## Lessons

If something in a Guide proves wrong or incomplete while you work, or you hit something another project in the same Stack or Archetype would also hit, record a Lesson as described in `~/.claude/commons/lessons/README.md`. The Signals and the filter are in `~/.claude/commons/CONTEXT.md`.

- **A Lesson pass** (checking the four Signals) runs at the end of a grill and at the end of a `grind-issues` run: the checkpoints where the owner is present and thinking about design, or where several units of work come back together. Elsewhere, record a Lesson when one is obvious; a missed one recurs.
- **A sub-agent reports what it found to whoever launched it, and doesn't record it.** The launching agent records, so parallel agents can't write duplicate Lessons.
