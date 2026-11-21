---
address: guides/model-calls/fixtures-and-properties.md
origin: samthorold/go-slow#363
signal: gap
---

When part of an act's input comes from a service that isn't a model and whose answers aren't recorded, the recordings often replace it with a stand-in that matches nothing, which keeps the replay deterministic. That stand-in can hollow out exactly what a slice adds. A slice gave a tool-using act a tool that finds records by entity; the recorded runs looked entities up in a stand-in that resolved no name, so a person named two ways was two entities, and most of the ten asks the model made found nothing. Every declared property was supported; only reading what the tool answered showed the tool had never been exercised in the case it exists for. When a slice adds or changes a tool, report beside the yield how often each tool was asked in the recordings and how often its answer held anything, and record the answers of any service the tool's answers depend on, rather than standing it in with one that matches nothing.
