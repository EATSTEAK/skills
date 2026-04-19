---
name: orchestrator
description: Orchestrate a multi-stage refactor or migration by creating a fresh team per stage, running one implementation subagent and one validation subagent, then cleaning up before the next stage.
---

Use this when the work should be executed as explicit stages with clean boundaries.

## Steps

1. Define the stages and the exact success criteria for each stage.
2. Write or update a short markdown note for each stage before execution.
3. Create one fresh team for the current stage only.
4. Spawn exactly one implementation subagent for that stage.
5. Wait for the implementation report.
6. Spawn exactly one validation subagent for the same stage.
7. Require the validation report in `/review` style.
8. Report all findings to the user, including INFO findings.
9. Ask before fixing INFO-level follow-ups.
10. Commit only the files for the current stage.
11. Request shutdown from all stage teammates.
12. Delete the stage team after all teammates terminate.
13. Create a new team for the next stage instead of reusing the old one.

## Default rules

- Use `opus` for both implementation and validation subagents.
- Keep one implementation agent and one validation agent per stage.
- Treat validation as independent; do not skip it.
- Prefer separate commits per stage.
- Exclude unrelated local files from stage commits.
- If validation says the stage is incomplete, continue the same stage instead of committing.

## Output discipline

- Keep stage reports short and factual.
- Always include remaining risks.
- Distinguish clearly between PASS, conditional approval, and not ready.
