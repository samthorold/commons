# Web apps Guide: htmx is required

How to apply the Stance *htmx is required*, from [the Web apps Guide](../web-apps.md#stance-htmx-is-required), which states the Stance.

## Why, in full

The htmx authors leave progressive enhancement to the developer, to be settled before the app is begun, because keeping non-JS clients working costs extra work in every command (*HS* 5). Building every command to render two ways (a swapped fragment and a redirected full page) is that cost, bought for users who run without JavaScript, and the owner's apps don't have them.

## How to apply

- routes use real HTTP verbs (`PUT`, `DELETE`), since htmx sends them. Pages stay real, bookmarkable URLs: a single shell that only ever swaps fragments would rebuild routing and history on the client (*HS* 1 advises against it).
