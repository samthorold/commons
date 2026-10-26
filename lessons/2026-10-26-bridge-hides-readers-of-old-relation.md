---
address: skills/to-issues
origin: samthorold/go-slow#113
signal: gap
---

When an epic moves what something rests on from one relation to another in slices, an interim bridge (keep filling the old relation from the new data until every reader has moved) hides the readers the plan forgot. Every reader of the old relation keeps passing its tests, so nothing fails to say which were left behind, and the slice that finally removes the bridge breaks them silently.

The case: a plan moved "what finds work" from per-statement ties to per-item mentions, listing three readers in one slice. A fourth reader, the query choosing past feedback to show as precedent, rested on the same ties and wasn't listed. It went on working only because of the bridge, and was found by the implementing agent reading the code, not by any test.

Candidate rule: a slice that adds a bridge lists every reader of the old relation (found by searching the code for it, not from the plan), and the slice that removes the bridge is blocked by a slice for each reader not yet moved. Breaking it into issues is where the list is cheapest to make.
