---
address: guides/model-calls/what-the-model-is-shown.md
origin: samthorold/go-slow#379
signal: gap
---

When a model chooses a tool's input (the words of a search), how the tool interprets that input (a phrase in order, all the words anywhere, any of them) is part of the act, as much as its instructions. Left out of the design, it gets fixed by whoever writes the tool's code, and a description vague about it ("matched as whole words") lets the model assume another rule: it asks in a way the tool never answers, every answer is empty, and no property fails, since an empty answer is a valid one. The design should state the rule and why, the tool's description should state it exactly, and the recorded runs should count how the asks landed (on every part of the input, on some, on none), so a mismatch between how the model asks and how the tool matches shows up as a number someone reads, not as a quiet drop in reach. While the tool's design is still being refined in use, the count is read without a declared rule: a rule declared before the design lands fixes a threshold for a mechanism that is about to change.
