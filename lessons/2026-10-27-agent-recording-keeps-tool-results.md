---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#128
signal: gap
---

A recording of an act that is an agent with tools kept only the model's turns: its calls, its responses, the request hash and usage. It didn't keep the tool results the agent was shown, or the reason a submission was refused, although the app's own record of a live run keeps both. Replaying stayed exact, since the tools run again over the frozen inputs. But every before/after comparison in a PR ("which lookups now return nothing", "why was the first submission refused") needed a throwaway test that replayed the calls, written afresh each time. Twice in one day the agent reporting also first guessed wrong about what the file held.

How it would apply: a recording of a tool-using act keeps, beside each turn, what the tools returned and the outcome (continued, refused with the reason told back, applied). It is not used for replay; it is there so the recording can be read. Or, if keeping it costs too much, the repo keeps the replay-and-print helper as a dev tool, so a comparison is one command.
