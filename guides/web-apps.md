# Web apps Guide

**Scope:** Archetype = web apps, any Stack. A web app is an application people use through a browser, served by the project itself. A service with only a JSON API is not one; it would be its own Archetype.

The Stack's Guide covers tooling; this Guide covers the shape of the app: its layers, its hypermedia UI, its storage and how it's tested.

## Stance: ports and adapters, with DDD only where it earns its keep

- **Stance:** the code is layered as ports and adapters (onion). The **domain** holds entities, value objects, domain services and the repository **ports** (interfaces), with no HTTP and no SQL. The **application** layer holds the use cases: command handlers and query handlers. **Adapters** sit at the rim: the web adapter (handlers and templates), storage adapters, loaders. The full domain-model treatment (aggregates, invariants enforced in the model) goes only where there are real invariants or rich logic; the rest is thin CRUD. That boundary is movable: a concept is promoted into the domain once it grows real rules.
- **Why:** the logic worth having is where the app's value is, and it has to be testable without a browser or a database. Dressing every table as an aggregate buys ceremony for concepts with no rules; leaving rich rules in handlers scatters them across adapters, where they drift.
- **How to apply:**
  - **One repository per aggregate root**, not per table.
  - **Lightweight CQRS:** commands go through the domain; queries return view-model DTOs and may read the store directly. Not event sourcing, not two databases.
  - Templates render **view models, never domain entities**.
  - Each design doc says which concepts are domain and which are CRUD today, and why.
- **What would change our mind:** apps that stay pure CRUD for their whole life, where the layers cost more than they protect.

## Stance: the server owns the markup and the state

- **Stance:** the app is hypermedia-driven (htmx): every screen is HTML the server renders, and every change to what a user sees is the server returning HTML to swap in. There is no JSON API for the browser and no client-side application state. If another client ever needs data, it gets its own versioned JSON API under its own root, and the hypermedia routes aren't bent to serve it.
- **Why:** the logic and the data are on the server. A client that rebuilds views from JSON duplicates that logic and creates a second source of truth that drifts from the first.
- **How to apply:** scripting is for interaction only, never business or presentation logic. No client-side UI components (modals, dropdowns) with their own state: interactivity is a server-rendered fragment swapped in. Prefer an inline edit or a separate page to a modal. The source is *Hypermedia Systems* (Gross, Stepinski, Akşimşek, https://hypermedia.systems).
- **What would change our mind:** an interaction that needs latency or offline behaviour HTML over the wire can't give (live drawing, offline capture).

## Stance: htmx is required

- **Stance:** the app requires its hypermedia runtime. Navigation is full pages, boosted (`hx-boost` on the body); interactivity is partial swaps of them. Core flows are not also built as no-JS form posts.
- **Why:** building every command to render two ways (a swapped fragment and a redirected full page) is ongoing complexity, bought for users who run without JavaScript, and the owner's apps don't have them.
- **How to apply:** routes use real HTTP verbs (`PUT`, `DELETE`), since htmx sends them. Pages stay real, bookmarkable URLs: a single shell that only ever swaps fragments would rebuild routing and history on the client.
- **What would change our mind:** an app whose audience may run without JavaScript (public, accessibility-led, unknown devices). It builds Web 1.0 first and enhances, and its design doc says so.

## Responses and routing

- **One URL, one response shape.** An endpoint returns either a full **page** (layout plus content) or a **fragment** (bare markup), never one or the other by reading `HX-Request`. A page is what a user can navigate to and bookmark; a fragment only fills a target inside a loaded page. *Why:* branching on request headers needs `Vary` and has to exclude boosted requests and history restores (both send `HX-Request: true`); each one missed swaps a fragment into the whole body.
- **Only page URLs enter history.** Never `hx-push-url` a fragment URL: going Back to it makes htmx refetch it as a history restore and swap it into the whole body.
- **Pages are REST nouns** (`GET /wines`, `GET /wines/{id}`); mutations use verbs on the resource (`POST /wines`, `PUT /wines/{id}`, `DELETE /wines/{id}`); fragment `GET`s are sub-resources named for what they fill (`GET /wines/{id}/edit`), with no `/partials/` prefix. A `GET` never mutates. A mutation that lands on a page answers `303 See Other`.
- **The unit of structure is the swap.** A piece of a page becomes its own component when a request swaps it on its own, or when it's reused; everything else stays inline. A swap target owns its `id` and its `hx-*` attributes and is rendered by one component, so first paint and re-render can't drift.
- **Always set `hx-target` and `hx-swap`.** To update more than one region: widen the target first; then an out-of-band swap per disconnected region; then server-triggered events (`HX-Trigger`).
- **A failed command re-renders its form.** HTML5 constraints are a courtesy; the domain is the authority. A validation failure answers `422` with the form re-rendered: entered values kept, errors in each field's slot, a form-level message for the rest. htmx doesn't swap `4xx` by default, so the layout configures `responseHandling` once to swap `422`.
- **htmx is vendored**, pinned by version in its file name (`htmx-2.0.11.min.js`), and configured once in the layout. *Why:* no runtime dependency on a CDN, and an upgrade is a visible change in a PR.
- **User content is inert.** Template autoescaping stays on, and free text a user typed is rendered inside an element carrying `hx-disable`, so injected `hx-*` attributes do nothing. Put it on the element holding the text, not on a container whose controls must still work.

## Storage

- **SQLite until something needs Postgres**: concurrent writers, an extension (e.g. pgvector), or several app instances. Then Postgres, with docker-compose running app and database for development.
- **Tests run against the real store while it's cheap**: a SQLite file in a temporary directory. When the store needs a container, the repository ports earn an **in-memory adapter** for unit tests, and integration tests drive the app against the real database, each test in a rolled-back transaction.

## Testing

How web apps carry out the Agentic development Guide's test-first Stance.

- **The hypermedia API is the public interface.** End-to-end tests drive the app the way a browser does, through the framework's test client: status codes, redirects, headers and the returned HTML. Domain logic and use cases are tested directly, without HTTP.
- **Time is a parameter.** The domain never reads the clock: use cases are told the time, handlers pass the current time, and tests pass the times they need.

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another web app would also hit), record a Lesson addressed to this Guide, as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one app stays in that app's own docs.
