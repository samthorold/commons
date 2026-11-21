---
address: guides/model-calls/recording.md
origin: samthorold/go-slow#376
signal: trap
---

Recording a reference API's responses verbatim as fixtures (a knowledge base's items, say, for an act's look-ups) can produce files of megabytes each (an item for a country), past `check-added-large-files`' 500 KB limit, and a set too large to commit. Keep each response as given except the fields the adapter never reads, and add a test that the adapter reads the same values from a trimmed response as from the full one, so the trim can't drop something the code later starts to read.
