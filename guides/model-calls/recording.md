# Model calls Guide: a recording answers exactly one request

How to apply the Stance *a recording answers exactly one request*, from [the Model calls Guide](../model-calls.md#stance-a-recording-answers-exactly-one-request), which states the Stance and why.

- Keep a hash of the request as sent (instructions, schema, input, model, and in a conversation the model's earlier turns in the form the provider returned them) with each recording, and keep in the recording whatever is needed to rebuild it. Fail the replay as stale on a mismatch. Fail, don't skip: a skipped property quietly tests nothing.
- Acts that feed each other (one act's output is the next one's input) record in sequence and stop at the first failure. Otherwise one failed call moves every later call onto a request no recording holds.
- Fixtures that build on each other (each one's work changes the state the next is run over) carry each earlier fixture forward by one sample chosen before its results are seen (its first), and every sample of a later fixture runs over a copy of that state. Otherwise each sample answers a different request.
- A call that brings back no answer while recording (a transport error, the provider overloaded) is not a sample: retry it, or stop without keeping it. An answer that came back counts, even one returned as an error (the model refusing, an answer cut off), since that is the act's behaviour on its request.
- Write each recording as soon as it arrives, or check its destination before the first call: a harness that writes only at the end loses a paid run when the write fails.
- A recording of a tool-using act keeps, beside each turn, what the tools returned and the outcome (continued, refused with the reason told back, applied). The replay doesn't need it; whoever compares two recordings does.
