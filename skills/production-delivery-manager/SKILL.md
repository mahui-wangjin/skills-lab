---
name: production-delivery-manager
description: Use when the user explicitly names this skill, asks for production-grade / complete / release-ready / high-assurance / quality-first / strict / zero-ambiguity engineering delivery, wants a senior technical lead to coordinate implementation and acceptance, asks for multi-agent/team-led delivery, needs worktree/workspace hygiene for risky or parallel engineering work, or needs a human-validation packet / HTML delivery report with architecture, core logic, verification evidence, screenshots, CI/workflow evidence, steelman review, and residual risks.
---

# Production Delivery Manager

## Purpose

Use this skill to turn a non-trivial engineering request into a controlled delivery loop with explicit gates, bounded delegation, delivery-target integration, verification evidence, and a steelman counter-review.

Production-grade means "passed the agreed gates with known residual risks." Do not claim bug-free, risk-free, or complete production safety unless the verification evidence actually proves it.

Production-grade delivery also means the user can validate the result without reading the entire diff. For medium, complex, production-grade, or user-requested report work, translate the implementation into a human validation surface: architecture review points, core logic flow, evidence map, steelman summary, residual risks, and explicit human checkpoints. Reports are finalization artifacts: keep terse evidence notes while implementing, then generate or update the HTML report after delivery-target integration and verification unless the user explicitly asked for a report-first artifact.

Result-first handoff is mandatory. The user cares about final outcomes, key changes, verification, residual risk, and next steps; do not make the final answer, HTML report, or project docs read like an implementation diary.

This skill coordinates other specialist skills and tools. Do not replace a more specific skill when one clearly applies; invoke or follow the specific skill at the relevant gate.

The lead agent is accountable for delivery quality, not just task velocity. When the user explicitly asks for strict, production-grade, high-assurance, team-led, or quality-first delivery, do not silently downgrade the work into a single-agent implementation unless the task is genuinely simple and the no-delegation reason is stated.

## Activation Rule

Activate this skill when one of these is true:

- The user explicitly names `$production-delivery-manager` or asks to use the engineering delivery / production delivery manager skill.
- The user explicitly asks for production-grade, complete production-level, release-ready, high-assurance, quality-first, strict delivery, no ambiguous requirements, team-led delivery, final acceptance, or an equivalent end-to-end engineering delivery standard.
- The user asks for a lead/manager agent to coordinate multiple agents through implementation, review, verification, and handoff.

## Operating Discipline

Avoid process theater:

- For simple tasks, do the work directly and report verification and risk briefly.
- For medium tasks, use a compact plan and one verification pass.
- For complex or production-grade tasks, use the full gate sequence and make a visible delegation decision.
- Ask only questions that can change scope, architecture, safety, or acceptance.
- Do not block on perfect requirements when a reversible, explicitly scoped slice can be delivered safely.
- Do not continue implementation when ambiguity affects data loss, security, permission, payment, migration, or irreversible behavior.
- Treat explicit quality-first or strict production delivery requests as complex by default. Downgrade only when the work is narrow, low-risk, reversible, and independently verifiable.
- If real sub-agents are unavailable or not useful, say so and perform labeled self-review perspectives. Do not pretend a single self-review is equivalent to independent review.
- Do not make the user reverse-engineer quality from raw diffs, command logs, CI job names, or screenshots. Surface the few architecture, core logic, evidence, and risk points that need human acceptance.
- Do not write or polish the final HTML report during core implementation. Capture only short evidence notes: command/check, result, artifact path, what it proves, and limitation.
- Generate the durable report at finalization from verified evidence. If a long-running task needs a report directory early, use it only as an artifact bucket until verification is complete.
- Do not write process logs, debug chronology, agent transcripts, repeated attempts, or command-by-command narratives into existing project docs.
- Before editing documentation, route the content: long-lived product/architecture/API/decision facts belong in project docs; final validation belongs in the handoff or `.production-delivery-reports/`; transient evidence notes stay in working notes unless the repository explicitly has an approved audit/evidence artifact location.

## Delivery Loop

Follow this sequence for implementation, refactor, integration, debugging, migration, release, or production-quality UI work:

1. Intake
2. Discovery
3. Workspace isolation
4. Delivery plan
5. Implementation
6. Delivery-target integration
7. Verification
8. Steelman counter-review
9. Human validation handoff

For small tasks, compress the loop, but do not skip verification or risk reporting.

For detailed gates and output shapes, read [delivery-gates.md](./references/delivery-gates.md) before planning a complex task.

For adversarial review, read [steelman-review.md](./references/steelman-review.md) before final acceptance or after any substantial implementation.

For human validation packets, HTML delivery reports, evidence directories, screenshot handling, CI/workflow evidence, report trigger rules, and the report scaffold script, read [human-validation-report.md](./references/human-validation-report.md) during finalization for complex or production-grade work, browser/UI acceptance, release-candidate work, or whenever the user asks for a report. Do not let report drafting interrupt implementation unless report creation is the requested task.

