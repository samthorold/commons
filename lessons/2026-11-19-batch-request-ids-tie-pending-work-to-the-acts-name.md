---
address: guides/model-calls.md#known-traps
origin: samthorold/go-slow#349
signal: trap
---

When a batch's request IDs are built from the act's name (`<act>-<hash of the work's key>`) and pending work is recognised by matching those stored IDs, renaming an act, or changing how IDs are built, makes work already in a batch at the provider look new. The next run then submits it again, as a second paid call, and the old batch's results arrive for work that has been sent twice. Recognise pending work by the act and the work's key (deriving the ID from them at the time of comparison), and keep matching results by the stored ID, so a batch sent under the old name still applies when it ends.
