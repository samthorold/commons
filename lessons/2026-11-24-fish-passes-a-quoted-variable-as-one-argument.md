---
address: dotfiles claude/CLAUDE.md#permissions--allowlists-claude-code
origin: samthorold/explorers@1473eee:docs/agents/known-traps.md
signal: trap
---

Where the login shell is fish, Bash-tool commands run in fish, and fish never word-splits a variable. So `env $v cmd` or `env "$v" cmd` with `v="A=1 B=2"` passes a single variable named `A` with the value `1 B=2`, not two variables. A command that builds several environment variables or arguments from one string has to be a `sh` script that uses the variable unquoted, run by its absolute path. This is the same root cause as the dotfiles rule about quoting globs under fish, and belongs beside it.