For sub-agent use, read [delegation-patterns.md](./references/delegation-patterns.md) when parallel work, specialist review, or bounded implementation ownership would help. For complex or production-grade work, read it before deciding not to delegate.

## Gate Rules

### 1. Intake

Identify:

- user goal
- user-visible acceptance criteria
- scope and non-goals
- risk level
- whether the task is simple, medium, or complex
- whether the user asked for quality-first, production-grade, strict delivery, or multi-agent/team-led execution

If requirements are unclear, ask the smallest number of blocking questions. If work can proceed under assumptions, state the assumptions and mark them as open.

If a request is production-grade or quality-first, classify it as complex unless the exception is obvious and documented. "I can do it myself faster" is not a valid downgrade reason.

### 2. Discovery

Before implementation:

- inspect project rules and source-of-truth docs
- use structural code search when available, such as CodeGraph for symbols and call flows
- use project knowledge graphs when the task spans docs, architecture, or decisions
- check current codebase patterns before creating new modules
- use official docs for version-sensitive framework, SDK, API, or platform behavior

If `reuse-first-guard` is available and the task introduces a module, dependency, service, page, component, workflow, adapter, or major refactor, invoke it before custom build decisions.

If a domain-specific skill is available, use it at the relevant gate:

- source/documentation skill for version-sensitive APIs
- test-driven skill for behavior changes with meaningful logic
- frontend delivery skill for UI fidelity and interaction polish
- security or database review skill for high-risk boundaries
- shipping skill for launch or rollout readiness

### 3. Workspace Isolation

Before planning edits, decide whether the current workspace is safe to use:

- run `git status --short` when inside a Git repository
- record the original workspace path, current branch, and intended delivery target before creating a branch or worktree
- treat local uncommitted or untracked changes as context, not an automatic blocker
- identify unrelated user changes and avoid touching those files
- continue in the current workspace when user changes are unrelated, non-overlapping, and the task's final validation target is that workspace
- use a dedicated branch or git worktree for large changes, risky refactors, multi-agent implementation, long-running work, or when preserving the user's current workspace matters
- treat an isolated branch or worktree as a candidate execution surface, not the default final delivery surface
- if the user made the request from the main/current workspace and did not ask for a PR-only or branch-only deliverable, make the original workspace/current branch the default delivery target
- before working in a separate branch or worktree, state how the result will be returned: merge, cherry-pick, patch application, PR/branch handoff, or explicit "not applied to original workspace"
- pause, ask, or isolate only when local changes overlap the intended edit scope, make user intent unclear, or raise irreversible risk
- do not create a separate worktree for tiny docs-only or one-file reversible edits unless the user asks
- when using parallel agents, assign non-overlapping file/module scopes; use separate worktrees for parallel code-writing agents when overlap risk is real

If `superpowers:using-git-worktrees` is available and the task needs isolation, use it before implementation. If no worktree is used, state why the current workspace is acceptable.

### 4. Delivery Plan

For medium or complex tasks, emit a short plan that includes:

- objective
- boundaries and non-goals
- workspace decision: current workspace, branch, or worktree
- delivery target and integration method if implementation is isolated
- file/module ownership
- role split if using sub-agents
- verification commands or manual checks
- rollback or mitigation notes when relevant

Do not assign two agents to overlapping write scopes unless one is explicitly review-only.

### 4.5. Delegation Quality Gate

Before implementation on complex, production-grade, or quality-first work, decide and report:

- which roles are needed for implementation, architecture review, risk review, verification, docs, or release
- which roles get real sub-agents, which roles are handled locally, and why
- which files or modules each code-writing agent owns
- which reviewers are read-only and what acceptance risks they must challenge
- whether any critical path work stays with the lead agent because delegation would block progress

Default for complex or production-grade delivery: use at least one independent specialist perspective for review, verification, architecture, security, database, frontend, or E2E risk unless no real sub-agent facility exists or the task's scope is genuinely too narrow. When no real delegation is used, include a no-delegation note in the plan and revisit it in the steelman review.

Do not use sub-agents as theater. Delegation must create non-overlapping ownership or an independent review surface that can change the result.

### 5. Implementation

Implement incrementally:

- prefer the nearest local pattern
- keep edits scoped
- avoid unrelated refactors
- preserve user changes
- keep temporary files, test artifacts, and local-only outputs out of the final diff unless they are intentional deliverables
- update docs or approved audit/evidence artifacts when the project rules require it
- keep interfaces explicit and testable

Document routing rule:

- Update project docs only with durable facts: accepted decisions, architecture boundaries, public contracts, operating rules, product behavior, or explicit follow-up commitments.
- Do not put process logs, temporary evidence notes, raw verification output, sub-agent notes, or chronological implementation records into existing product, architecture, development, or governance docs.
- If the project has no explicit approved audit/evidence artifact, do not create one just to store process notes. Use the final handoff or `.production-delivery-reports/` when durable validation evidence is required.
- If a process artifact is intentionally persisted, put it in the report evidence area or a project-approved audit/evidence artifact path, label it as evidence, and keep formal docs result-oriented.

When the task is large, land one coherent slice at a time and verify before broadening.

### 6. Delivery-Target Integration

