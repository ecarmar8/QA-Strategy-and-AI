# Start here — English QA skills with Playwright MCP

**Open this folder locally in Claude Code or Cursor, connect Playwright MCP, then run the small browser demonstration.** GitHub is where you publish the methodology and its Markdown visuals; the local MCP client is where browser actions happen.

| Step | Open/do | Result |
|---|---|---|
| 1 | [SKILLS_INSTALLATION.md](SKILLS_INSTALLATION.md) | The client discovers the 35 `qa-*` skill entry points |
| 2 | [PLAYWRIGHT_MCP_SETUP.md](PLAYWRIGHT_MCP_SETUP.md) | A real MCP connection receipt, or a precise blocker |
| 3 | [CTO_LIVE_DEMO.md](CTO_LIVE_DEMO.md) | A visible three-case browser exercise with actual evidence |
| 4 | [99-CTO-FIVE-MINUTE-WALKTHROUGH.md](99-CTO-FIVE-MINUTE-WALKTHROUGH.md) | A separate fictional payment example explaining risk and No-Go |
| 5 | [MASTER_PROMPT.md](MASTER_PROMPT.md) | A full lifecycle on your real supplied scope when ready |

## What you show the CTO

Keep three surfaces visible: **the short scope/case table**, **the live browser**, and **the evidence-based report**. The 35-skill library is supporting material; the CTO does not need to read every file.

Say:

> “These skills encode my QA process. The LLM uses them to analyze, plan and assess evidence. Playwright MCP supplies the browser actions. I keep business expectations, actual observations and release decisions separate.”

Use the live task-list exercise for connectivity and execution. Use the simulated refund example for payments judgment. State which is live and which is simulated.

## First client instruction

```text
Read START_HERE.md and 90-OPERATING-CONTRACT.md.
Use qa-connect-playwright-mcp to verify the actual browser connection.
Follow the read-only connection-check scope in PLAYWRIGHT_MCP_SETUP.md.
Then present the exact CTO_LIVE_DEMO.md execution scope before the live run.
Use the user's current authorization; do not invent tools or results.
Keep all explanations, cases and reports in English.
```

The connection-check instruction itself grants no mutations. To execute the three cases, use the explicit scoped live-run prompt in CTO_LIVE_DEMO.md. Reuse authorization already granted; do not ask the same permission twice.

## What this revision contains

- 35 numbered QA procedures, including the new MCP setup skill 34.
- 35 lightweight discoverable project entry points in `.claude/skills/`.
- English setup, installation, master prompt, templates, visuals and CTO scripts.
- Optional official Playwright CLI-skill installation instructions, clearly separate from MCP.

All distributed files are Markdown. Configuration snippets and commands are inside the documentation; no application, credentials, test results or vendor skill code is bundled. This revision has not connected to your machine or executed a product test.
