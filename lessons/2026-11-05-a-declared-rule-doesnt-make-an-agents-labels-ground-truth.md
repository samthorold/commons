---
address: guides/model-calls/fixtures-and-properties.md
origin: samthorold/go-slow#294
signal: gap
---

Declaring samples and a rule before drawing them doesn't make the labels they judge ground truth. An agent probing a judgement act wrote its own "these belong together" and "these don't" pairs, declared a pass rule first, and reported that one model passed. The owner challenged one negative, and most negatives proved contestable from the fixtures themselves, so a model that never joined them might simply have been missing what the act is for. The discipline around the rule made an opinion read like a measurement. A property can assert only what a source states or what needs no opinion of the answer (nothing lost, citations resolve, sizes, agreement between samples); anything else is the owner's reading, and a probe should hand the owner the output to read rather than a score.
