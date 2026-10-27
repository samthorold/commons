---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#123
signal: gap
---

A slice that re-records one fixture for a narrow reason (a new check refuses one of its samples) re-reads every property of that fixture, not only the one it was aimed at. On an unchanged request, a property that sat at N of N can come back refuted on the fresh draw from the model's variance alone, and the slice is then blocked on a design change it never set out to make.

The case: a new plain-code check refused one sample of one fixture, so the fixture was redrawn on fresh samples. Every sample passed the act's checks, the new one included, but an unrelated test-only property (a Fact placing the event where it happened) fell from 5 of 5 to 3 of 5, which the rule reads as refuted. The request hash was unchanged, so the act was the same act.

The Guide's flake-or-regression rule covers checks failing across tries, but not a property refuted on a fresh draw that was made for another reason. Candidate rule: a brief that re-records a fixture says what happens if any of its properties comes back refuted or undecided, not only the one in view. The default is to stop and report rather than redraw, since a second draw aimed at the line is shopping for a result. And a slice whose only need is to replace one refused sample should count the cost of re-reading the whole fixture when it is sized.
