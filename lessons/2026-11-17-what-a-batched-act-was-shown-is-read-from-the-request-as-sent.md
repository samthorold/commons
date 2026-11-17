---
address: guides/model-calls/kept-calls.md
origin: samthorold/go-slow#322
signal: gap
---

An act whose result is applied later (a batch) and whose input shows judgements from upstream acts can't rebuild "what the model was shown" from the current record when the result arrives. Upstream judgements made between sending and applying (often in the same batch turn) change the rebuilt input, so a byte-for-byte comparison refuses most results, and a lenient rebuild checks citations against text the model never saw. Two rules follow. Number the source's stretches independently of any upstream judgement: a stretch an upstream act rejects keeps its number and is left out, rather than shifting every later number. And read what was shown, including what was left out, from the request as sent (which is kept anyway), never from a rebuild.
