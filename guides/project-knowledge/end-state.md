# Project knowledge Guide: the system design states its end state as hypotheses

How to apply the Stance *the system design states its end state as hypotheses*, from [the Project knowledge Guide](../project-knowledge.md#stance-the-system-design-states-its-end-state-as-hypotheses), which states the Stance.

## Why, in full

An end state is never certain. A mature project then drifts into local optimisation, each step judged against the last result instead of against where the work is going. Declaring rules before the readings makes that Drift visible as a declared value that changed with no design change. Status kept in the design would turn the design into a chronology.

## How to apply

- Where the domain is sourced, a hypothesis is a domain phenomenon the model should reproduce, and its rule uses the domain's empirical range (supported inside it, refuted wholly outside, undecided if it straddles), citing the number rather than restating it. A threshold of our own is set only where the sources give none, and a hypothesis no source supports is a candidate to drop: unsourced hypotheses are the ones that drift.
- Tests stay in the suite whatever the status. A status holds only for the implementation it was read on.
- A refuted hypothesis changes the system design, and that change is how the end state is revised. Declared values change only together with such a change.
- A reading declares its size or its stopping rule before it runs, as part of its reading rule. A reading that leans one way without crossing its line is undecided: read again on fresh runs, judged alone, or use a sequential rule that keeps going until it crosses a declared bound. Adding runs to the same reading until it crosses the line is not a reading.
- Where an instrument's error runs one way, the reading rule is asymmetric. Use is biased upward while the only user is also the builder, who opens the product to check their work as well as to use it: a window busy with development can refute (if even the builder doesn't open it, that is strong evidence) but never support, and *supported* needs a quiet window, declared by commit frequency. Filtering out the days with commits doesn't work during active development, because it excludes nearly every day.
- A clause whose scope depends on a baseline ("on a case already below the baseline, …") states the rule alone, and the test or report computes which cases it covers. Cases named beside it are labelled as examples, never as the list: a list worked out by hand misses cases, and where one went out with the rule, the rule is what was declared.
- A reading rule says the window it reads over and the points it is read at (back-to-back windows from a stated start, the latest ended window giving the status). A register derived on every view keeps no memory of when it last read, and fixed points stand in for that memory. A rule read over the whole history ("refuted by any missed day") is refuted for good by one bad day.
- A derived register learns from outside that what a hypothesis was read on has changed: a running system can't see a change to its own code. Feed the change in (commit history through an admin command, marking the paths the design names), and name in the design any change made only through configuration (switching a model), which commits don't show.
- The change a hypothesis is read on is a change to what runs. The paths the design names leave out the tests, recorded fixtures and dev tools beside the code, by the Stack's conventions for them (in Go, `_test.go` files and `testdata/`, which the toolchain never builds in). Matched by directory prefix, every test-only change, harness fix or re-recording makes hypotheses Due, each has to be deferred by hand, and a Due raised by a real change can't be told from the noise. A recording made for a changed act still lands in the same commit as the change to the act, so nothing that matters is lost.
- Between revisions, grain only gets finer. A hypothesis may be replaced by finer ones under the same part of the end state. A replacement that goes up a grain or sideways is a design change.
- A link means relevance, not sufficiency. Supported children don't make their parent supported: the parent is resolved only by its own test.
- Tests near the top are often cheap, coarse necessary conditions (e.g. "a game against a mock human ends in under ten minutes"). They can refute but not confirm, and they run on every change.
- A supported hypothesis doesn't move into the domain layer. Domain facts come from sources about the world.
