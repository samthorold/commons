---
address: guides/agentic-development.md#the-pr-workflow
origin: samthorold/py-minimax-games#188
signal: trap
---

When two branches each append a section at the same place in a shared document (a results log that parallel agents add to), git can line up text the two additions share and cut the conflict in the wrong place. A heading that follows both additions (here `## Milestone 7: ...`) was split across the conflict blocks, so resolving by keeping both sides in order left a heading fragment in the middle of one section and dropped it from where it belonged. The Guide's check, that `git diff origin/main --stat` lists only the PR's own changes, can't see this: the files and line counts look right. After resolving a conflict in prose, read the resolved region through, or diff its headings against `origin/main`'s (`git diff origin/main -- <file> | grep '^[-+]#'`): every heading on `main` should still be there, unchanged.
