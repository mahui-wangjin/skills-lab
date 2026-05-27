---
name: maintainability-guard
description: Guard long-term code maintainability before adding behavior to large, mixed-responsibility, or likely-reused code. Use before modifying any source file, module, page, service, job, script, test helper, or component when file size is growing, responsibilities are mixing, reuse is likely, tests are hard to write, dependency direction is unclear, or the task risks continuing a "just patch the same file" pattern. Emit a maintainability gate before planning or implementation when the target file is over 800 lines, the module has multiple change reasons, or the user asks about maintainability, extensibility, architecture, refactoring, or avoiding overgrown code.
---

# Maintainability Guard

## Purpose

Use this skill to decide whether a change can safely continue in place or must first split responsibilities, clarify interfaces, or reduce coupling.

This is not a small-file rule. Do not split code just because it is long. Split when boundaries are unclear, change reasons diverge, reuse appears, testing is hard, or implementation details leak across modules.

## Core Principles

Apply these principles to any stack, language, or framework:

- **Single change reason:** A module should have one primary reason to change.
- **Separation of concerns:** Business rules, interface adaptation, persistence, permission checks, audit, scheduling, rendering, and presentation transforms should not remain tangled.
- **High cohesion, low coupling:** Keep logic that changes together close. Keep unrelated concepts from knowing each other's internals.
- **One abstraction level:** A function or method should not mix domain decisions with SQL, DOM, HTTP, file-system, queue, or framework details.
- **Change-axis fit:** Things that evolve together can stay together. Things that evolve independently deserve a boundary.
- **Test boundary:** Logic that cannot be tested through a stable interface usually has an unclear boundary.
- **Dependency direction:** Stable domain rules should not depend on volatile framework, database, UI, transport, or vendor details.
- **Stable contracts:** Modules should collaborate through named inputs, outputs, errors, events, and side effects, not by reaching into internal state.

## Trigger Thresholds

Line count is an alarm, not a verdict.

Use these thresholds to trigger review:

| Size | Default action |
| --- | --- |
| `< 400` lines | Continue normally unless responsibilities are already mixed. |
| `400-800` lines | Watch for a second responsibility or second use case. |
| `800-1200` lines | Emit the maintainability gate before adding behavior. |
| `1200-2000` lines | Require a written reason to continue in place, or split one clear responsibility first. |
| `> 2000` lines | Do not add new business behavior until a structure-recovery slice is planned. Bug fixes may be allowed if narrowly scoped. |
| `> 3000` lines | Treat as a maintainability incident. Plan recovery before feature work. |

Treat reusable or foundational code more strictly. A poor boundary in reused code spreads complexity to every caller.

## Maintainability Gate

Before planning or implementation, emit this gate:

```md
### Maintainability Gate

- Target: <file/module/function/component/job/etc.>
- Current size and shape: <line count if known, main responsibilities>
- Change being added: <new behavior or responsibility>
- Trigger: <size / mixed responsibility / reuse / test difficulty / dependency direction / user concern>

### Boundary Assessment

- Single change reason: <Pass / Risk / Fail>
- Concern separation: <Pass / Risk / Fail>
- Cohesion and coupling: <Pass / Risk / Fail>
- Abstraction level: <Pass / Risk / Fail>
- Change-axis fit: <Pass / Risk / Fail>
- Test boundary: <Pass / Risk / Fail>
- Dependency direction: <Pass / Risk / Fail>
- Stable interface: <Pass / Risk / Fail>

### Decision

- Continue in place: <Yes / Conditionally / No>
- Required action before feature work: <none / small extraction / interface clarification / structure-recovery slice>
- Do not split: <what must stay together and why>
- Split candidate: <specific responsibility to extract, if any>
- Verification: <tests, typecheck, lint, architecture check, or manual review>
```

Keep the gate concise. It should help the user decide, not become process theater.

## Decision Rules

### Continue In Place

Continue in place when most of these are true:

- The module has one clear responsibility.
- The new change belongs to the same change reason.
- No second caller or reuse scenario exists.
- Tests can cover the behavior through the existing public interface.
- Dependencies still point in the correct direction.
- Extraction would create pass-through files or vague names.

### Split First

Split before feature work when any of these are true:

- One file now owns three or more independent responsibilities.
- A second real use case or caller appears.
- Callers must understand internal ordering, flags, storage shape, permission details, rendering details, or framework lifecycle.
- Tests need to reach into private internals or construct a huge unrelated context.
- A high-level rule depends directly on low-level details.
- The same mapping, validation, permission, status, rendering, or adapter logic is duplicated.
- A future change would require editing several unrelated sections of the same large file.

### Do Not Over-Split

Do not extract when:

- The only reason is line count.
- The extracted module would only forward parameters.
- The new name is generic, such as `utils`, `helpers`, `manager`, `common`, or `misc`.
- There is only one caller, one use case, and no independent test or change reason.
- The extraction makes callers know more details than before.
- The split separates logic that always changes together.

## Boundary Patterns

Prefer boundaries that hide details behind a small contract:

- **Entry orchestration:** Coordinates the use case, delegates details.
- **Domain rule:** Holds stable business decisions without framework or I/O details.
- **Adapter:** Converts between external shapes and internal contracts.
- **Persistence boundary:** Owns storage queries and transaction-specific details.
- **Permission boundary:** Centralizes authorization decisions and denial reasons.
- **Audit/observability boundary:** Records evidence without taking over business flow.
- **Presentation boundary:** Converts data for UI or output without owning domain state.
- **Reusable interaction boundary:** Exposes a focused API for repeated UI or workflow behavior.

These names are examples of responsibility shapes, not required folders. Adapt them to the project's framework.

## Framework Examples

Use examples only to recognize responsibility shape:

- In a UI project, a page that owns data loading, table columns, dialogs, permission rules, charts, import/export, and audit views should usually split presentation blocks, state hooks, constants, and adapters.
- In a backend project, an endpoint handler that owns request parsing, validation, permission checks, transaction control, persistence, domain decisions, and audit logging should usually delegate to explicit boundaries.
- In a worker or job project, scheduling, claiming, execution, retry, compensation, and audit should not all remain tangled once the workflow becomes production-critical.
- In a script-heavy project, parsing, planning, file mutation, error reporting, and CLI output deserve separate functions once reuse or testing matters.

Do not turn these examples into universal folder names.

## Structure-Recovery Slice

When a file is already too large, do not attempt a full rewrite by default.

Use a small recovery slice:

1. Identify one named responsibility that can move with minimal behavior change.
2. Define its public contract: inputs, outputs, errors, side effects.
3. Move only that responsibility.
4. Keep call sites boring and explicit.
5. Run targeted verification.
6. Stop unless the next extraction is equally obvious.

Prefer "one clear extraction that reduces future change cost" over a broad architectural rewrite.

## Verification

Match verification to the boundary:

- Extracted pure logic: unit tests or focused contract tests.
- UI extraction: typecheck plus runtime/browser check for the affected state.
- Backend extraction: unit/integration tests for success, denial, error, transaction, and audit paths as relevant.
- Dependency boundary: lint, dependency-cruiser, Semgrep, or review of import direction.
- Size gate: line-count or complexity script, if available.

If no automated check exists, report that and provide the smallest manual review checklist.
