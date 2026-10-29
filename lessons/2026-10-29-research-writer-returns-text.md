---
address: guides/agentic-development.md#agents-in-parallel
origin: a private Adopter (see the portfolio), research slices run with the deep-research Skill
signal: trap
---

In Claude Code, the deep-research Skill's report writer, run as a sub-agent, couldn't write its report file: the harness blocked the write, though researcher sub-agents wrote their notes into the same tree. Telling the writer to return the report as its final message, and having the coordinator save it with Write, works, and gives the coordinator a natural point to fix the report before it lands (house style, pronouns, relative links, a section the writer mustn't write). A brief for the writer should say so up front, or the writer spends its run failing to save.
