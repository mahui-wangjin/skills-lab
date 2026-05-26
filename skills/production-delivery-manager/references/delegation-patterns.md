# Delegation Patterns

Use real sub-agents only when the user has authorized delegation or the environment explicitly supports it for the task.

The lead agent must keep the critical path moving locally and delegate bounded side work that can run independently.

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

## Bad Delegation Tasks

Do not delegate:

- vague ownership such as "fix the feature"
- the immediate blocking investigation you need before taking any next step
- overlapping edits to the same files
- final architecture judgment
- final acceptance decision
- tasks requiring hidden context not passed to the sub-agent

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

For code-editing workers, add:

- You are not alone in the codebase.
- Do not revert unrelated edits.
- Keep changes inside the assigned scope.
- List changed files in the final response.

## Integration

When a sub-agent returns:

1. Review its changed files or findings.
2. Reject or revise unsupported claims.
3. Resolve conflicts with the main plan.
4. Run or record relevant verification.
5. Close the agent when no longer needed.

Sub-agent output is evidence, not final truth.
