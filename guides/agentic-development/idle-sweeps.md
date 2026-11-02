# Agentic development Guide: idle sweeps

The Conventions for an agent's idle sweep, from [the Agentic development Guide](../agentic-development.md#idle-sweeps), which says when to read them.

- **An agent waiting on a background process does one slice of the sweep** (`CONTEXT.md`, *Sweep*): while it watches CI, a long test run or reading, or a Monitor, with nothing else of its own to do. A wait expected to last only a minute or two gets none. *Why:* the wait costs nothing, and between scheduled sweeps traps and Local copies outlive their need, costing context in every session.
- **One slice is one item**, the first not already reported: a Lesson in the inbox, a Known trap's *remove when*, or one of the current repo's agent docs (`CLAUDE.md` and what it points to) against its Guides, for Local copies of what a Guide now holds and for Drift. It is read-only, so it can be dropped the moment the wait ends with nothing half-done.
- **It reports and changes nothing.** Findings go in the agent's next status to the owner and as a comment on the recurring sweep's issue, where the next sweep acts on them; a sub-agent reports to whoever launched it. *Why:* the agent is mid-task in another piece of work, and which calls aren't an agent's to make is not yet settled (see *decide, record, carry on*).
- **What would change our mind:** reports that pile up unread, or items an agent could have resolved safely that keep waiting for the next sweep. Then some items move to being resolved in place.
