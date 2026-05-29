# Delivery Gates

Use these gates to control engineering work from request to handoff.

## Gate 0: Task Classification

Classify before planning:

- Simple: one narrow change, low blast radius, clear acceptance.
- Medium: multiple files, existing patterns available, moderate verification needed.
- Complex: cross-module behavior, unclear requirements, data/security/migration/release risk, or production-grade expectation.

Simple tasks may skip visible planning, but must still report verification and risk.

## Gate 1: Requirements

Lock or state:

- user goal
- target user or system
- in-scope behavior
- out-of-scope behavior
- acceptance criteria
- known assumptions
- blocking questions

Stop and ask when:

- multiple plausible products would satisfy the request
- data ownership, permission, payment, deletion, migration, or security behavior is unclear
- the requested output cannot be verified without a missing artifact or decision
- proceeding would create irreversible or high-cost changes

Proceed with assumptions when:

- the assumption is low-risk
- the implementation can be reversed
- the assumption is explicitly reported
- verification can still prove the agreed slice

## Gate 2: Discovery

Gather only context needed for the task.

Required checks when relevant:

- project rules and source-of-truth docs
- existing local modules, APIs, pages, components, tests, scripts, adapters, fixtures, and examples
- CodeGraph or structural search for definitions, callers, callees, flows, and impact
- graph or docs maps for cross-document and architecture questions
- official documentation for version-sensitive behavior

Discovery output should identify:

- nearest reusable local pattern
- affected modules and files
- interfaces and contracts
- likely tests or validation commands
- risks that can change the plan

## Gate 2.5: Workspace Isolation

Before editing files, choose the workspace strategy.

Required checks:

- If inside a Git repository, run `git status --short`.
- Record the original workspace path, current branch, and intended delivery target before creating a branch or worktree.
- Identify tracked and untracked changes that are unrelated to the task.
- Treat local changes as decision context, not as an automatic stop condition.
- Do not overwrite, revert, delete, or reformat unrelated user changes.
- Decide whether the current workspace, a new branch, or a separate git worktree is the right execution surface.
- Decide whether the isolated surface is temporary implementation space or the accepted final deliverable.

Use the current workspace when:

- the task is small, reversible, and low-risk
- tracked changes are unrelated or clearly non-overlapping
- untracked files can be ignored safely
- the user's expected validation or merge target is the current workspace
- the work can be reviewed with a clear diff that separates user changes from agent changes

Use a dedicated branch or git worktree when:

- the task is large, risky, long-running, or likely to span multiple verification cycles
- the user needs their current workspace preserved
- multiple agents will write code in parallel
- existing local changes overlap the likely edit scope, or user intent for those files is unclear

When using a branch or worktree:

- Default the delivery target to the original workspace/current branch when the user asked from that workspace and did not request a PR-only or branch-only handoff.
- State the integration method before implementation: merge, cherry-pick, patch application, PR/branch handoff, or explicit "not applied to original workspace".
- Treat worktree output as candidate work until it is integrated into the agreed delivery target and verified there.
- Do not claim the task is complete from an isolated worktree unless the user explicitly accepted that branch/worktree/PR as the deliverable.

Ask before proceeding when:

- the task requires editing a file that already has user changes and the intended final content is ambiguous
- merging agent changes with user changes could drop content, reorder large sections, or hide authorship
- validation would be misleading because it would test a mixed state whose ownership is unclear

Cleanup requirements:

- Keep intentional deliverables in the diff.
- Remove temporary files, logs, generated scratch artifacts, and abandoned test fixtures before handoff.
- Report any remaining untracked files that were not created by the task and were intentionally left alone.

## Gate 3: Plan

For medium and complex work, provide:

- objective
- implementation slices
- workspace decision: current workspace, branch, or worktree, with reason
- delivery target and integration method when implementation is isolated
- file/module ownership
- sub-agent roles, if used
- verification strategy
- rollback or mitigation path for risky changes

A valid plan has disjoint ownership. One owner may edit a module; reviewers may inspect any module without editing.

## Gate 4: Implementation Control

During implementation:

- keep the scope tight
- prefer established local conventions
- avoid speculative abstractions
- preserve unrelated user changes
- update docs or ledgers required by project rules
- stage broad changes through small, verifiable slices

If new information invalidates the plan, pause, report the conflict, and re-plan.

## Gate 4.5: Delivery-Target Integration

Before final verification:

- If work happened in the current workspace, confirm this workspace and branch are the intended delivery target.
- If work happened in a branch or worktree, merge, cherry-pick, or apply the patch back to the agreed target when safe and within user instructions.
- If integration is blocked by conflicts, dirty overlapping files, missing permissions, or user preference, report the task as not applied to the delivery target.
- Run `git status --short` in the delivery target after integration.
- Separate task changes from unrelated pre-existing user changes in the report.

If integration cannot be performed, downgrade the completion claim to "candidate implemented in <branch/worktree>" or "handoff only"; do not present it as delivered in the user's active workspace.

## Gate 5: Verification

Choose the strongest practical verification for the risk.

Examples:

- Unit tests for pure logic and services.
- Integration tests for API/database/workflow boundaries.
- Typecheck/lint/build for compile-time and packaging safety.
- Migration dry-runs or schema checks for data changes.
- Browser checks for UI flows and runtime errors.
- Security checks for permission, validation, injection, secrets, tenant isolation, and audit trails.
- Governance or link checks for documentation changes.

Final verification must run from the delivery target unless the agreed deliverable is explicitly a branch or PR. Verification run only in a temporary worktree is partial evidence and must be labeled as such.

Verification report format:

```md
### Verification

- Ran: `<command or check>` -> <result>
- Not run: `<command or check>` -> <reason>
- Manual check: <what was inspected and why it is sufficient or partial>
```

## Gate 6: Handoff

Final handoff format:

```md
### Delivered

- <completed change>

### Verified

- <evidence>

### Workspace

- <current workspace/branch/worktree decision, delivery target, integration status, and cleanup status>

### Residual Risk

- <risk or "No known residual risk beyond untested environments.">

### Next Step

- <one concrete next action, or "None required.">
```

Use this structure when the task is complex. For small tasks, compress it into a short paragraph while keeping the same facts.
