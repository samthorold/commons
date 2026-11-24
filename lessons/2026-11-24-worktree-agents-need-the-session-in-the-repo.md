---
address: skills/grind-issues/SKILL.md
origin: samthorold/explorers#877
signal: trap
---

When `grind-issues` is asked to work a named repo from a session started in a parent folder that isn't itself a git repo, the first `Agent` call with `isolation: "worktree"` fails: "Cannot create agent worktree: not in a git repository". The harness makes the worktree from the session's working directory, not from the repo the issues belong to. `cd` into the repo's checkout first (in the main session `cd` carries to the next call when it ends inside the working directories), then launch. The skill's Startup could make that its first step when the user names a repo.
