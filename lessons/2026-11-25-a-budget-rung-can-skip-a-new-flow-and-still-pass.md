---
address: guides/emergent-systems/substrate-is-part-of-the-end-state.md
origin: samthorold/explorers#908
signal: gap
---

A cheap rung that reads a budget (an agent's income against its upkeep, over one step) can go on passing after the substrate gains a cost, because its arithmetic doesn't count the new flow. Here a new tissue-renewal cost acted last in the tick, after the one tick the rung reads, so the rung passed unchanged at 1.0012×; counted, the founder's income covered only 0.77 of its upkeep. When a change adds or moves a flow in the substrate, each budget rung's arithmetic is checked for whether it includes that flow, not just whether its test still passes; where it doesn't, whether it should is a question about the rung's rule, for the owner, not a fix to the test.
