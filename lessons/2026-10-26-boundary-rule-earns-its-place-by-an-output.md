---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#117
signal: gap
---

A rule that settles a classification boundary in an act's instructions (where one category ends and the next begins) earns its place only through an output the end state reads that it changes. A boundary that changes no such output is left to feedback and its precedents, and the act's instructions say nothing about it.

Why: the Stance already says that text added to the instructions shifts the model's judgement on every input, but it doesn't say when that cost is worth paying, and a grill tends to pursue every boundary the recordings show the model drawing inconsistently. Inconsistency alone isn't a reason. The case: an act sorts statements into two categories, only one of which can reach the daily output. Two boundaries (is an arranged future event in the reportable category; is a declared intention) decided whether real news could ever appear, and earned rules. A third (is a hedged timetable a plan or a forecast) was drawn inconsistently too, but either answer left the daily output practically unchanged. The owner stopped the grill there by asking what it would change in the output, and nothing did. The hedged timetable got no rule; feedback marking it wrong, with its precedent, covers it.

How it would apply: before writing a boundary rule into an act's instructions, name the output the end state reads that it changes, and the part of the end state that reading serves. If there is none, the act's instructions say nothing, and the boundary is left to the feedback the end state already reads.
