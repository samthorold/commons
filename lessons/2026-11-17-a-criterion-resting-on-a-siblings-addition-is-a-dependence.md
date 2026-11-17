---
address: guides/agentic-development/agents-in-parallel.md
origin: samthorold/go-slow#314
signal: gap
---

Two slices of one epic were run in parallel because neither's design depended on the other's outcome. But one slice's acceptance criteria named a capability the other was still adding (show an earlier editor-written passage that a new item cites, when citing such passages was the sibling's work). The agent could meet those criteria only by guessing the sibling's storage, so it left them out and handed back a partial PR, which cost a send-back once the sibling merged. The test for sequencing should include this: when a slice's acceptance criteria use a concept, table or capability that another open slice introduces, that is a dependence, even when the designs don't otherwise touch. Either sequence the slices, or say in the brief which criteria wait for the sibling and send the PR back for them once it merges.
