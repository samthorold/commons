---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#72
signal: contradiction
---

The Stance says to judge pass rates at recording time and have the suite replay one sample. That leaves each rate as a claim in a PR body that nothing checks again: a later change to how a property is asserted quietly stops testing the samples the rate was measured on. Committing every sample, and having the suite replay them all and judge each property by its declared rule on every run, keeps status derived rather than stored, as a register's is. The cost is larger recordings. It also removes the question of which sample to replay.

The Stance is also silent on what one sample is when the act retries in use. An act whose own checks run in production, with a retry budget, fails in two different ways:

- A refused check costs a retry, not a wrong output. Its property is "passes within its attempts".
- A property only the suite asserts runs nowhere in use, so every failure is a wrong output. It is rated per call, over the samples that passed their checks.

Rating both per call treats a cost like an error. So a sample is one piece of work run with production's retry budget, and the two kinds of property are rated apart. Judge each fixture separately rather than pooled across fixtures: a property can fail on one input while the pooled rate looks fine.
