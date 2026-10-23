---
name: execute-web-tests-with-playwright
description: "Bind and execute approved web cases through actual Playwright MCP tools or an explicitly selected existing Playwright runner, with observed assertions and evidence."
---

# 20 · Execute web tests with Playwright

Version: 1.1 · Language: English · Role: Senior QA / QA Lead

## When to use

Bind and run approved web cases with an available Playwright environment.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Actual Playwright MCP connection or existing runner/project; authorized target/build; observed page/interface or existing locator bindings; confirmed cases, data and identities. An MCP interactive run does not require a new test-code project. Authentication state must be handled securely.

## Procedure

1. Select and record the execution path: Playwright MCP, existing Playwright Test runner, or separately configured Playwright CLI. For MCP, use [34-connect-playwright-mcp.md](34-connect-playwright-mcp.md) first. Discover the actual tools and schemas; an MCP prefix or parameter name may differ by client/version. Confirm target/build, browser, scope and case readiness. If tooling is absent, return exact prerequisites and keep cases Not Run.
2. Reuse approved authentication or supervised legitimate sign-in; never embed passwords or bypass MFA. Keep session state out of repository/report output and manage it as a secret.
3. Inspect actual elements. For MCP, use current accessibility snapshots and fresh element references accepted by the discovered tool schema; re-inspect after relevant changes. For a code runner, prefer observed roles, labels and supported test IDs with Playwright assertions/auto-waiting. Verify observable business outcomes through available assertions or state inspection. Do not guess selectors or equate an action's success response with a passed case. Never mix MCP and CLI element references/sessions.
4. For an attended walkthrough, verify a visible browser. MCP is headed by default in the documented setup; [PLAYWRIGHT_MCP_SETUP.md](PLAYWRIGHT_MCP_SETUP.md) describes optional `headless: false` / `slowMo: 1000` launch configuration. Pacing is not synchronization. CI may use headless mode in its authorized runtime.
5. Run scoped cases and collect per-attempt outcomes, actual observations and available sanitized screenshot/snapshot evidence. Record browser/build/correlation information when genuinely available, otherwise Unknown. Collect traces only if supported and actually produced. An interactive MCP session does not automatically generate a Playwright Test HTML report or install a regression suite. Skills 26–27 can produce a Markdown executive report from the actual run ledger. Validate financial/data effects through separately authorized interfaces where needed.
6. Diagnose test, environment and product failures. Preserve first failures through retries; inspect artifacts for sensitive data before sharing. Native desktop is out of scope for ordinary Playwright; Electron support is experimental and requires a separate compatibility decision.

## Required output

Playwright execution ledger: Case/test | Run/attempt | Build/browser | Locator binding reference | Result | Business assertion | Screenshot/trace reference | Defect/blocker | Cleanup.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No fake traces, generated selectors presented as observed, or green results from an unexecuted plan. If a test uses a mock provider, report that boundary.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: approved refund web case, actual role/label locators, ready sandbox. Output: observed assertions and evidence per run; if login blocks on MFA, hand off to user and mark execution Blocked until resolved.

## Handoff

Use [CTO_LIVE_DEMO.md](CTO_LIVE_DEMO.md) for the bounded three-case browser demonstration. Its report starts Not Run and is distinct from file 99's simulated payment outcomes.

22–24, 25 for CI, 26 for result aggregation.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
