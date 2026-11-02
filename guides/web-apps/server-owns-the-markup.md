# Web apps Guide: the server owns the markup and the state

How to apply the Stance *the server owns the markup and the state*, from [the Web apps Guide](../web-apps.md#stance-the-server-owns-the-markup-and-the-state), which states the Stance.

## Why, in full

The logic and the data are on the server. Each response carries the controls for what the user can do next (HATEOAS: an archived item shows *Unarchive*), so the client knows nothing of the domain and needs no versioning (*HS* 2). A client that rebuilds views from JSON duplicates that logic and creates a second source of truth that drifts. A data API and a hypermedia API want opposite things (stable, general and versioned against specific and churning), so one API serving both is under constant pressure from the UI (*HS* 10).

## How to apply

- Never serve HTML and JSON from the same URL by `Accept`: they differ in shape, error handling and authentication (*HS* 10). Never parse the app's own HTML as data.
- No client-side UI components (modals, dropdowns) with their own state: interactivity is a server-rendered fragment swapped in. Prefer an inline edit or a separate page to a modal; a modal is for an alert or a confirmation (*HS* 5).
- Spend the complexity budget on the app's real core and accept good-enough UX rather than reproducing an SPA's (*HS* 1, 13). Where one part genuinely needs client-side reactivity, it becomes an island of client code for that part only, and the rest stays hypermedia.
