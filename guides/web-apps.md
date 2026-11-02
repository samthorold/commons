# Web apps Guide

**Scope:** Archetype = web apps, any Stack. A web app is an application people use through a browser, served by the project itself. A service with only a JSON API is not one; it would be its own Archetype.

The Stack's Guide covers tooling; this Guide covers the shape of the app: how it runs and is configured, its layers, its hypermedia UI, its storage and how it's tested.

The hypermedia Stances follow the htmx authors' book, *Hypermedia Systems* (Gross, Stepinski, Akşimşek, https://hypermedia.systems/book/contents/), cited as *HS* with its chapter. The book targets htmx 1.9; where this Guide departs from it, it says so and why. This Guide is written against **htmx 2**, and several specifics below (configuring `responseHandling`) are htmx 2 behaviour: an Adopter on another major records it as a Deviation.

Each Stance's *How to apply* and the full text of its Why, and the Conventions for one job, live in their own files under `~/.claude/commons/guides/web-apps/`, and this Guide says when to read each. Links are relative to this file.

## Stance: twelve-factor, wired in `main`

- **Stance:** the app is a twelve-factor app (https://12factor.net). Whatever varies between deploys (the database URL, the port, credentials) comes from environment variables, read once at the entry point into a typed config. `main` is the composition root: it reads the config, builds the adapters and passes them to the app's constructor, which takes its dependencies and reads nothing from the environment itself. No app factory that picks a named config ("development", "testing"), and no named environments.
- **Why:** an app built from its dependencies is tested by building it with the ones the test wants, with nothing to patch.
- **How to apply:** before adding config, a backing service, logging, a process's start or shutdown, or an admin task such as a migration, or setting up docker-compose or `.env.example`, read [twelve-factor](web-apps/twelve-factor.md).
- **What would change our mind:** config too structured for flat variables (many nested per-tenant settings), or a deploy target that can't supply an environment.

## Stance: ports and adapters, with DDD only where it earns its keep

- **Stance:** the code is layered as ports and adapters (onion). The **domain** holds entities, value objects, domain services and the repository **ports** (interfaces), with no HTTP and no SQL. The **application** layer holds the use cases: command handlers and query handlers. **Adapters** sit at the rim: the web adapter (handlers and templates), storage adapters, loaders. The full domain-model treatment (aggregates, invariants enforced in the model) goes only where there are real invariants or rich logic; the rest is thin CRUD. That boundary is movable: a concept is promoted into the domain once it grows real rules.
- **Why:** the logic worth having is where the app's value is, and it has to be testable without a browser or a database.
- **How to apply:** before adding a concept, a repository, a use case or a query, deciding what a template renders, or keeping a record of judgements, read [ports and adapters](web-apps/ports-and-adapters.md).
- **What would change our mind:** apps that stay pure CRUD for their whole life, where the layers cost more than they protect.

## Stance: the server owns the markup and the state

- **Stance:** the app is hypermedia-driven (htmx): every screen is HTML the server renders, and every change to what a user sees is the server returning HTML to swap in. The HTML is the app's API, and it is **specific to this UI**: endpoints are shaped for the screen they serve and refactored freely, unversioned and undocumented (*HS* 10, 12). There is no JSON API for the browser and no client-side application state. If another client (a script, a partner, a native app) needs data, it gets its own versioned JSON API under its own root (`/api/v1/...`), and the hypermedia routes aren't bent to serve it.
- **Why:** the logic and the data are on the server; a client that rebuilds views from JSON duplicates that logic in a second source of truth that drifts.
- **How to apply:** before serving JSON, adding a modal, dropdown or other client-side component, or giving one part of the UI client-side reactivity, read [the server owns the markup](web-apps/server-owns-the-markup.md).
- **What would change our mind:** an interaction that needs latency or offline behaviour HTML over the wire can't give (live drawing, offline capture, a spreadsheet where one edit cascades everywhere: *HS* 1, 11). If that is most of the app rather than an island, hypermedia is the wrong fit.

## Stance: htmx is required

- **Stance:** the app requires its hypermedia runtime. Navigation is full pages, boosted (`hx-boost` on the body); interactivity is partial swaps of them. Core flows are not also built as no-JS form posts.
- **Why:** keeping non-JS clients working costs extra work in every command (*HS* 5), for users the owner's apps don't have.
- **How to apply:** before choosing a route's HTTP verb, or making navigation swap fragments into one shell instead of loading pages, read [htmx is required](web-apps/htmx-is-required.md).
- **What would change our mind:** an app whose audience may run without JavaScript (public, accessibility-led, unknown devices). It builds Web 1.0 first and enhances, and its design doc says so.

## Stance: scripting is hypermedia-friendly

- **Stance:** scripting is for interaction design only, never business or presentation logic, and it follows the authors' rules for hypermedia-friendly scripting (*HS* 9): the server exchange stays hypermedia, UI state lives in the DOM (an attribute such as `hidden`, not a JavaScript variable), and pieces talk through events rather than callbacks. Behaviour is invoked where it's used (Locality of Behaviour). The default is plain JavaScript with no build step: one behaviour per file, attached by a `data-` attribute and initialised on `htmx:load` so swapped-in content gets it too.
- **Why:** the goal is less code, not less JavaScript (*HS* 9); state kept outside the DOM is lost or contradicted by the next swap.
- **How to apply:** before adding a third-party widget, a scripting library (Alpine, _hyperscript) or ARIA to a widget, read [scripting](web-apps/scripting.md).
- **What would change our mind:** behaviours that keep needing state the DOM can't hold, which is the island case under *the server owns the markup*.

## Responses and routing

Before adding or changing a route, a handler's response, or a template's markup or `hx-*` attributes, read [responses and routing](web-apps/responses-and-routing.md). It decides that each URL answers one shape (a page or a fragment), the routes and status codes for pages, fragments and commands, and how swaps, failed forms, waits, htmx itself and user content are handled.

## Storage

Before choosing the store, writing a migration, or deciding what store tests run against, read [storage](web-apps/storage.md). It decides SQLite until something needs Postgres, how a SQLite migration rebuilds a table, and when the repository ports earn an in-memory adapter.

## Testing

How web apps carry out the Agentic development Guide's test-first Stance. The book is silent on testing beyond accessibility; this is ours.

- **The hypermedia API is the public interface.** End-to-end tests build the app through its constructor (*twelve-factor*, above) with the adapters they want, and drive it the way a browser does, through the framework's test client: status codes, redirects, headers and the returned HTML. Domain logic and use cases are tested directly, without HTTP.
- **Replace only boundaries, by injection.** A fake stands in for what the app doesn't own (a third-party API, the clock) and is passed in through the constructor; nothing is patched, and the app's own layers are never mocked.
- **Time is a parameter.** The domain never reads the clock: use cases are told the time, handlers pass the current time, and tests pass the times they need. Waiting is time too: code that waits (backoff, a rate limit, an in-process timetable) takes its sleep and its ticks as parameters (a `sleep(ctx, d)` function, a channel of ticks), so a test neither really sleeps nor races on cancellation. A fake that replays recorded responses is built with a sleep that returns at once, and its recorder keeps the headers the client acts on (`Retry-After`): a recording can hold the service's backoff answers, and replayed with a real sleep each one is a real wait.
- **Timetables that feed each other start in order.** When one in-process timetable reads what another writes (a daily summary over what a collection loop stores), the order they start in is part of the design: start the reader once the writer's first run has ended, and test it. *Why:* both start with the process, and left to which thread wins, the reader's first run works on what the writer hasn't stored yet.
- **A headless screenshot passes `--virtual-time-budget` and `--timeout`** (Chromium's `--headless --screenshot`, for a PR's screenshots). *Why:* without them, a page carrying an htmx poll (`hx-trigger="every …"`) can keep the browser waiting forever; the two flags bound the wait, so the shot is taken.

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another web app would also hit), record a Lesson addressed to this Guide (to the detail file, where the Lesson is about how to apply a Stance or a job's Conventions), as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one app stays in that app's own docs.
