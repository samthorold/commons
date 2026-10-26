---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#91
signal: gap
---

The Stance judges a changed act by a declared pass rate against a fixed line. It says nothing about comparing the changed act with the one it replaces. With the few samples a small app can afford, a fixed line only separates "nearly always" from "often fails", while the question a change asks is "better or worse than before, and on what".

The statistics literature's cheapest gain is a paired comparison: sample the old and new versions on the same fixtures and compare per fixture. This removes the variance between fixtures for free (Miller 2024, "Adding Error Bars to Evals", https://arxiv.org/abs/2411.00640; read as a summarised page). The same source warns that a small suite detects only large effects. Detecting a 3-point difference needed about 1,000 cases.

In practice the per-sample tables in the origin PR were already a paired comparison, made informally: main's counts against the new version's, per fixture and per field. They were what showed a side effect no pass-rate line would have caught. Candidate rule: when an act's instructions or schema change, the samples of the change are reported paired with samples of the current version on the same fixtures, every output field counted, beside the pass-rate verdict.
