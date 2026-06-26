# Delegation Patterns

Use real sub-agents only when the user has authorized delegation and the environment supports it for the task. Explicit requests for this skill, production-grade delivery, quality-first delivery, team-led delivery, parallel work, or multi-agent execution authorize the lead to evaluate and prioritize real sub-agent use within the current tool policy.

The lead agent must keep the critical path moving locally and delegate bounded side work that can run independently.

For complex, production-grade, strict, or quality-first delivery, delegation is the default quality posture, not an optional flourish. If no real sub-agent is used, the lead must state the exception, add compensating objective verification where practical, and later challenge the exception during steelman review.

## Good Delegation Tasks

Delegate when the task is:

- self-contained
- materially useful
- not the next blocking step
- assigned to a disjoint file/module scope if it edits files
- easy to verify after return

Examples:

- Code Explorer: map existing auth flow, no edits.
- Docs Lookup: verify current API behavior from official docs.
- Backend Worker: implement one service/controller slice.
- Frontend Worker: implement one page or component slice.
- Database Reviewer: inspect schema and migration risks.
- Reviewer: inspect the final diff for correctness and missing tests.
- E2E Runner: run browser validation while implementation polish continues.
- Evidence Reporter: at finalization, assemble a human-readable validation packet or HTML report from accepted verification evidence without inventing results. During implementation, keep only an evidence ledger and do not polish the final report.

## Minimum Quality Surfaces

For production-grade work, try to create at least one independent surface beyond lead-agent implementation:

- Architecture surface: Architect or Code Explorer maps boundaries before broad edits.
- Risk surface: Reviewer, Security, Database, TypeScript, Performance, or silent-failure reviewer challenges failure modes.
- Verification surface: Test or E2E runner validates user-visible flows, build/runtime checks, or regression tests.
- Documentation/release surface: Docs or Release agent checks that handoff, ledgers, Human Validation Packet, HTML report, CI/workflow evidence, and acceptance evidence match the change.

Use the surfaces that match the task's risk. A backend data migration may need database/security review; a frontend product workflow may need E2E and accessibility review; a docs-only skill change may only need skill validation plus reviewer critique.

An independent surface must be capable of changing the result. A real sub-agent review, targeted automated test, typecheck/build, browser/E2E pass, security/database review, or release/doc consistency check can count when it directly targets the risky acceptance criteria. A generic self-affirming checklist does not count.

## Bad Delegation Tasks

Do not delegate:

- vague ownership such as "fix the feature"
- the immediate blocking investigation you need before taking any next step
- overlapping edits to the same files
- final architecture judgment
- final acceptance decision
- tasks requiring hidden context not passed to the sub-agent
- final completion claims or user-facing acceptance

Do not skip delegation on complex work merely because the lead can implement faster. Speed is not a sufficient reason when the user's stated preference is delivery quality.

## Delegation Prompt Shape

Use this shape:

```md
Role: <specialist>
Goal: <specific outcome>
Scope: <files/modules/responsibilities>
Do not: <explicit exclusions>
Inputs: <docs, symbols, paths, assumptions>
Expected output: <patch, findings, test result, risk list>
Verification: <command/check or evidence required>
```

For read-only review agents, ask for findings that could change the result: blockers, missing tests, weak assumptions, overclaims, missing human-validation surfaces, report gaps, and residual risks. A review prompt that cannot produce a rejection is usually too soft.

For code-editing workers, add:

- You are not alone in the codebase.
- Do not revert unrelated edits.
- Keep changes inside the assigned scope.
- Use the assigned branch or worktree only; do not write into the lead agent's workspace unless explicitly instructed.
- Treat your branch or worktree as a candidate implementation surface; the lead agent owns integration into the delivery target.
- Clean up temporary files, logs, scratch outputs, and abandoned artifacts created by your task.
- List changed files, branch/worktree path, and whether your changes were committed, staged, or left as a working-tree diff in the final response.

## Integration

When a sub-agent returns:

1. Review its changed files or findings.
2. Reject or revise unsupported claims.
3. Resolve conflicts with the main plan.
4. Integrate accepted code changes into the agreed delivery target by merge, cherry-pick, patch application, or explicit PR/branch handoff.
5. Run or record relevant verification from the delivery target whenever the task is meant to affect the user's active workspace.
6. Confirm temporary artifacts and unused worktrees/branches are cleaned up or explicitly handed off.
7. Close the agent when no longer needed.

Sub-agent output is evidence, not final truth. A sub-agent's isolated worktree cannot be treated as delivered until the lead agent has integrated or explicitly handed off that surface.

## No-Delegation Note

When complex or production-grade work proceeds without real sub-agents, record a concise note:

```md
No real sub-agent used because: <reason>.
Risk accepted: <what independent perspective is missing>.
Fallback: <self-reviewed specialist perspectives or extra objective verification added>.
Completion claim: <full / partial / candidate / self-reviewed>.
```

This note is not a waiver for quality. If the missing perspective is important to acceptance, downgrade the completion claim or ask the user.
