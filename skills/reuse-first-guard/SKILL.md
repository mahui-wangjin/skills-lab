---
name: reuse-first-guard
description: Enforce a reuse-first decision gate before building from scratch. Use when a task introduces a new dependency, third-party service, infrastructure capability, custom module, major refactor, or a likely wheel-rebuild area such as auth, payments, search, storage, messaging, forms, CMS, analytics, monitoring, or workflow tooling. When this skill is active, emit the fixed `### Reuse-First Check` and `### Decision` template before repository exploration, memory reads, planning, or implementation.
---

# Reuse First Guard

## Gate First

This skill is a gate, not an exploration workflow.

When active:

- Start with the fixed template immediately.
- Do not read repository files first.
- Do not read project memory first.
- Do not inspect docs or config first.
- Do not make a plan first.
- Do not add freeform introduction or closing summary.

If information is missing, still emit the template and put the single most important follow-up question in `Next step`.

## Trigger

Use this skill before implementation when the task:

- adds a new dependency
- adds a third-party service
- adds infrastructure or platform capability
- creates a new custom module
- proposes a major refactor
- looks like rebuilding a common capability

Treat these as default hot spots:

- authentication and authorization
- payments and billing
- search
- storage and file handling
- messaging and notifications
- forms and validation
- file upload and file handling
- CMS and content workflows
- analytics, logging, and monitoring
- workflow and orchestration tooling

If the task does not change technical direction or ownership, skip this skill.

## Decision Rule

Check options in this order:

1. Official capability
2. Managed service or SaaS
3. Mature open-source library, template, or starter
4. Code generation or AI-assisted generation
5. Custom build

For UI-heavy commodity capabilities, separate visual layer from behavior layer:

- Keep custom UI when it is mainly presentation.
- Prefer native browser capability or headless / unstyled primitives for behavior, accessibility, focus management, validation, and state transitions.
- Do not jump from "we want custom visuals" to "we should also custom-build the state machine".

For forms, pickers, dialogs, uploads, and similar interaction controls, apply this sub-order:

1. Native browser capability
2. Existing framework primitive or official capability
3. Mature headless / unstyled library
4. Mature domain library for the capability
5. Thin adapter around the chosen path
6. Custom build

Special rule for upload and file handling:

- If there is no confirmed backend upload contract yet, stop at native file selection plus the thinnest possible local state shell.
- Do not continue expanding a demo shell into a custom upload queue, dedupe engine, retry flow, progress system, or validation matrix by default.
- If real upload behavior is required, prefer a mature upload library or proven platform integration before extending local custom logic.

If a lower-cost or lower-maintenance reuse path is clearly viable, do not default to custom build.

Allow direct custom build only when at least one of these is clearly true:

- core business differentiation
- compliance or data sovereignty
- security requirement
- performance requirement
- unacceptable vendor lock-in
- long-term TCO clearly better than reuse

Use `Conditionally` when custom build may be justified but still needs proof.

Read [evaluation-criteria.md](./references/evaluation-criteria.md) only when you need more detailed trade-off prompts, exception tests, or scenario patterns.

## Output Template

Use this exact structure every time:

```md
### Reuse-First Check

- Trigger: <why this gate applies>
- Reuse paths checked: <official / SaaS / open source / generate>
- Recommendation: <recommended path>
- Why not custom build by default: <1-3 concise reasons>

### Decision

- Allow direct custom build: <No / Conditionally / Yes>
- If custom build continues, required justification: <reason or constraint>
- Next step: <one concrete next action or one focused question>
```

Formatting rules:

- The first line must be `### Reuse-First Check`.
- Always include both sections.
- Do not add text before the first heading.
- Do not add text after the last bullet.
- Keep bullets short and concrete.

## After The Gate

Only after emitting the template may you:

- ask one focused question
- inspect the repository
- read docs or memory
- move into planning or implementation

If the user only wants the gate decision, stop after the template.
