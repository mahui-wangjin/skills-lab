# Delivery Gates

Use these gates to control engineering work from request to handoff.

## Gate 0: Task Classification

Classify before planning:

- Simple: one narrow change, low blast radius, clear acceptance.
- Medium: multiple files, existing patterns available, moderate verification needed.
- Complex: cross-module behavior, unclear requirements, data/security/migration/release risk, or production-grade expectation.
- Quality-first or strict production-grade requests are complex by default. Downgrade only when the work is narrow, reversible, low-risk, and independently verifiable.

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
- quality priority: speed-first, balanced, or quality-first when the user has stated a preference

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
- delegation decision: real sub-agents, local specialist perspectives, or a stated no-delegation exception

A valid plan has disjoint ownership. One owner may edit a module; reviewers may inspect any module without editing.

For complex or production-grade work, a valid plan must not simply say "I will implement and verify." It must identify at least one independent challenge surface: specialist review, E2E/browser verification, security/database/type review, docs/release check, or an explicit reason real delegation is unavailable or not useful.

## Gate 3.5: Delegation Quality Gate

Before implementation on complex, production-grade, or quality-first work:

- decide which work stays on the lead agent's critical path
- delegate bounded side work when it can run independently and materially improve quality
- assign non-overlapping write scopes to code-writing agents
- assign read-only reviewers to challenge correctness, safety, maintainability, verification gaps, or user-visible acceptance
- record why no real sub-agent is used if the task remains single-agent

Good no-delegation reasons:

- the task is simple: narrow, low-risk, reversible, and independently verifiable
- the task is a small, reversible, one-file change with clear validation
- the environment has no real sub-agent facility
- the next step is blocked on local discovery and cannot usefully run in parallel
- delegation would require sharing missing private context or would risk overlapping writes

Bad no-delegation reasons:

- "faster if I do it myself" on a production-grade or broad task
- "the code looks simple" without checking blast radius and verification
- "I will self-review later" when an independent reviewer could run in parallel
- assigning every role to the lead without naming residual risk

Simple low-risk work does not need a delegation matrix. It only needs a brief reason for the compressed path, verification evidence, and residual-risk reporting.

## Gate 4: Implementation Control

During implementation:

- keep the scope tight
- prefer established local conventions
- avoid speculative abstractions
- preserve unrelated user changes
- update docs or ledgers required by project rules, after routing content to the right artifact type
- stage broad changes through small, verifiable slices
- keep report work out of the implementation loop; record only a terse evidence ledger when a command, screenshot, sub-agent review, CI run, or manual check produces evidence

### Gate 4.1: Document Routing

Before writing to any repository document, classify the content:

| Content type | Correct destination | Must not go into |
| --- | --- | --- |
| Long-lived product, architecture, API, workflow, operating rule, or accepted decision | Existing project docs, ADRs, specs, or source-adjacent docs | HTML report evidence-only sections |
| Final delivery summary, key outcomes, evidence map, residual risk, human checkpoints | Final answer and, when triggered, `.production-delivery-reports/<date>_<slug>/index.html` | Product/architecture/development docs |
| Temporary evidence ledger, command result notes, browser screenshots, short log excerpts | Agent working notes while implementing; report `evidence/` only when durable evidence is required | Formal docs unless the project explicitly has a task-ledger path |
| Debug chronology, repeated failed attempts, raw command dumps, sub-agent transcripts | Normally nowhere durable; include only if the user explicitly asks for audit-trail detail | Existing project docs and result reports |

Rules:

- Formal docs are for durable facts, not the agent's work diary.
- Do not create or repurpose an existing product, architecture, development, or governance doc to hold process notes.
- If project rules require a task ledger, write only concise final task state: goal, key changes, verification, risk/blocker, next step. Do not paste execution chronology.
- If uncertain whether a document is a ledger or source-of-truth doc, treat it as source-of-truth and keep process notes out.

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

For complex or production-grade work, include whether verification had an independent surface such as a delegated reviewer, delegated E2E pass, targeted automated test, browser run, build/typecheck, or a clearly labeled self-reviewed fallback.

When there is no real sub-agent or independent reviewer, strengthen the objective verification where practical. If verification cannot compensate for the missing perspective, label the result as partial, candidate, or self-reviewed instead of complete production-grade delivery.

## Gate 5.5: Human Validation Report

Before final handoff, decide whether a durable report is required.

Always include a compact Human Validation Packet for medium and complex work.

Use result-first reporting. The report must help the user accept or reject the final outcome without reading the full diff. It is not a development diary, scratchpad, chronological debug log, or place to narrate repeated failed attempts.

The user's default validation need is a final summary:

- delivered capabilities
- key changes and boundaries
- final verification and what it proves
- residual risks or evidence gaps
- concrete next step or no action required

Do not include process chronology unless the user explicitly asks for an audit trail.

During implementation, maintain only a compact evidence ledger:

```md
- Evidence: <command/check/artifact>
  Result: <passed/failed/skipped/not run>
  Proves: <one sentence>
  Limit: <one sentence>
```

Do not repeatedly write or polish the HTML report while implementation is still changing. Generate or update the durable report after delivery-target integration, final verification, and steelman review, using the final evidence ledger.

Generate an HTML report under `.production-delivery-reports/<YYYY-MM-DD>_<slug>/index.html` when:

- the user asks for a report or validation package
- the task is complex, production-grade, release-candidate, merge-to-main, launch, rollback, or final acceptance work
- the risky surface includes architecture, core business logic, permission, security, data/schema/migration, queues/workers, external side effects, AI runtime, or product UI/browser acceptance
- screenshots, browser traces, logs, CI/workflow artifacts, sub-agent findings, or multiple verification surfaces need to be reviewed together

Use `scripts/create_report.py` when possible to scaffold the report directory, `index.html`, `evidence/`, and `manifest.json`. Read `human-validation-report.md` for the report contract before writing the report.

CI/workflow results are evidence inputs. A report may cite a CI run, job, artifact, or release-candidate workflow, but the report must still explain what that evidence proves and does not prove.

If the task is small and low risk, do not generate a report unless asked. Report verification and risk briefly.

If a report trigger applies but no report is generated, state why in the final handoff and downgrade the completion claim if the missing report weakens acceptance.

## Gate 6: Human Validation Handoff

Final handoff format for complex work:

```md
### Delivered

- <final user-visible capabilities or engineering outcomes>

### Human Validation Packet

- Status: <complete / candidate / partial / blocked / self-reviewed>
- Needs user decision: <yes/no>
- Review first: <1-3 human review points>
- Delivered capabilities: <what the user can now do or what behavior changed>
- Architecture surface: <boundary and dependency direction only if relevant to acceptance>
- Core logic surface: <critical flow and invariants, not implementation chronology>
- Evidence map: <final tests/build/CI/browser/screenshots/docs and what each proves>
- Evidence gap: <what was not proven>
- Steelman result: <strongest objection and decision>
- Residual risk: <specific risk or none known>
- Human checkpoints: <acceptance checks>
- Report: <path or not generated reason>

### Verified

- <evidence>

### Delegation / Review

- <delegation decision, independent challenge surface, or no-delegation reason for complex/production-grade work>

### Workspace

- <current workspace/branch/worktree decision, delivery target, integration status, and cleanup status>

### Report Artifact

- <HTML report path, evidence path, committed/staged/local-only status, or not generated reason>

### Residual Risk

- <risk or "No known residual risk beyond untested environments.">

### Next Step

- <one concrete next action, or "None required.">
```

Use this structure when the task is complex. For small tasks, compress it into a short paragraph while keeping the same facts.
