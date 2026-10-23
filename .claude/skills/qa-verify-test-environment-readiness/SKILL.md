---
name: qa-verify-test-environment-readiness
description: "Establish whether this build and its dependencies support trustworthy checks. Use for verify environment readiness."
---

# Verify environment readiness

Read and apply [the authoritative procedure](../../../docs/procedures/13-verify-test-environment-readiness.md) and [the shared operating contract](../../../docs/operating-contract.md). Reuse current scope and authorization. Load relevant source revisions, distinguish confirmed rules, observations and proposals, and return the required artifact plus a checkpoint. Missing requirements remain Pending definition; execution without evidence remains Not Run. Apply the procedure directly rather than treating this entry point as its full content.

Expected inputs: Target/build, configuration, accounts, data and dependencies.

Required output: Track-specific readiness and blockers.

Use [the skill catalog](../../../docs/skills.md) to select adjacent procedures. This project-local entry point requires the repository structure to remain together.
