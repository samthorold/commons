---
address: guides/web-apps/storage.md
origin: samthorold/go-slow#286
signal: gap
---

"Tests run against the real store while it's cheap" holds only while opening a fresh store is cheap, and applying every migration to each test's fresh SQLite file stops being cheap as migrations accumulate. With a pure-Go SQLite driver under a race detector, applying some thirty migrations took about a second per fresh database. A suite that opens one per test paid that hundreds of times: about 90% of one package's test time, and a large share of the rest. The fix keeps the real store: migrate one file once per test binary, close it (which checkpoints the WAL; check the `-wal` file is gone), and give each test its own copy of that file. Each test still gets an independent, fully migrated Record. An in-memory adapter isn't needed. The Convention could say so: tests copy a store migrated once, rather than migrating one per test.
