# Executable automation

## Run in three steps

Use Node.js 22 or later from the repository root:

```bash
npm ci
npx playwright install chromium
npm run test:automation
```

The command starts and stops isolated local targets, runs the **Postman** API collection followed by Playwright UI and baseline quality checks, and returns a failing exit code if either runner fails. It does not target an external application. On Linux CI use `npx playwright install --with-deps chromium`.

| Command | Purpose | Evidence |
|---|---|---|
| `npm run test:api` | Run the Postman v2.1 collection against a managed local target | 24 requests, assertion results, JSON and JUnit |
| `npm run test:ui` | Run Playwright create, reject and complete workflows | HTML, JUnit, JSON; traces/screenshots on failure |
| `npm run test:nfr` | axe automated rules, keyboard path, response headers | Actual measurements/assertions; no conformance certification |
| `npm run report:automation` | Open the Playwright HTML report | Latest local browser run |
| `npm run mcp:check` | Initialize MCP, list tools and navigate the local target | `reports/automation/mcp-connection.json` |

Reports are local and ignored by Git. Recorded framework verification is in [framework-validation.json](../data/framework-validation.json). These results are **framework evidence**, not a project readiness decision or historic business achievements. The existing quality KPI ledgers remain separate.

## Postman desktop

1. Run `npm run serve:contract` and keep that terminal running.
2. Import [the collection](../automation/postman/QA_API.postman_collection.json) and [the environment](../automation/postman/Local_Contract.postman_environment.json).
3. Select **QA Local Contract** as the environment. Run the **whole collection in order**, one iteration. Requests build dependent fixtures and clean them up. API-00 creates a new isolated workspace each iteration.
4. Inspect Tests results and actual response bodies. The token is a public synthetic local fixture. Never replace it with a committed real credential.

The included account-free runner pins Newman 6.2.3 for v2.1 compatibility. Postman currently deprecates Newman and recommends **Postman CLI** for maintained integrations and newer collection formats. For a new organization-wide adoption, use its approved Postman CLI installation:

```bash
# First start the local target in a separate terminal.
postman collection run automation/postman/QA_API.postman_collection.json -e automation/postman/Local_Contract.postman_environment.json
```

CLI authentication/availability follow your installed Postman version. The local verification receipt explicitly records the runner actually exercised. Do not migrate the collection to v3 while keeping a v2.1-only runner.

## Test architecture and applicability

[The local contract](../automation/CONTRACT.md) is the test oracle. UI fixtures use HTTP for setup, cleanup and cross-layer effects; the dedicated API test suite is Postman. Each test uses isolated synthetic data. Schema assertions verify structure; persisted-value and no-side-effect assertions verify behavior beyond HTTP codes.

[The test-type matrix](test-types.md) distinguishes implemented local checks from planned product assessments. The local target is intentionally small; it proves framework execution, not SQL Server, a third-party provider, an entire architecture, full WCAG conformance or security assurance.

To adapt to a real application, confirm routes, contracts, rules, roles, data, locators and environment. Add project specifications under `automation/application/`, replace the `.example` only after real expectations are bound, then explicitly set `QA_APP_URL` and `QA_APPLICATION_SCOPE_CONFIRMED=true` before using `playwright.application.config.ts`. Its fail-closed setup prevents a local pass being presented as an external product pass.

## MCP connections

`npm ci` installs the pinned Playwright MCP server. The committed files start the same local launcher:

| Client | Configuration | Start/check |
|---|---|---|
| Claude Code | `.mcp.json` | Open at repository root, approve workspace server trust when requested; verify server/tools in the client |
| Gemini CLI | `.gemini/settings.json` | Open at repository root; inspect `/mcp` and verify available tools |
| VS Code Copilot | `.vscode/mcp.json` | Open repository folder; use MCP: List Servers, start Playwright and verify tools in agent mode |
| Other MCP client | `node scripts/start-playwright-mcp.cjs` | Configure stdio at repository root and verify actual discovery |
| Other LLM without MCP | Markdown procedures + saved artifacts | Review supplied evidence; no browser execution is implied |

The launcher defaults to an isolated browser profile. Configuration does not establish a trusted connection on someone else's computer. `npm run mcp:check` performs an actual local handshake and navigation independently of those clients. Optional `QA_BROWSER_EXECUTABLE` and JSON-array `QA_BROWSER_ARGS` support a managed browser installation; `QA_MCP_HEADLESS=true` enables headless checks. Do not give an agent production data or blanket action authority through configuration.

MCP exploration does not replace deterministic regression or release evidence. Review generated locators and assertions, reproduce findings, then add maintainable tests where risk justifies them.

## CI gate

[Azure pipeline template](../ci/azure-pipelines.yml) installs locked dependencies and browsers, executes both runners, publishes JUnit and retains evidence even after test failure. Bind it to an actual pipeline and required branch/stage policy before claiming an enforced gate. A published file alone does not block releases.

## Cases for Azure Test Plans

Open [the exporter](../test-case-export.html) or use [the CLI](azure-test-cases.md). Exporting case definitions does not create test results or mark automation as associated in Azure.

## Primary references

- [Playwright web server](https://playwright.dev/docs/test-webserver)
- [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Postman Newman status and v2.1 support](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Postman CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [Gemini CLI MCP](https://geminicli.com/docs/tools/mcp-server/)
- [VS Code MCP](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
