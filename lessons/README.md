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

**Promotion**: read the Lesson with its Guide side by side, follow the Origin to the evidence, then either revise the Guide (reason in the commit) and delete the Lesson file in the same commit, or delete the Lesson as Local or wrong.
