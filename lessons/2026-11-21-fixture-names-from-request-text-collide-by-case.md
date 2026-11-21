---
address: guides/global/written-files.md
origin: samthorold/go-slow#376
signal: trap
---

A recorder that names its fixture files after request text (a search's words, a URL path) must make the names unique without relying on case. Two requests differing only in case ("UK government", "UK Government") map to two names that macOS's case-insensitive filesystem stores as one file: the second answer overwrites the first, the replay passes locally, and only CI on Linux finds the missing file. Path separators in the text need escaping for the same reason. Make the name unique by construction (a short hash of the exact text beside a readable slug) and add a check that each kept file answers the request its name says, which fails on macOS too.
