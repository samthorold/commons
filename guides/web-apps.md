# Web apps Guide

**Scope:** Archetype = web apps, any Stack. A web app is an application people use through a browser, served by the project itself. A service with only a JSON API is not one; it would be its own Archetype.

The Stack's Guide covers tooling; this Guide covers the shape of the app: how it runs and is configured, its layers, its hypermedia UI, its storage and how it's tested.

The hypermedia Stances follow the htmx authors' book, *Hypermedia Systems* (Gross, Stepinski, Akşimşek, https://hypermedia.systems/book/contents/), cited as *HS* with its chapter. The book targets htmx 1.9; where this Guide departs from it, it says so and why. This Guide is written against **htmx 2**, and several specifics below (configuring `responseHandling`) are htmx 2 behaviour: an Adopter on another major records it as a Deviation.

## Stance: twelve-factor, wired in `main`

- **Stance:** the app is a twelve-factor app (https://12factor.net). Whatever varies between deploys (the database URL, the port, credentials) comes from environment variables, read once at the entry point into a typed config. `main` is the composition root: it reads the config, builds the adapters and passes them to the app's constructor, which takes its dependencies and reads nothing from the environment itself. No app factory that picks a named config ("development", "testing"), and no named environments.
- **Why:** an app constructed from its dependencies is tested by constructing it with the ones the test wants, with nothing to patch and no heavy mocking. A factory keyed on an environment name hides the wiring, and named environments multiply with every new deploy (12factor, *Config*). Config in the environment also keeps credentials out of the repo, so a repo can go public without a scrub.
- **How to apply:**
  - **Backing services are attached resources:** swapping the database for another instance is a change of config, never of code (12factor, *Backing services*).
  - **Dev/prod parity:** every deploy, the developer's included, uses the same backing services at the same versions (12factor, *Dev/prod parity*). docker-compose runs them locally, and runs the app from the same image with its environment set as in production. In-memory adapters are for tests, never a running app.
  - **Logs are an event stream:** written unbuffered to stdout, never to files the app manages.
  - **Disposable processes:** start in seconds; on SIGTERM stop accepting connections, finish in-flight requests, then exit.
  - **Admin tasks are one-off processes** from the same codebase and config: migrations and fix-up scripts are commands of the app (e.g. a subcommand of its binary), not separate tooling.
  - The repo carries a `.env.example` listing every variable with a safe local value; the real `.env` is gitignored.
- **What would change our mind:** config too structured for flat variables (many nested per-tenant settings), or a deploy target that can't supply an environment.

## Stance: ports and adapters, with DDD only where it earns its keep

- **Stance:** the code is layered as ports and adapters (onion). The **domain** holds entities, value objects, domain services and the repository **ports** (interfaces), with no HTTP and no SQL. The **application** layer holds the use cases: command handlers and query handlers. **Adapters** sit at the rim: the web adapter (handlers and templates), storage adapters, loaders. The full domain-model treatment (aggregates, invariants enforced in the model) goes only where there are real invariants or rich logic; the rest is thin CRUD. That boundary is movable: a concept is promoted into the domain once it grows real rules.
- **Why:** the logic worth having is where the app's value is, and it has to be testable without a browser or a database. Dressing every table as an aggregate buys ceremony for concepts with no rules; leaving rich rules in handlers scatters them across adapters, where they drift. The htmx authors' own shape is the same in MVC terms: thin controllers over a fat model, which is what lets a hypermedia API and a JSON API share one domain (*HS* 10).
- **How to apply:**
  - **One repository per aggregate root**, not per table.
  - **Lightweight CQRS:** commands go through the domain; queries return view-model DTOs and may read the store directly, with the joins and aggregates one screen needs. Not event sourcing, not two databases.
  - Templates render **view models, never domain entities**.
  - Each design doc says which concepts are domain and which are CRUD today, and why.
- **What would change our mind:** apps that stay pure CRUD for their whole life, where the layers cost more than they protect.

## Stance: the server owns the markup and the state

- **Stance:** the app is hypermedia-driven (htmx): every screen is HTML the server renders, and every change to what a user sees is the server returning HTML to swap in. The HTML is the app's API, and it is **specific to this UI**: endpoints are shaped for the screen they serve and refactored freely, unversioned and undocumented (*HS* 10, 12). There is no JSON API for the browser and no client-side application state. If another client (a script, a partner, a native app) needs data, it gets its own versioned JSON API under its own root (`/api/v1/...`), and the hypermedia routes aren't bent to serve it.
- **Why:** the logic and the data are on the server. Each response carries the controls for what the user can do next (HATEOAS: an archived item shows *Unarchive*), so the client knows nothing of the domain and needs no versioning (*HS* 2). A client that rebuilds views from JSON duplicates that logic and creates a second source of truth that drifts. A data API and a hypermedia API want opposite things (stable, general and versioned against specific and churning), so one API serving both is under constant pressure from the UI (*HS* 10).
- **How to apply:**
  - Never serve HTML and JSON from the same URL by `Accept`: they differ in shape, error handling and authentication (*HS* 10). Never parse the app's own HTML as data.
  - No client-side UI components (modals, dropdowns) with their own state: interactivity is a server-rendered fragment swapped in. Prefer an inline edit or a separate page to a modal; a modal is for an alert or a confirmation (*HS* 5).
  - Spend the complexity budget on the app's real core and accept good-enough UX rather than reproducing an SPA's (*HS* 1, 13). Where one part genuinely needs client-side reactivity, it becomes an island of client code for that part only, and the rest stays hypermedia.
- **What would change our mind:** an interaction that needs latency or offline behaviour HTML over the wire can't give (live drawing, offline capture, a spreadsheet where one edit cascades everywhere: *HS* 1, 11). If that is most of the app rather than an island, hypermedia is the wrong fit.

## Stance: htmx is required

- **Stance:** the app requires its hypermedia runtime. Navigation is full pages, boosted (`hx-boost` on the body); interactivity is partial swaps of them. Core flows are not also built as no-JS form posts.
- **Why:** the htmx authors leave progressive enhancement to the developer, to be settled before the app is begun, because keeping non-JS clients working costs extra work in every command (*HS* 5). Building every command to render two ways (a swapped fragment and a redirected full page) is that cost, bought for users who run without JavaScript, and the owner's apps don't have them.
- **How to apply:** routes use real HTTP verbs (`PUT`, `DELETE`), since htmx sends them. Pages stay real, bookmarkable URLs: a single shell that only ever swaps fragments would rebuild routing and history on the client (*HS* 1 advises against it).
- **What would change our mind:** an app whose audience may run without JavaScript (public, accessibility-led, unknown devices). It builds Web 1.0 first and enhances, and its design doc says so.

## Stance: scripting is hypermedia-friendly

- **Stance:** scripting is for interaction design only, never business or presentation logic, and it follows the authors' rules for hypermedia-friendly scripting (*HS* 9): the server exchange stays hypermedia, UI state lives in the DOM (an attribute such as `hidden`, not a JavaScript variable), and pieces talk through events rather than callbacks. Behaviour is invoked where it's used (Locality of Behaviour). The default is plain JavaScript with no build step: one behaviour per file, attached by a `data-` attribute and initialised on `htmx:load` so swapped-in content gets it too.
- **Why:** the goal is less code, not less JavaScript (*HS* 9). State kept outside the DOM is lost or contradicted by the next swap; a widget that needs a JSON endpoint quietly reintroduces the data API this Guide rules out.
- **How to apply:** a third-party widget must work on the DOM without a JSON endpoint; wrap a callback-style one so it dispatches an event, and let `hx-trigger` listen for it. Alpine or _hyperscript (the authors' own favourite) come in only when plain behaviours get unwieldy, and the app's design doc says so. For complex widgets use an established accessible library; no ARIA is better than bad ARIA.
- **What would change our mind:** behaviours that keep needing state the DOM can't hold, which is the island case under *the server owns the markup*.

## Responses and routing

- **One URL, one response shape.** An endpoint returns either a full **page** (layout plus content) or a **fragment** (bare markup), never one or the other by reading `HX-Request`. A page is what a user can navigate to and bookmark; a fragment only fills a target inside a loaded page. *Why:* the book branches on `HX-Request` and `HX-Trigger` (*HS* 2, 6), which needs `Vary` on every such header and has to exclude boosted requests and history restores (both send `HX-Request: true`); each one missed swaps a fragment into the whole body or serves it from a cache. A fragment with its own URL has none of those cases.
- **Only page URLs enter history.** Never `hx-push-url` a fragment URL: going Back or refreshing requests it without htmx, and gets a fragment where a page belongs (*HS* 4).
- **Pages are REST nouns** (`GET /wines`, `GET /wines/{id}`); mutations use verbs on the resource (`POST /wines`, `PUT /wines/{id}`, `DELETE /wines/{id}`); fragment `GET`s are sub-resources named for what they fill (`GET /wines/{id}/edit`), with no `/partials/` prefix. A `GET` never mutates. A mutation that lands on a page answers `303 See Other`: a `302` after `DELETE` or `PUT` keeps the method (*HS* 5).
- **A command issued from several pages has a route under each**, nested under that page's resource (`PUT /lists/{id}/items/{iid}/archived` beside `PUT /items/{iid}/archived`). Each answers `303` to its own page, and all call the same use case. *Why:* a single route has to guess where to return, from `Referer` or a hidden field, which brings back the request-dependent response that *one URL, one response shape* avoids. The duplication is only a thin handler.
- **Removing an element is `200` with an empty body**, swapped `outerHTML`. A `204` swaps nothing (*HS* 6, 8).
- **The unit of structure is the swap.** A piece of a page becomes its own component when a request swaps it on its own, or when it's reused; everything else stays inline. A swap target owns its `id` and its `hx-*` attributes and is rendered by one component, with all its states (empty, running, done) in it, so first paint and re-render can't drift (*HS* 6, 7).
- **Always set `hx-target` and `hx-swap`.** To update more than one region, in this order (*HS* 8): widen the target; then an out-of-band swap per disconnected region; then server-triggered events (`HX-Trigger`) that other regions listen for.
- **A failed command re-renders its form.** HTML5 constraints are a courtesy; the domain is the authority (*HS* 5). A validation failure answers `422` with the form re-rendered: entered values kept, errors in each field's slot, a form-level message for the rest. htmx doesn't swap `4xx` by default, so the layout configures `responseHandling` once to swap `422`. (The book leaves the status unstated.)
- **Every request a user waits on shows an indicator**; typing triggers are debounced (`keyup changed delay:…`); an expensive region loads lazily (`hx-trigger="load"` or `revealed`) on its own endpoint; a job that ends is polled by a fragment that re-polls only while running; destructive actions carry `hx-confirm`; competing requests are ordered with `hx-sync` (*HS* 5–8).
- **Downloads are not boosted:** `hx-boost="false"` on a link to a file, which an AJAX request can't save (*HS* 5, 7).
- **htmx is vendored**, pinned by version in its file name (`htmx-2.0.10.min.js`), and configured once in the layout. *Why:* no runtime dependency on a CDN, and an upgrade is a visible change in a PR (*HS* 4 offers both and leans the same way).
- **User content is inert.** Template autoescaping stays on, and free text a user typed is rendered inside an element carrying `hx-disable`, so injected `hx-*` attributes do nothing (*HS* 8). Put it on the element holding the text, not on a container whose controls must still work.

## Storage

- **SQLite until something needs Postgres**: concurrent writers, an extension (e.g. pgvector), or several app instances. Then Postgres, run locally by docker-compose (*twelve-factor*, above).
- **SQLite migrations can rebuild a table.** SQLite can't change a constraint (a `CHECK`) in place, so the change is a rebuild by SQLite's own procedure (https://www.sqlite.org/lang_altertable.html, *Making other kinds of table schema changes*): create `new_X`, copy, drop `X`, rename `new_X` to `X`, then `PRAGMA foreign_key_check` before committing. The migration runner makes that possible: each migration runs on one connection with `PRAGMA foreign_keys = OFF` set before its transaction begins (inside one the pragma does nothing). *Why:* with foreign keys on, dropping a table others refer to fails. And renaming the *old* table first, the order that looks natural, rewrites other tables' references to point at the temporary name. A runner that pools connections or opens each migration's transaction itself can't do this, and that is found only on the first `CHECK` that changes.
- **Tests run against the real store while it's cheap**: a SQLite file in a temporary directory. When the store needs a container, the repository ports earn an **in-memory adapter** for unit tests, and integration tests drive the app against the real database, each test in a rolled-back transaction.

## Testing

How web apps carry out the Agentic development Guide's test-first Stance. The book is silent on testing beyond accessibility; this is ours.

- **The hypermedia API is the public interface.** End-to-end tests build the app through its constructor (*twelve-factor*, above) with the adapters they want, and drive it the way a browser does, through the framework's test client: status codes, redirects, headers and the returned HTML. Domain logic and use cases are tested directly, without HTTP.
- **Replace only boundaries, by injection.** A fake stands in for what the app doesn't own (a third-party API, the clock) and is passed in through the constructor; nothing is patched, and the app's own layers are never mocked.
- **Time is a parameter.** The domain never reads the clock: use cases are told the time, handlers pass the current time, and tests pass the times they need. Waiting is time too: code that waits (backoff, a rate limit, an in-process timetable) takes its sleep and its ticks as parameters (a `sleep(ctx, d)` function, a channel of ticks), so a test neither really sleeps nor races on cancellation.
- **Timetables that feed each other start in order.** When one in-process timetable reads what another writes (a daily summary over what a collection loop stores), the order they start in is part of the design: start the reader once the writer's first run has ended, and test it. *Why:* both start with the process, and left to which thread wins, the reader's first run works on what the writer hasn't stored yet.

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another web app would also hit), record a Lesson addressed to this Guide, as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one app stays in that app's own docs.
