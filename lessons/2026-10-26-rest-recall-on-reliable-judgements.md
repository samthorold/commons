---
address: guides/model-calls.md
origin: samthorold/go-slow#92
signal: gap
---

When several parts of an app use the outputs of one model act, decide for each use which judgement it rests on, by what a miss costs there and how reliably the judgement is made. In an extraction app, one judgement (which named things a statement involves, and in what role) fed both the search for candidates (which threads a new item could belong to, which nearby facts it could be caused by) and the links shown to the owner (two threads connected because one entity plays the same role in both). For the search, a miss costs a duplicate thread. For the links, a false tie misleads the reader. Annotation studies, and model evaluations, put the two candidate judgements far apart: what a text *names* is among the most reliable (κ around .8 to .95), while which named thing a statement involves in what role, and above all what a text is *about*, are among the least. So the search rests on what the item names and the links on the role judgement. The judgement's run-to-run variation then decides only what it costs least to get wrong. A wider candidate set needs a bound (here, ranking by shared entities weighted by rarity) to keep each call's cost flat.

The Guide says how to test an act and what it is shown, but not that its outputs' uses should be matched to their reliability. When an act's output varies between samples, that is the first question to ask, before tightening its instructions: does anything that pays for a miss rest on this judgement?
