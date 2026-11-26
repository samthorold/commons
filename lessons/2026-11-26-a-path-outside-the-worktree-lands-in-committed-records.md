---
address: guides/agentic-development/agents-in-parallel.md
origin: samthorold/py-minimax-games#240
signal: trap
---

A worktree agent briefed with an absolute path to data in the main checkout can record that path in the files it commits. In the origin, a resumable run's state file stored its input folder as given, and that file was committed as the run's record. That put the owner's home directory into a public repo. Making the path repo-relative doesn't help: the data lies outside the worktree's root, so no relative path from the worktree reaches it. When a brief hands a worktree agent a path outside its worktree, the brief should also say how that path appears in anything committed: repo-relative, as it would be from the main checkout. The launcher should then grep the PR for the absolute prefix before merging.
