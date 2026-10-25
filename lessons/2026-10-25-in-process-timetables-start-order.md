---
address: guides/web-apps.md#testing
origin: samthorold/go-slow#84
signal: gap
---

The Guide says waiting is time too: a timetable takes its ticks as parameters. It doesn't say that when one in-process timetable reads what another writes, the order they start in is part of the design.

The case: a daily-output schedule and a collection loop, both started at process start. Both fired at once, so the schedule wrote the day's output from yesterday's data before the first collection had stored anything.

The fix there was to start the reader only after the writer's first run ends. Whatever the fix, the dependency between loops should be explicit and tested, not left to which goroutine or thread wins.
