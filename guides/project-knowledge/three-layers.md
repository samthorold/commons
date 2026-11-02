# Project knowledge Guide: three layers, written in one language

How to apply the Stance *three layers, written in one language*, from [the Project knowledge Guide](../project-knowledge.md#stance-three-layers-written-in-one-language), which states the Stance.

## Why, in full

Each layer changes for a different reason (the world is understood better; the model changes; the code is refactored), so mixing them makes every change touch everything. A shared language keeps the layers, the issues, the tests and the conversation saying the same thing.

## How to apply

- Work at one layer at a time, and write each fact once, at its layer, referencing the others rather than restating them. Create files lazily, only when there is something to write, and conform to the layout a repo already has. The `grill-with-docs` Skill is the Procedure that writes these layers; its `CONTEXT-FORMAT.md` and `SYSTEM-DESIGN-FORMAT.md` are the formats.
