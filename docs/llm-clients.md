# One method, different LLM clients

The procedures are ordinary Markdown. Any LLM that can read the supplied text can apply the analysis method. File discovery, tool execution, context limits and permissions depend on its host. A model name does not establish browser, SQL, API or pipeline access.

## Working model

**Project sources → choose a skill → AI drafts/reasons → accountable review → actual tools verify → evidence ledger → quality decision.**

Start with the engagement objective and a small source package: a story/specification, related rules/contracts, known dependencies, current checkpoint and relevant defects if available. Do not load all procedures blindly. Procedure 00 selects stages; 31 supports leadership and 32 reviews source fidelity throughout.

| Client | What this repository supplies | How to start | Capability check |
|---|---|---|---|
| Claude Code, local project session | CLAUDE.md and `.claude/skills/qa-*/SKILL.md` | Open the repository as the workspace; invoke `/qa-orchestrate-testing-lifecycle` or ask it to read MASTER_PROMPT.md | Confirm the relevant skill/procedure was loaded and inspect actual exposed tools before execution |
| Gemini CLI | GEMINI.md and `.gemini/skills/qa-*/SKILL.md` | Open the repository, use `/skills list` to inspect discovery, then request the orchestrator by name or point to procedure 00 | Use `/skills reload` if needed and follow the client's actual activation/permission controls |
| GitHub Copilot in VS Code | `.github/copilot-instructions.md`; VS Code also documents `.claude/skills/` discovery | Open the repository, use an agent-capable session and explicitly request the needed skill/procedure | Confirm skill availability in that client; agent/tool availability is separate from ordinary text chat |
| Other coding assistants | AGENTS.md, MASTER_PROMPT.md and authoritative procedures | Ask the assistant to read those files and the selected procedure | Use its supported discovery paths or explicit file reads; do not assume another client's slash commands work |
| Chat-only LLM / web chat | Attach or paste the master prompt, operating contract, relevant procedure and sanitized sources | Request a stage-appropriate analysis with explicit source references | It may produce analysis/design; execution requires actual supported tools or a truthful human/tool handoff |

These are client adaptations of 35 unique skills. The `.claude` and `.gemini` folders contain thin entry points to the same authoritative procedures; they are not separate methodologies. Keep the complete repository together so relative references resolve. Other products branded with similar model names may use different discovery behavior.

## A source-analysis request

```text
Read MASTER_PROMPT.md, docs/operating-contract.md and
docs/procedures/00-orchestrate-testing-lifecycle.md.
Use the supplied actual sources and current checkpoint.
Understand the context, identify decisions affecting risk,
then apply only the relevant procedures. Explain each selected
skill's purpose and return a source-linked artifact, unknowns
and the next action. Keep project artifacts in English.
```

## A focused skill request

```text
Apply procedure 04 to this story and its related sources.
Separate confirmed rules, observed behavior and proposals.
Identify essential ambiguity, dependency and state questions.
Do not invent acceptance criteria or expected results.
Return decisions/questions plus the coverage they affect.
```

## An execution request

Supply the actual target/build, approved scope/data/accounts, expected oracle, evidence location and cleanup. Verify real tools and readiness using the appropriate procedure before running. Design is not execution; unavailable tooling leaves dependent checks Not Run/Blocked. Follow [tool connections](tool-connections.md).

## Resuming or changing the model

Transfer a compact checkpoint: objective/scope, sources/revisions, confirmed decisions, artifact references, actual run/build evidence, blockers, authorization boundaries and next procedure. Recheck invalidated evidence; preserve earlier attempts. The next model should continue the work rather than recreate unsupported history.

## What accountable review checks

Source fidelity; expected-result oracles; duplicate/omitted risk coverage; realistic data and bindings; tool truthfulness; actual evidence freshness; complete denominators; and decision authority. Review AI-generated SQL for actual schema/grain/joins and automation for real interfaces/assertions before use. Keep confidential sources within the organization's permitted tools.

## Official client references

- Claude Code project skills: https://code.claude.com/docs/en/skills
- Gemini CLI skills and session discovery: https://geminicli.com/docs/cli/using-agent-skills/
- Gemini CLI project context: https://geminicli.com/docs/cli/gemini-md/
- VS Code agent-skill discovery: https://code.visualstudio.com/docs/agent-customization/agent-skills

Client features can change; use the actual installed version and organization settings. This repository does not claim live client authentication or tool connection merely because these files exist.
