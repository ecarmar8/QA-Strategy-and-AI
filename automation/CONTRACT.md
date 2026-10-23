# Local verification contract · version 1.0

The loopback-only target verifies the framework itself. Its routes, rules and credentials are authored test-support behavior, not assumptions about an external product. Each test has a unique workspace and cleans its created records.

- UI `/`: labelled record creation form, announced errors/results, persisted listing and completion.
- `GET /health`: target/version identity.
- `/api/records`: synthetic `Bearer qa-local-contract` authentication plus `x-workspace-id`. The token is a public local-only fixture, not a real credential.
- POST: trimmed name length 1–80; 201 plus `{id,name,status:'open'}`. Invalid input 400 and no effect.
- GET list/item: workspace-scoped records; unknown/cross-workspace item 404; unauthenticated access 401.
- PATCH item: status `open` or `completed`; invalid value 400 without changing persisted state.
- DELETE item: 204, then GET returns 404.
- Idempotency-Key: same key/name returns the same record, 200 on replay; changed payload 409.
- Local-only fault header `x-qa-fault: throttle-once`: first valid creation per workspace returns 429 and Retry-After 0 without an effect. The client test uses one bounded retry and verifies one persisted record.
- Page responses set Cache-Control no-store and X-Content-Type-Options nosniff.
- Automated accessibility baseline: configured axe WCAG A/AA rules plus a separate keyboard check. This is not a claim of full conformance or security certification.

UI/API tests execute actual HTTP/browser assertions against this target. Extending to a real product requires its actual routes, contracts, data, identities, locators and expected results; change its adapter/specifications rather than replacing a URL and assuming these rules apply.
