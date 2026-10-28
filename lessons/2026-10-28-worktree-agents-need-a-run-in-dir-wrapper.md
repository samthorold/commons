---
address: skills/grind-issues/SKILL.md
origin: a private Adopter (see the portfolio)
signal: trap
---

A worktree sub-agent can't run a command from a package's directory. `cd` doesn't carry over between its shell calls, `cd <dir> && …` is refused as compound, and the Bash tool has no working-directory parameter (a brief that tells the agent to "use the Bash tool's cwd" sends it looking for one). In a monorepo whose test runners must start in the package (`flutter test`, `dart test`, many JS runners), each agent then improvises its own wrapper. The brief should hand it one: a small script, run by absolute path, that does `cd "$1"; shift; exec "$@"`, or the repo's own test script taking a package path.
