---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace - as `handoff-<slug>.md`, the slug naming the work (e.g. `handoff-commons-skills.md`). After `/clear`, a SessionStart hook ([hooks/handoff-list.py](hooks/handoff-list.py)) lists recent `handoff-*.md` files by name and age and has the fresh session offer the likely one before reading it, so the name is what the next session chooses by.

The handoff is transient by design. Before writing it, make sure anything durable is already in a commit, a doc or an issue (the Project knowledge Guide's first Stance).

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (epics, plans, system-design docs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
