# Playwright MCP setup — English quick start

**Goal:** let a local MCP-capable LLM client apply Edward's QA skills while controlling a visible browser. This guide configures existing tooling; it does not build a new QA application.

Contents: [Choose your route](#choose-your-route) · [Claude Code](#option-a--claude-code) · [Cursor](#option-b--cursor) · [Pacing](#optional-visible-pacing) · [Verify](#verify-the-connection-before-testing) · [Troubleshooting](#troubleshooting) · [CLI skills](#optional-official-playwright-cli-skill)

## Choose your route

| Layer | Responsibility | Installed/provided by |
|---|---|---|
| QA skill library | Business analysis, strategy, cases, oracles, defects and decisions | This ZIP |
| MCP host / LLM client | Loads skills and calls external tools | Your local Claude Code or Cursor installation/account |
| Playwright MCP server | Browser navigation, inspection and interaction | `@playwright/mcp` |
| Application under test | Actual behavior and data | Supplied demo URL or your authorized test environment |
| Optional Playwright CLI skill | Teaches a coding agent a separate shell-driven browser workflow | Official `@playwright/cli` installation |

Use **MCP + this QA library** for the first live demonstration. You do not need the optional CLI route, an Azure connection or a new test framework for that exercise. Installing the CLI skill alone does not connect an MCP server.

## Before you start

1. Extract this ZIP and open the folder containing this file as your local workspace.
2. Keep `.claude/skills/` and all root Markdown files together. See [SKILLS_INSTALLATION.md](SKILLS_INSTALLATION.md).
3. Use Node.js **20 or newer**, npm/npx, and an installed authenticated Claude Code or Cursor client. Their own installation/sign-in is separate from this bundle.
4. Check these commands in the same environment where the client will launch MCP:

```sh
node --version
npm --version
npx --version
```

For your Windows/WSL setup, choose one starting point. A native Windows client is convenient for a visible presentation browser. A WSL client needs Node, browser dependencies and a usable Linux display in its own environment. Do not assume Windows and WSL share PATH, browser installations, workspace paths or localhost networking. First prove the browser and target are reachable from the MCP runtime you selected.

## Option A — Claude Code

In a terminal opened in the extracted project folder, inspect existing servers:

```sh
claude mcp list
```

If no working Playwright entry exists, add one:

```sh
claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest --isolated
```

Then check and start a session:

```sh
claude mcp list
claude
```

Inside Claude Code, use `/mcp` to inspect the server and its actual tools. If an existing entry has different settings, inspect it with `claude mcp get playwright` before deciding to update it. Do not blindly register a second server or delete other servers.

The `add` command saves configuration; it does not prove browser launch. The final receipt must include a successful actual navigation/snapshot. The command uses local project context by default; it does not publish anything to GitHub. Client policy may require its normal first-use tool approval.

Official references: [Claude MCP](https://code.claude.com/docs/en/mcp) and [MCP quick start](https://code.claude.com/docs/en/mcp-quickstart).

## Option B — Cursor

Open the extracted folder in Cursor. Create or merge the following **entry** into `.cursor/mcp.json` at that workspace root. The ZIP remains Markdown-only; this is configuration you create in your client project. Preserve other existing entries.

```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--isolated"]
    }
  }
}
```

Reload or reconnect the entry as required by your Cursor version. Inspect the server's connection and tools in Cursor's MCP configuration interface. Use Agent mode to invoke browser tools. Do not infer connection success from a valid JSON file.

Official reference: [Cursor MCP configuration](https://cursor.com/docs/mcp). The same shared `mcpServers` shape appears in the [official Playwright MCP setup](https://playwright.dev/mcp/installation); other hosts may require their own configuration envelope.

## Optional visible pacing

The documented MCP default is headed; omit `--headless` for the presentation. To use Edward's preferred one-second pacing, create `playwright-mcp.config.json` in the workspace with this content:

```json
{
  "browser": {
    "isolated": true,
    "launchOptions": {
      "headless": false,
      "slowMo": 1000
    }
  }
}
```

Update the same server entry to pass `--config` followed by the **absolute path** to that file, replacing the simple `--isolated` argument. Example argument list, using your actual path:

```json
["-y", "@playwright/mcp@latest", "--config", "C:/QA/QA_Testing_Lifecycle_Skills_EN/playwright-mcp.config.json"]
```

Use a Linux absolute path if the server runs in WSL. The example path is illustrative; do not paste it unless it exists. `slowMo` affects presentation pacing, not assertion synchronization. Use snapshots, actual conditions and supported assertions for correctness. Consult the installed server's current configuration schema if it rejects an option. Source: [Playwright MCP configuration schema](https://github.com/microsoft/playwright-mcp#configuration-file).

## Verify the connection before testing

Paste into the LLM client:

> Use the connect-playwright-mcp procedure in file 34 and the shared contract. Discover the connected Playwright MCP server and list only its relevant browser capabilities, without dumping credentials or unrelated configuration. I authorize read-only navigation to https://demo.playwright.dev/todomvc/ for this connection check. Open a visible browser, inspect the actual current page snapshot, and return a receipt showing client, server status, target URL, observed page information and missing capabilities. Do not create, complete or delete items yet. If tools are unavailable, report the exact blocker; do not simulate success.

Expected deliverable: an **actual connection receipt**, or a specific blocker. No QA case becomes Passed merely because this check worked. Proceed to [CTO_LIVE_DEMO.md](CTO_LIVE_DEMO.md) only after the host actually exposes working browser tools.

## Troubleshooting

| Symptom | Check / next step |
|---|---|
| `node`, `npx` or client command not found | Confirm installation and PATH in the client's own runtime, then restart the client |
| Native Windows process cannot launch `npx` | Inspect the client error; if a shell wrapper is required, use `command: "cmd"` and args beginning `["/c", "npx", "-y", ...]` in that Windows entry |
| Package cannot download | Check npm registry/network/proxy access from the same runtime; record installation Blocked |
| Config saved, tools absent | Inspect MCP status/error and actual tools; reconnect/restart; do not proceed on the saved entry alone |
| Browser cannot launch | Use the server's supported browser-install capability or documented installation guidance; for WSL also check display/system dependencies |
| Browser opens but target cannot load | Check target reachability from that browser's runtime, including the correct host/port for local apps |
| Login/MFA required | Let the user complete the legitimate sign-in; no passwords in prompts or scripts |
| Existing profile locked | Use an isolated profile for the demo; do not terminate unrelated browser processes |
| Screenshot/trace capability absent | Report the limitation; use available sufficient evidence or block only the dependent requirement |

An isolated profile is lost when its browser context closes. For the demo this is useful; for a real authenticated workflow, plan secure sign-in/session handling deliberately. GitHub stores the skills and instructions; it does not start your local MCP process. A cloud chat also does not gain access to your local MCP server merely because you upload these Markdown files.

## Optional official Playwright CLI skill

Choose this only if you want the separate shell-driven workflow:

```sh
npm install -g @playwright/cli@latest
playwright-cli --help
playwright-cli install --skills
```

The documented default installs the official skill in `.claude/skills/playwright-cli`. For an agent using `.agents/skills`, the documented alternative is `playwright-cli install --skills=agents`. This optional installation also performs its documented workspace initialization; review its changes before committing.

Keep Edward's `qa-*` skills and the official `playwright-cli` skill: the first guide quality decisions, the second guides CLI operations. Select **MCP** or **CLI** explicitly for a run and record which was actually used. Their sessions and element references are separate. CLI installation does not register MCP, and MCP operation does not require CLI installation.

Official references: [CLI installation](https://playwright.dev/agent-cli/installation), [CLI skills](https://playwright.dev/agent-cli/skills), [CLI versus MCP](https://playwright.dev/agent-cli/introduction).

## Version and verification limits

These instructions were checked against official documentation on 2026-10-22. `@latest` is convenient for first setup; record the resolved version and use a verified pinned version for a repeatable presentation if your environment requires it. Do not invent a version number. This package update did not install anything on your computer, connect your MCP client, or execute the browser exercise.
