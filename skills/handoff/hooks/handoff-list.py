#!/usr/bin/env python3
"""SessionStart hook (after /clear): list recent handoff docs by name and age.

Prints the list as additional context, without the files' contents, and asks
Claude to offer them to the user before reading any. Prints nothing when there
are none.
"""

import json
import os
import subprocess
import time
from pathlib import Path

MAX_AGE_DAYS = 7
MAX_FILES = 10


def temp_dirs() -> list[Path]:
    dirs = [os.environ.get("TMPDIR", ""), "/tmp"]
    try:
        dirs.append(
            subprocess.run(
                ["getconf", "DARWIN_USER_TEMP_DIR"],
                capture_output=True,
                text=True,
                check=False,
            ).stdout.strip()
        )
    except OSError:
        pass
    seen: set[Path] = set()
    out: list[Path] = []
    for d in dirs:
        if d and (p := Path(d).resolve()).is_dir() and p not in seen:
            seen.add(p)
            out.append(p)
    return out


def age(seconds: float) -> str:
    minutes = int(seconds // 60)
    if minutes < 60:
        return f"{minutes} min ago"
    hours = minutes // 60
    if hours < 48:
        return f"{hours} h ago"
    return f"{hours // 24} days ago"


def main() -> None:
    now = time.time()
    found: list[tuple[float, Path]] = []
    for d in temp_dirs():
        for f in d.glob("handoff-*.md"):
            mtime = f.stat().st_mtime
            if now - mtime <= MAX_AGE_DAYS * 86400:
                found.append((mtime, f))
    if not found:
        return
    found.sort(reverse=True)
    lines = [
        f"- {f} (modified {time.strftime('%Y-%m-%d %H:%M', time.localtime(m))}, {age(now - m)})"
        for m, f in found[:MAX_FILES]
    ]
    context = (
        "Handoff documents from earlier sessions were found (newest first):\n"
        + "\n".join(lines)
        + "\n\nBefore doing anything else in your first reply, judging only from the names "
        "and times (do not read any of them yet), say which of these, if any, looks like "
        "it continues the user's work here, and ask whether to read it. Read a handoff only "
        "after the user says yes; if they say none applies, carry on without them."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }
        )
    )


main()
