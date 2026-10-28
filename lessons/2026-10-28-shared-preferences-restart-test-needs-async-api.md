---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: trap
---

A port test that an adapter over `shared_preferences` "survives a restart" can pass without ever re-reading storage if it uses `SharedPreferences.getInstance()` with `setMockInitialValues`: that API hands back a cached singleton. Use `SharedPreferencesAsync`, which caches nothing, against `InMemorySharedPreferencesAsync` from `shared_preferences_platform_interface` (a dev dependency), and build a fresh adapter for the "after restart" half.
