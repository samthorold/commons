---
address: guides/global.md#known-traps
origin: samthorold/go-slow#97
signal: trap
---

An HTTP response recorded verbatim as a test fixture usually has no trailing newline, so the `end-of-file-fixer` pre-commit hook rewrites the file when it is committed. That is harmless for a fixture that is parsed, and it breaks one that is hashed or compared byte for byte, or a recorder that checks whether its file is unchanged. The fix is in the recorder: write the newline itself, so the committed fixture is what the recorder wrote. Excluding the fixtures from the hook also works, but leaves them inconsistent with the rest of the repo.
