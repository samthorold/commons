---
address: guides/model-calls/kept-calls.md
origin: samthorold/go-slow#335
signal: gap
---

The kept-calls Stance says a kept call is kept "for good and never rewritten" and names the output's judge (the act, its instructions' version, the model, the request's hash), but it doesn't say what renaming an act does to the calls already kept under the old name. An act's name usually isn't part of its request: the model is never shown it, and a request hash over instructions, input, schema, model and effort leaves it out. So a rename makes no recording stale, and the only trace of the old name is the label on kept calls, judgements, work and pending batches. The choice is to relabel those in a migration, or to keep the old name readable as an alias for good. An Adopter early in its life, with no need for a backwards-compatible record, relabelled them in a migration. Read literally, "never rewritten" forbids that, though what it protects is the request and response as sent, and those don't change. The Stance could say which it means: the request and response are never rewritten, while the judge's label may be migrated (or must be aliased).
