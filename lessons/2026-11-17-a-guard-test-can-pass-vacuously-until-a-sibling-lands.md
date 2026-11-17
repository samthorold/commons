---
address: guides/agentic-development/test-first.md
origin: samthorold/go-slow#315
signal: gap
---

A test that guards an absence ("no model call's input contains X") passes vacuously while the input it inspects can't contain X yet. Here a parallel slice hadn't yet made the input show the items X is attached to. Written test-first, the guard still never went red, because nothing could put X there. Once the sibling slice merged, the agent made the guard real by deliberately putting X into the input, watching the test fail, and reverting. That step also found a real defect (an empty title rendered where the newly shown items appeared). The Convention: a guard test of an absence must be shown to fail, by planting what it guards against, both when it is written and again when a slice that widens the guarded input lands.
