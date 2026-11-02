# Model calls Guide: an act is judged over its samples, in the suite

How to apply the Stance *an act is judged over its samples, in the suite*, from [the Model calls Guide](../model-calls.md#stance-an-act-is-judged-over-its-samples-in-the-suite), which states the Stance.

## Why, in full

A property passing on one sample says little about its pass rate: a recording that happened to pass hides a flaky property until the next re-recording exposes it. A rate judged once at recording time is a claim in a PR body that nothing checks again; a later change to how a property is asserted quietly stops testing the samples it was measured on. Derived on every run, the status stays true of the code, as a register's does (Project knowledge Guide, end-state Stance). Pooled across fixtures, a rate hides a property that fails on one input.

## How to apply

- Declare N and each property's rule (supported, refuted, undecided, by count) before the samples are drawn, as reading rules are declared.
- A sample is one piece of work run as it runs in use, with the act's retry budget. Passing the act's own checks is rated over all samples ("passes within its attempts": a refused try costs a retry, not a wrong output). A property only the suite asserts runs nowhere in use, so it is rated over the samples that passed their checks.
- A re-recording reads its failures by where they fall. The same fixture failing the same check on every try is a regression. On a large share of tries but not all, it is a slip: a defect in the act, paid for as a retry every time it happens in use. Different fixtures failing on different tries is flake. Only flake is answered by drawing again.
- **Rest each use on the judgement reliable enough for it.** When an act's output varies between samples, first ask what rests on it, before tightening the instructions. Where several uses read one act's output, each rests on the most reliable judgement that serves it, by what a miss costs there: a candidate search can rest on what a text names (among the most reliably judged), while a link shown to the owner, where a false tie misleads, needs the judgement it shows. The variation then decides only what costs least to get wrong. A wider candidate set needs a bound to keep each call's cost flat.
- Redrawing a fixture re-reads every property it has. A slip, or any property refuted or undecided that the run wasn't aimed at, stops the run and is reported, never redrawn: drawing until a count crosses its line is not a reading. The fix is a change to the act (*change an act on its cheapest stage*). A slice that redraws one fixture for a narrow reason counts the cost of re-reading all of it when it is sized.
- How a change to an act reports its samples beside the current version's (the paired report) is in [changing an act](changing-an-act.md).
