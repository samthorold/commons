---
address: guides/model-calls/what-the-model-is-shown.md
origin: samthorold/go-slow#380
signal: gap
---

A model searching a record by words is guessing what the record's authors wrote, and when it reaches for a subject rather than a name it asks with several words in no order it can know (a bag of words). A strict match (the words as a phrase, or every word in one passage) then fails exactly when the guess is broadest, and the model spends its turns narrowing, or falls back to another tool. Matching any of the words, ranking the passages that hold the most first and showing beside each which words it holds fits how the model asks instead of instructing against it. Unlike a likeness or embedding search, it decides nothing out of sight: the model sees why each passage is listed and judges whether it bears. The cost is that a phrase ranks no higher than its words scattered, which the model reads in place.
