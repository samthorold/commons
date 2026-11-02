---
address: guides/project-knowledge.md#stance-the-system-design-states-its-end-state-as-hypotheses
origin: samthorold/go-slow#271
signal: gap
---

When a register learns from commit history that what a hypothesis was read on has changed ("marking the paths the design names"), the paths should cover only what is built into the running system. Test files, recorded fixtures and dev tools often sit under the same directories as the code they test. Matching by directory prefix makes every test-only change, harness fix or re-recording raise hypotheses Due, even though nothing in use changed. Each of those then has to be deferred by hand, and a Due raised by a real change can't be told apart from noise.

The design should define the change a hypothesis is read on as a change to what runs. Tests, recordings and tools beside the code are excluded, by the conventions the Stack uses for them (in Go, `_test.go` files and `testdata/`, which the toolchain never builds in). A recording made for a changed act still lands in the same commit as the change to the act, so nothing that matters is lost. A change made only through configuration still has to be fed in separately, as the Guide already says.
