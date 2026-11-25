---
address: guides/emergent-systems/substrate-is-part-of-the-end-state.md
origin: samthorold/explorers#905
signal: gap
---

A property that checks a conservation floor ("no store goes negative") on an aggregate, such as the total of a pool across cells, can't see a breach in one store: one cell can be overdrawn while the total stays positive. Here the property passed on totals for months while proportional f32 splits overdrew individual cells and carcasses by a few ulps; checking every store found a second source of the same bug in another flow. Floors are checked per store; totals are only for closure (sum in equals sum out, within the closure's tolerance). And a floor has no tolerance: a share is capped at what its store holds, so rounding never draws below zero, and the cap changes nothing, bit for bit, wherever the store covers the share.
