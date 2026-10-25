---
address: (missing Guide: Go)
origin: samthorold/go-slow#47 (PR #54)
signal: trap
---

A JSON Schema built as a Go `map[string]any` is marshalled with its properties in alphabetical order, and a model generating structured output tends to write the fields in schema order. The order in which a model writes fields is then decided by their names, not by the design. In the origin, `claims` came before the `entities` list that the claims referred to, which made dangling references more likely. Where generation order matters, build the schema with an ordered type, or shape it so order can't matter (e.g. inline the referenced objects instead of referring by name).
