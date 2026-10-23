---
name: connect-playwright-mcp
description: "Set up or verify a Playwright MCP connection, bind QA skills to real browser tools, and diagnose client, browser or target failures before live web testing."
---

# 34 · Connect Playwright MCP and bind QA skills

Version: 1.1 · Language: English · Role: Senior QA / QA Lead

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md). Treat installation, tool discovery, successful navigation and completed testing as separate milestones. This skill is a setup prerequisite for skill 20 when the chosen execution path is MCP; its number does not put setup after release.

## Inputs and prerequisites

- Chosen MCP client, operating system/runtime and workspace root.
- Node.js/npm/npx available in that same runtime; use Node.js 20 or newer for the documented setup.
- Existing server configuration, if any; do not add a duplicate Playwright entry blindly.
- Intended browser target and authorized read/test actions; legitimate sign-in if needed.
- QA case/source references and output location; no passwords or cookies in prompts.

## Procedure

1. Read [PLAYWRIGHT_MCP_SETUP.md](PLAYWRIGHT_MCP_SETUP.md) and inspect the actual client capabilities. Choose the MCP route explicitly. The optional Playwright CLI skill is a different route and is not required for MCP.
2. Verify `node --version`, `npm --version` and `npx --version` where the client starts its tools. A working Windows Node installation does not prove a WSL client can launch it correctly, or vice versa. Record the environment without exposing unrelated configuration/secrets.
3. Inspect any existing Playwright server. If missing and configuration is authorized, register the documented stdio server in the selected client. Keep it local and use an isolated browser profile for the starter demo. If installation is not authorized, return the precise proposed setup; do not claim it was installed.
4. Restart/reload the client as needed and inspect its MCP connection status and real exposed tool schemas. A saved config is not a successful connection. Tool names, prefixes, argument keys and optional capabilities can vary by installed version.
5. Build a capability map for navigation, current-page snapshot, input/click/keyboard, assertions/inspection and screenshot. Treat traces, video, network and arbitrary code execution as optional capabilities; do not assume they exist or enable broad execution merely for this demo.
6. For an authorized target, open the browser and inspect the real page snapshot. Use fresh references from the current page for subsequent actions. Re-snapshot after navigation or changes; never reuse element references from another MCP/CLI session.
7. For an attended demo, verify a visible browser window. MCP is headed by default in the documented setup; optional presentation pacing can use the configuration described in the setup guide. Fixed delays are not synchronization or proof of success.
8. Confirm the target/build, agreed expectations, data isolation and allowed mutations before handing off to skill 20. A connection exercise does not validate product behavior or grant external-system access.
9. Capture a connection receipt. On failure, distinguish missing executable/PATH, package retrieval, MCP startup/tool listing, browser launch, target reachability, authentication and business assertion failure. Report the actual stage and suggested correction; do not manufacture a pass.

## Required output

| Milestone | Required record |
|---|---|
| Client/runtime | Client, workspace, OS/runtime, Node version if actually checked |
| Server | Entry name, package/version when reported, transport and sanitized args |
| Connection | Configured / Connected / Tools verified / Blocked, with actual evidence |
| Capabilities | Real tool name, purpose and schema reference; optional missing features |
| Browser | Headed/hidden/unknown, isolated profile status, browser/version if observed |
| Target | URL/build if known, scope and navigation/snapshot evidence |
| Handoff | Ready for scoped execution or exact blockers; no test pass implied |

Keep secrets and session state out of the receipt. Do not dump complete MCP/client configuration if it includes other services or credentials.

## Missing input and stopping behavior

If the current LLM has no MCP host or local tool capability, produce the setup instructions for the user's chosen client and keep connection Unverified. If tools connect but target access fails, record target readiness Blocked while preserving the successful connection milestone. If only an optional trace tool is absent, explain the evidence limitation and continue with sufficient approved evidence.

## Quality checks and boundaries

- Verify real connection and tool output before saying Connected.
- Use credentials only through approved secure sign-in; do not bypass MFA.
- Standard Playwright browser control does not automate every native desktop client.
- Do not equate browser interaction with an installed regression suite or Playwright Test HTML report.
- Do not claim this chat or the user's machine was configured by reading this file.
- Apply skill 32 before publication and reuse existing authorization without repeated questions.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

Use [20-execute-web-tests-with-playwright.md](20-execute-web-tests-with-playwright.md) for actual web execution, and skills 26–28 for the evidence-based report. Save a checkpoint with the connection receipt and remaining prerequisites.
