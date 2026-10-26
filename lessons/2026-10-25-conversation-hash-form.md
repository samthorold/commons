---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#85
signal: gap
---

The Stance says to keep a hash of each recording's request (instructions, schema, input, model). For a tool-using conversation, it doesn't say which form of the model's earlier turns goes into the hash.

If the provider's opaque raw form is hashed, and the recording keeps only a provider-neutral form, the replay can never rebuild the hash. And where kept calls in use hash one form while recordings hash another, "the same request" no longer means one thing in use and in the suite.

Candidate rule: hash the form both sides keep, and keep in a recording every form the hash covers.

Resolved in the origin (samthorold/go-slow#97) by keeping the provider form, not hashing the neutral one: a neutral hash would leave out what the provider is actually sent (thinking blocks passed back), and would change the meaning of every hash already kept in use. So the recording keeps each model turn as the provider returned it, and the hash is over the request exactly as sent. That suggests the candidate rule tightens to: hash the request as sent, and make the recording keep whatever is needed to rebuild it.