Before final verification, ensure the implemented change is present in the agreed delivery target:

- if work happened in the current workspace, confirm the changed files and branch/workspace are the intended target
- if work happened in a branch or worktree, merge, cherry-pick, or apply the patch back to the agreed target when safe and within user instructions
- if integration is blocked by conflicts, dirty overlapping files, missing permissions, or user preference, stop and report the task as not applied to the delivery target
- do not claim completion from an isolated worktree unless the user explicitly accepted that branch/worktree/PR as the deliverable
- after integration, run `git status --short` in the delivery target and report any unrelated remaining changes separately from the task diff

### 7. Verification

Verification must match risk:

- code-only change: targeted tests, typecheck, lint, or build where available
- backend behavior: unit/integration tests, API contract checks, migration checks, logs/error paths
- frontend behavior: build plus browser/runtime checks for critical flows and responsive states
- security/data change: permission, validation, tenant/data isolation, audit, and failure-path checks
- docs-only change: governance checks, link/path checks, or diff review as applicable

Run final verification from the delivery target, not only from the isolated worktree, unless the agreed deliverable is explicitly a branch or PR. If only worktree verification was possible, report the result as partial and state that the original workspace/target branch was not verified.

If a command cannot run, report why and provide the next best verification path. Do not describe unrun checks as completed.

If complex or production-grade work proceeds without real sub-agents or independent reviewers, compensate with stronger objective evidence where practical: targeted tests, typecheck, lint, build, contract checks, migration checks, browser/E2E runs, security/database checks, or documented manual inspection. If the missing independent perspective cannot be compensated, downgrade the claim to partial, candidate, or self-reviewed.

### 8. Steelman Counter-Review

Before final completion on substantial work, run a steelman counter-review:

- argue the strongest case that the solution is wrong, incomplete, unsafe, overbuilt, under-tested, or mis-scoped
- compare against requirements, existing architecture, test evidence, and likely production failure modes
- either fix the issue, downgrade the completion claim, or document residual risk

Use an independent reviewer sub-agent when available and the review can run in parallel. Otherwise perform the review yourself from a fresh skeptical stance.

For complex or production-grade work, steelman must challenge the delegation choice: if the lead agent implemented, reviewed, and verified everything alone, explain why that was acceptable or downgrade the completion claim.

### 9. Human Validation Handoff

Final handoff must include:

- what changed
- how it was verified
- workspace, branch/worktree, integration, and cleanup status
- what remains risky or unverified
- what the user should do next, if anything

Final handoff must be result-first:

- Lead with delivered capabilities and final state.
- Summarize key changes by outcome or boundary, not by chronological steps.
- Include final verification evidence and what it proves.
- Include residual risks and concrete next steps.
- Exclude iteration history, repeated failed attempts, raw command dumps, and "then I did..." narration unless the user explicitly asks for an audit trail.

For medium and complex work, include a compact Human Validation Packet. For complex, production-grade, release-candidate, browser-heavy, migration/security/data-risk work, or when the user asks for a report, generate or update an HTML report under `.production-delivery-reports/<YYYY-MM-DD>_<slug>/index.html` from the final evidence notes unless repository policy or user preference blocks it. If no report is produced when a trigger applies, state why and downgrade the claim if the missing report weakens user validation.

Keep the final answer concise, but never omit failed checks or residual risks.

## Role Policy

The lead agent owns final quality. Sub-agents may explore, implement, test, or review, but they do not own final acceptance.

Use specialists when they materially improve the result. For complex or production-grade work, assume specialists will improve quality unless a concrete exception applies:

- Planner / Architect for unclear scope or broad design
- Research / Docs for version-sensitive or source-backed decisions
- Backend / Frontend / Database for disjoint implementation slices
- Security / Reviewer for high-risk boundaries
- Test / E2E for validation and regression checks
- Docs / Release for handoff, changelog, and launch readiness

When no real sub-agent facility exists, simulate these perspectives internally and label conclusions as self-reviewed.

Do not let the lead agent become the only implementer, reviewer, tester, and release judge for a risk-bearing product change merely to save time. The lead may keep critical-path work local, but must still create an independent challenge surface through real sub-agents or explicit self-reviewed specialist perspectives.

## Completion Standard

Do not mark a task complete unless:

- acceptance criteria are satisfied or explicitly adjusted
- implementation is finished for the agreed scope
- changes are present in the agreed delivery target, or the user explicitly accepted an unapplied branch/worktree/PR handoff
- verification evidence is reported
- steelman objections are handled or documented
- for complex or production-grade work, the handoff reports the delegation decision, the independent challenge surface used, and any no-delegation reason or self-reviewed downgrade
- for medium or complex work, the handoff includes a Human Validation Packet that exposes architecture review points, core logic, evidence, steelman result, human checkpoints, and residual risks
- when report triggers apply, the HTML delivery report exists in `.production-delivery-reports/` and is generated from verified evidence, or the final handoff explains why it was not generated and what evidence replaces it
- residual risks and next steps are clear

If any condition is not met, report the task as partially complete, blocked, or needing user decision.
