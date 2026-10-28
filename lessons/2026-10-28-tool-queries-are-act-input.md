---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#158
signal: gap
---

When an act is an agent with tools, what its tools return is part of the act's input, and it comes from app code far from the act: a storage query the tools share with a page, say. A change made for the page (here, which records a derived relation counts) changes what the agent is shown on the next run. It can make the agent's recorded conversations stale, and so carry the agent's re-record cost (the most expensive act's) inside what looks like a storage or UI change. Nothing in the act's own code or instructions shows it.

How it would apply: name, beside each tool-using act, the queries its tools read, so a change to one is seen as a change to the act. And brief a slice that changes such a query to run the agent's replay and stop for the owner's say if it goes stale, rather than discovering the cost at merge.
