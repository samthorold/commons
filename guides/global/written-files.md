# Files a program writes and checks back

Detail for the [Global Guide](../global.md). Read when writing a program that writes files it, or a test, later checks back (recorded fixtures, generated files, snapshots).

- **Files a program writes and checks back are written as the hooks would leave them** (recorded fixtures, generated files: ending in a newline, no trailing whitespace). *Why:* otherwise a hook rewrites the file on commit, and anything that hashes it, compares it byte for byte or checks it is unchanged breaks. Fix the writer; excluding the files from the hooks is the fallback.
