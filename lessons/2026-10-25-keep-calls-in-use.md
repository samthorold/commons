---
address: guides/model-calls.md
origin: samthorold/go-slow#63
signal: gap
---

The Guide covers how an act is tested (fakes, recordings, readings) but not what the running app keeps of its own model calls. An app whose judgement is read in use (feedback says *this is wrong*) needs to see why the act judged as it did, and only the request as sent answers that: inputs assembled at run time (precedents, candidates drawn from the app's store as it stood) are reproduced by no commit. A Stance candidate: keep every call in use, request as sent and response as returned (thinking, refusals and check-refused answers included), for good and never rewritten, as a side record no act is ever shown (an act shown its own earlier answers takes instructions by another route). Give each kept call the same request hash recordings carry, so "the same request" means one thing in use and in the suite, and a call that went wrong is already a fixture's input where the material is admissible. Link each output to the call that made it, since diagnosis starts from the feedback, upstream of the final output.

Learned in building it (samthorold/go-slow#80): linking an output to its kept call by matching time and work key breaks when one run handles many pieces of work at the same moment. Keep the call's id with the output, or keep which piece of work produced it.
