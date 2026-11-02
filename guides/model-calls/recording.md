# Model calls Guide: a recording answers exactly one request

How to apply the Stance *a recording answers exactly one request*, from [the Model calls Guide](../model-calls.md#stance-a-recording-answers-exactly-one-request), which states the Stance.

## Why, in full

A replay that doesn't compare the request the code would send now stays green after the instructions, schema or model change, testing a prompt that no longer exists. And a sample is only a sample of the act if it answers the same request as the others: one drawn over a different prior state, or lost to the provider, measures something else.

## How to apply

- Keep a hash of the request as sent (instructions, schema, input, model, and in a conversation the model's earlier turns in the form the provider returned them) with each recording, and keep in the recording whatever is needed to rebuild it. Fail the replay as stale on a mismatch. Fail, don't skip: a skipped property quietly tests nothing.
- Acts that feed each other (one act's output is the next one's input) record in sequence and stop at the first failure. Otherwise one failed call moves every later call onto a request no recording holds.
- **Each act is recorded over its own frozen copies** of the upstream recordings, never over the upstream recordings themselves, so re-recording one act leaves every other act's recordings valid. Copies, not hand-made input: they were made by the production path, and hand-made input lets a downstream act pass on what no upstream act writes. A frozen copy is part of the downstream act's request, so it goes in the request hash. It is loaded as it was kept, not passed through the upstream act's current checks: the act that made it checked it then, and re-checking it would make a new upstream check fail acts it never touched.
- **Two checks cover the gap until a refresh**, with no recording of their own. A chain replay over the most downstream act's frozen copies, one consistent run, asserts only properties that span acts (an output traced back to its source). A compatibility check feeds each act's current recordings to the acts downstream on a fake model, so a change in the shape of an upstream output fails at once. A change in what an upstream act judges is not a code failure; the refresh brings it downstream ([changing an act](changing-an-act.md)).
- Fixtures that build on each other (each one's work changes the state the next is run over) carry each earlier fixture forward by one sample chosen before its results are seen (its first), and every sample of a later fixture runs over a copy of that state. Otherwise each sample answers a different request.
- A call that brings back no answer while recording (a transport error, the provider overloaded) is not a sample: retry it, or stop without keeping it. An answer that came back counts, even one returned as an error (the model refusing, an answer cut off), since that is the act's behaviour on its request.
- Write each recording as soon as it arrives, or check its destination before the first call: a harness that writes only at the end loses a paid run when the write fails.
- A recording of a tool-using act keeps, beside each turn, what the tools returned and the outcome (continued, refused with the reason told back, applied). The replay doesn't need it; whoever compares two recordings does.
