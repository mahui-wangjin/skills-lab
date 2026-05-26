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
- Identify tracked and untracked changes that are unrelated to the task.
- Do not overwrite, revert, delete, or reformat unrelated user changes.
- Decide whether the current workspace, a new branch, or a separate git worktree is the right execution surface.

Use the current workspace when:

- the task is small, reversible, and low-risk
- there are no conflicting tracked changes
- any unrelated untracked files can be ignored safely

Use a dedicated branch or git worktree when:

- the task is large, risky, long-running, or likely to span multiple verification cycles
- the user needs their current workspace preserved
- multiple agents will write code in parallel
- existing local changes overlap the likely edit scope

Cleanup requirements:

- Keep intentional deliverables in the diff.
- Remove temporary files, logs, generated scratch artifacts, and abandoned test fixtures before handoff.
- Report any remaining untracked files that were not created by the task and were intentionally left alone.

## Gate 3: Plan

For medium and complex work, provide:

- objective
- implementation slices
- workspace decision: current workspace, branch, or worktree, with reason
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

- <current workspace/branch/worktree decision and cleanup status>

### Residual Risk

- <risk or "No known residual risk beyond untested environments.">

### Next Step

- <one concrete next action, or "None required.">
```

Use this structure when the task is complex. For small tasks, compress it into a short paragraph while keeping the same facts.
