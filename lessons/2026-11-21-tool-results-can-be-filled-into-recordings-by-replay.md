---
address: guides/model-calls/recording.md
origin: samthorold/go-slow#371
signal: gap
---

Where a tool-using act's replay rebuilds its tool results deterministically from frozen inputs, recordings made before they kept tool results (the Convention that a recording keeps, beside each turn, what the tools returned) can be brought up to it without spending: run the recording path over the existing recordings with a model that fails on any call. Only attempts whose requests are still current can answer, so the requests and responses stay byte-identical and the tool results are added beside them. The Convention says what to keep but not that adopting it late needn't cost a re-record, so an agent may re-record, or put the Convention off, when the change is free.
