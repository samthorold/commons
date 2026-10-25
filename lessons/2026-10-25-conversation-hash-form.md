---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#85
signal: gap
---

The Stance says to keep a hash of each recording's request (instructions, schema, input, model). For a tool-using conversation, it doesn't say which form of the model's earlier turns goes into the hash.

If the provider's opaque raw form is hashed, and the recording keeps only a provider-neutral form, the replay can never rebuild the hash. And where kept calls in use hash one form while recordings hash another, "the same request" no longer means one thing in use and in the suite.

Candidate rule: hash the form both sides keep, and keep in a recording every form the hash covers.
