---
address: guides/agentic-development.md#known-traps
origin: samthorold/explorers@1473eee:docs/agents/instrument-runtimes.md
signal: trap
---

A background run that lasts hours on a macOS laptop stalls when the machine sleeps, and the stall looks like a hang. The process is paused, and `Instant` stops too, so a run budget never fires. `caffeinate -i` stops only idle sleep, not system or lid sleep: a sweep run under it overnight made almost no progress. `caffeinate -s` holds the system awake, but only on AC power; on battery it does nothing more than `-i`, and a run there took 2.4–2.7 times its CPU time in wall-clock. What works for an unattended run is `caffeinate -s -w <pid>`, on mains power with the lid open. Before suspecting a hang, check `ps -o cputime,etime` and `pmset -g log`. A run that was already stalled loses no work: `kill -STOP` its processes and `kill -CONT` them later. Its wall-clock is then meaningless, so report CPU time (`user` + `sys`) as its cost. Keeping the machine awake is the owner's call, so ask before starting a long run, and say whether it needs mains power.
