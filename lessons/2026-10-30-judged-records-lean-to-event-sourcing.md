---
address: guides/web-apps.md#stance-ports-and-adapters-with-ddd-only-where-it-earns-its-keep
origin: samthorold/go-slow#208
signal: contradiction
---

The Guide's lightweight CQRS rules out event sourcing, but an app whose record is mostly a model's judgements may want it. Such an app needs to read its record *as it stood at a time*, and it needs that in three ways:

- work that runs on the record at a time;
- the owner's feedback, which is point in time;
- judgements by several judges (models, prompt versions) kept side by side, with a view choosing whose it reads.

Tables updated in place can't answer "as of t" or keep rival judgements without replaying a log. Keeping that log and deriving views from it is event sourcing. Configuration nobody judges (sources, preferences) can stay CRUD. Forgettable text under a source's terms is kept outside the stream. A working concept in the Origin, not yet built: promote once an Adopter has run on it.
