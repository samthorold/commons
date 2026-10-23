---
name: grill-me
description: Interview the user relentlessly about a plan or decision that has no repo docs to write into (how they work, a plan outside any project, the shape of a workflow), resolving each branch of the decision tree. Use when user wants to stress-test such a plan, get grilled on it, or mentions "grill me". For a plan that belongs to a repo, use grill-with-docs; for a concept that is itself still in question, open-session.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

Ask only what needs me. A question you can answer confidently from the Commons, the docs or the sources, answer it yourself, say so, and carry on. For each question you do ask, give a light recommendation.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

If the plan turns out to belong to a repo, whose `CONTEXT.md` and design docs should record what's settled, switch to `/grill-with-docs`. If the questions keep getting reshaped instead of answered, the concepts themselves are in question: switch to `/open-session`.
