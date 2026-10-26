---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#91
signal: gap
---

Instructions that describe a concept in words close to an output field's name act as instructions for that field. An extraction act's schema had an optional free-text `role` field, meant for a person's office. A new paragraph defined when an entity is involved in a statement "when it has a role in it". The model then filled `role` for organisations and places on 96–100% of mentions, against 4% before. Rewording the paragraph to avoid the word cut it to 54–84% but did not stop it.

Two things follow:

- **When comparing samples of a changed act, count every output field, not only the ones the change was aimed at.** The leak was only caught because the comparison also counted the role field.
- **When an output field must stay narrow and the instructions need nearby concepts, enforce the field's scope in code** (drop the value where it doesn't apply) rather than by more wording. Code leaves the request, and so every recording, unchanged.
