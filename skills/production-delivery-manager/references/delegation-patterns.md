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
