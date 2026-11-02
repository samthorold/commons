# Agentic development Guide: agents implement test-first

How to apply the Stance *agents implement test-first*, from [the Agentic development Guide](../agentic-development.md#stance-agents-implement-test-first), which states the Stance.

## Why, in full

An agent working unattended needs an objective signal of done that it didn't shape to fit its own code. A test written before the code pins down the intended behaviour while the agent still only knows the intent; tests written after tend to describe whatever got built, bugs included. Small red-green steps also keep each change small enough to diagnose when it goes wrong, and leave a suite that lets the next agent change the code safely.

## How to apply

- for every feature or bug fix, whether in a Skill-driven run (e.g. `grind-issues`) or not. A bug fix starts with a test that reproduces it. Where the Archetype makes exact assertions hard (stochastic simulations, search), test properties, invariants or seeded runs rather than skipping the test.
