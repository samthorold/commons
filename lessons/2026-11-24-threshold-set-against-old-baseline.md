---
address: guides/project-knowledge/end-state.md
origin: samthorold/py-minimax-games#227
signal: gap
---

A reading rule with an absolute threshold is calibrated, implicitly, against the baseline the instrument gave when the rule was written. When the instrument is fixed or changed, read the champion (the current baseline) on it before reading any candidate: the champion may now sit near or past the threshold, so the rule no longer tests what it was written to test (here a threshold set when the baseline read about 2% asked, after the fix, for only a few points more than the baseline's 21%). Thresholds that are about whether a candidate gains something are better stated relative to the champion's reading on the same instrument, so an instrument change doesn't silently move what "supported" means. Any restatement is an End state change made before the candidate is read against it, not after.
