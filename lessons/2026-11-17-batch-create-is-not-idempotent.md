---
address: guides/model-calls.md#known-traps
origin: samthorold/go-slow#303
signal: trap
waiting: confirming that a provider can accept a batch whose client then times out
---

Creating a message batch is not idempotent, but provider SDKs retry requests on timeout by default (the Anthropic SDKs: two retries). A large batch body (megabytes, which finer per-call units quickly reach) uploading slowly can time out on the client after the server has accepted it, and the retry submits a second, paid batch. An adapter that submits batches should set no retries on the create call (or make it idempotent some other way) and recover through its own record of pending batches. Unverified: whether the server can in fact accept a batch whose client then times out; the probe that found this avoided it by setting retries to zero.
