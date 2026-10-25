---
address: guides/web-apps.md
origin: samthorold/go-slow#73
signal: gap
---

A collector that fetches a feed conditionally (ETag / Last-Modified) and then fetches each new entry's detail must not save the feed's validators for a run in which any entry was skipped because its detail fetch failed. Otherwise the next run gets a 304, and the skipped entries are never seen again.

Any project that collects feeds politely and enriches entries would hit this. No Guide covers collecting from third-party sources yet, so this is addressed to the nearest.
