---
address: guides/model-calls/changing-an-act.md
origin: samthorold/go-slow#382
signal: gap
---

Frozen copies of an upstream act that calls tools aren't frozen when the downstream harness rebuilds its input by replaying the upstream conversation and answering its tool calls with today's code. A change to only what a tool answers (how a search matches, so an empty answer now lists numbered passages) renumbers what the frozen answer's citations stand for: the downstream act goes stale, and re-recording it over its copies records it on output the model never wrote. The detail file names plain code crossing frozen copies in general; this case is easy to miss because the upstream act's own recordings are untouched by the copies, and a brief expecting the downstream act to stay clean is wrong. Until the harness replays the kept tool results instead, a change to what an upstream act's tools answer budgets a refresh of the downstream copies in the same change.
