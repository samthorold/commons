---
address: guides/web-apps.md#storage
origin: samthorold/go-slow#48
signal: trap
---

SQLite can't alter a CHECK constraint in place, so widening one means rebuilding the table (create new, copy, drop old, rename). With foreign keys on, `ALTER TABLE … RENAME` rewrites other tables' references to the old name, even with `legacy_alter_table` on, and the drop then fails. Foreign keys have to be turned off on the same connection, outside the migration's transaction (`PRAGMA foreign_keys` is a no-op inside one), with a `PRAGMA foreign_key_check` before committing. A migration runner that uses a connection pool or wraps every migration in a transaction can't do this until it is changed to. Any Adopter on SQLite (the Guide's default store) will hit it the first time a CHECK changes.
