# Load the QA skills in Claude Code or Cursor

This revision contains the readable numbered procedures plus **35 project skill entry points** in `.claude/skills/qa-*/SKILL.md`. Each entry point loads its numbered authoritative procedure and the shared contract from this bundle. The entry points are small; they do not duplicate the full procedures.

## Local workspace

1. Extract the ZIP.
2. Open `QA_Testing_Lifecycle_Skills_EN`, the folder containing `README.md`, as the client workspace.
3. Keep the complete folder together, including `.claude/skills/`.
4. Start a new client session or refresh skills as supported by your installed version.

In Claude Code, project skills are discovered from `.claude/skills/<name>/SKILL.md`. Cursor currently supports that layout as a compatibility location; its primary layouts also include `.cursor/skills/` and `.agents/skills/`. We use one layout to avoid duplicate skill discovery. See the official [Claude skill documentation](https://code.claude.com/docs/en/skills) and [Cursor skill documentation](https://cursor.com/docs/skills).

## Try one skill

In Claude Code:

```text
/qa-orchestrate-testing-lifecycle
```

Then provide the scope and mode, or append a clear request. Other useful entry points:

| Entry point | Purpose |
|---|---|
| `/qa-connect-playwright-mcp` | Verify the MCP setup and browser capability |
| `/qa-analyze-acceptance-criteria-and-refine` | Review a supplied story and ask refinement questions |
| `/qa-design-functional-test-cases` | Design cases from confirmed rules |
| `/qa-execute-web-tests-with-playwright` | Execute authorized web cases through the selected real tool path |
| `/qa-produce-clear-visual-quality-reports` | Build a concise evidence-based report |
| `/qa-evaluate-release-readiness-and-risk` | Assess gates and recommend a release decision |

In Cursor, type `/` in Agent chat and select the discovered skill by name. If an entry is not visible, ask the agent to read the numbered procedure directly and follow its shared contract while you diagnose skill discovery. Loading an instruction is independent from connecting an MCP tool.

## Entry-point behavior

An entry point instructs the agent to read `../../../<numbered-procedure>.md` relative to its own skill directory. This resolves to the extracted workspace root. It also links the contract, master prompt and setup material where needed. These are **project-local skills**, not standalone global installations. Copying only one entry-point folder to a global skill directory would break those references. Keep the complete bundle or adapt its references explicitly.

There is no automatic permission grant in a skill file. The real user/session scope controls test execution and Azure writes. Skill invocation must not bypass client policies, MFA, environment gates or a missing business oracle.

## Put it in your GitHub repository

Keep this bundle as its own folder in `Agentic-QA-Engineer`. Do not replace an existing root `README.md`, `CLAUDE.md` or client configuration. Open the bundle folder locally for the simplest discovery behavior.

For a new upload, run these commands from the existing local repository root after copying the extracted folder there:

```sh
git status --short
git add -- QA_Testing_Lifecycle_Skills_EN
git diff --cached --stat
```

Inspect the staged changes. Commit only if they contain the intended Markdown bundle and no private material:

```sh
git commit -m "Add QA lifecycle skills and Playwright MCP guide"
git push
```

If your folder already exists in the repository, merge this revision deliberately and inspect the diff first. Do not overwrite unrelated work. GitHub web uploads are also possible, but ensure the `.claude/skills` entries are actually included. A ZIP uploaded as one opaque file is less useful for reading the methodology online.

The commands above publish the repository files; they do not install Node, connect Playwright, run tests, create Azure items or deploy an application. After configuring MCP locally, keep credentials, browser profiles, traces and customer data out of a public repository. Review any runtime-generated files before staging them.

## If you prefer a generic LLM

Attach the master prompt, shared contract, numbered orchestrator and relevant procedures. This gives the LLM the QA method. For actual browser execution, its host must separately provide compatible Playwright tools. Ordinary file upload does not create that capability.
