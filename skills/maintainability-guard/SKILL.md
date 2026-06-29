---
name: maintainability-guard
description: Use when adding or changing source files, modules, pages, services, jobs, scripts, smoke/E2E/browser automation tests, validation scripts, test helpers, or components where file size is growing, responsibilities are mixing, reuse or duplication is likely, tests are hard, dependency direction is unclear, or the task risks continuing a "just patch the same file" pattern; also when the user asks about maintainability, extensibility, architecture, refactoring, code splitting, test script bloat, or avoiding overgrown code.
---

# Maintainability Guard

## Purpose

Use this skill to decide whether a change can safely continue in place or must first split responsibilities, clarify interfaces, or reduce coupling.

Test and automation code is code. Apply this skill to smoke scripts, E2E tests, browser automation, validation/reporting scripts, fixtures, selectors, and helpers with the same seriousness as application code.

This is not a small-file rule. Do not split code just because it is long. Split when boundaries are unclear, change reasons diverge, reuse appears, testing is hard, or implementation details leak across modules.

It is also not a large-file-only rule. Small files can fail maintainability when they introduce a reusable rule, a second change axis, duplicated mapping, hidden dependency direction, or a hard-to-test boundary.

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

## Always-On Boundary Check

Before modifying code, perform this lightweight check even when the target is under 400 lines:

1. What responsibility is being added or changed?
2. Is it a domain rule, adapter, persistence detail, permission rule, status transition, mapper, formatter, presentation transform, reusable interaction, or orchestration step?
3. Does a second caller, second use case, likely follow-up use case, or similar existing implementation exist?
4. Would tests become simpler if this behavior had a named input/output contract?
5. Would extraction hide details, or would it only create a pass-through wrapper?
6. For test or automation code, are runner/bootstrap, fixtures, selectors, actions, assertions, screenshots/evidence, reporting, and cleanup mixed in one place?

If the answer reveals reuse, duplication, a new change reason, unclear testing, or dependency-direction risk, do not rely on line count. Emit the Maintainability Gate before planning or implementation.

## Trigger Thresholds

Line count is an alarm, not a verdict.

Use these thresholds to trigger review:

| Size | Default action |
| --- | --- |
| `< 400` lines | Continue only after the lightweight boundary check. Small files can still fail on reuse, duplication, mixed responsibility, dependency direction, or test boundary. |
| `400-800` lines | Watch for a second responsibility, second use case, repeated mapping, repeated status logic, or new abstraction level. |
| `800-1200` lines | Emit the maintainability gate before adding behavior. |
| `1200-2000` lines | Require a written reason to continue in place, or split one clear responsibility first. |
| `> 2000` lines | Do not add new business behavior until a structure-recovery slice is planned. Bug fixes may be allowed if narrowly scoped. |
| `> 3000` lines | Treat as a maintainability incident. Plan recovery before feature work. |

Treat reusable or foundational code more strictly. A poor boundary in reused code spreads complexity to every caller.

## Gate Triggers

Emit the Maintainability Gate before planning or implementation when any trigger applies:

- The target is over 800 lines.
- The module has multiple change reasons or already mixes responsibilities.
- The change introduces or modifies a reusable rule, adapter, mapper, validator, permission check, status transition, formatter, hook, workflow step, reusable UI interaction, or presentation transform.
- Similar logic exists elsewhere, or a second caller/use case is likely enough that the code would be copied soon.
- Tests would need private internals, framework lifecycle tricks, large unrelated setup, or manual-only verification.
- A high-level decision depends directly on database, transport, DOM, queue, vendor, or framework details.
- A smoke, E2E, browser automation, or validation script mixes runner/bootstrap, fixtures, selectors, actions, assertions, evidence capture, reporting, and cleanup.
- A smoke test is growing into a product acceptance harness instead of staying a small health check.
- The user asks about maintainability, extensibility, architecture, refactoring, reuse, avoiding overgrown code, or why agents keep patching the same file.

## Maintainability Gate

Before planning or implementation, emit this gate:

```md
### Maintainability Gate

- Target: <file/module/function/component/job/etc.>
- Current size and shape: <line count if known, main responsibilities>
- Change being added: <new behavior or responsibility>
- Trigger: <size / mixed responsibility / reuse / duplication / test difficulty / dependency direction / user concern>
- Always-on check: <new responsibility, caller/use-case count, reuse/duplication signal, test boundary signal>

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
- Contract if split: <inputs, outputs, errors, side effects, owner>
- Verification: <tests, typecheck, lint, architecture check, or manual review>
```

Keep the gate concise. It should help the user decide, not become process theater.

## Decision Rules

### Continue In Place

Continue in place when most of these are true:

- The module has one clear responsibility.
- The new change belongs to the same change reason.
- No real or likely second caller, second use case, or duplication scenario exists.
- Tests can cover the behavior through the existing public interface.
- Dependencies still point in the correct direction.
- Extraction would create pass-through files or vague names.
- The lightweight boundary check did not reveal a reusable rule, adapter, mapper, permission check, status transition, formatter, workflow step, or presentation transform.

### Split First

Split before feature work when any of these are true:

- One file now owns three or more independent responsibilities.
- A second real use case or caller appears.
- A second likely use case is close enough that the next agent would probably copy the same logic.
- Callers must understand internal ordering, flags, storage shape, permission details, rendering details, or framework lifecycle.
- Tests need to reach into private internals or construct a huge unrelated context.
- A high-level rule depends directly on low-level details.
- The same mapping, validation, permission, status, rendering, or adapter logic is duplicated.
- A future change would require editing several unrelated sections of the same large file.
- The host file is small but the new behavior has a different change reason from the host.

### Do Not Over-Split

Do not extract when:

- The only reason is line count.
- The extracted module would only forward parameters.
- The new name is generic, such as `utils`, `helpers`, `manager`, `common`, or `misc`.
- There is only one caller, one use case, no likely second use case, no duplication, and no independent test or change reason.
- The extraction makes callers know more details than before.
- The split separates logic that always changes together.

## Reuse and Extraction Test

Before choosing "continue in place" for a reusable-looking behavior, answer these checks explicitly:

- **Second-use pressure:** Where is the next realistic caller or use case? If it is named, treat reuse as real enough to design a boundary.
- **Copy pressure:** Would another agent copy this mapping, validation, permission, status, rendering, or adapter logic into another file? If yes, extract or clarify the contract now.
- **Contract pressure:** Can the behavior be named with specific inputs, outputs, errors, and side effects? If no, do not extract yet. Clarify the interface first.
- **Caller burden:** Does extraction make callers know less about ordering, flags, storage shape, rendering details, or framework lifecycle? If yes, extraction likely helps.
- **Test pressure:** Would a focused test become smaller after extraction? If yes, the boundary is probably real.

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

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is under 400 lines, so maintainability does not apply." | Small files can still introduce reusable rules, duplicate mappings, mixed change reasons, and hard-to-test boundaries. Run the lightweight boundary check. |
| "There is only one caller today." | If a second use case is already named or the next agent would copy the logic, reuse is real enough to design a contract. |
| "Do not over-split means keep it here." | Do not over-split forbids pass-through wrappers and vague names. It does not excuse duplication, hidden dependency direction, or mixed responsibilities. |
| "Extraction will take longer than patching." | If the patch spreads a rule that will be reused, the cheap patch creates future coordination cost. Prefer one small boundary with a named contract. |
| "Tests can cover it through the page/service." | Broad tests may be fine for orchestration. If the rule itself needs private setup or many unrelated dependencies, the boundary is unclear. |

## Red Flags

- You are adding a mapper, validator, permission rule, status transition, formatter, hook, adapter, or workflow step to a file that mainly does something else.
- You are about to paste similar logic from another file.
- You describe the future as "when the next page/service/job needs this..."
- Tests require mounting a full page, opening a browser, creating a database transaction, or constructing a large service graph just to check a small rule.
- Callers must know internal ordering, flags, storage shape, rendering details, or framework lifecycle.
- You are using line count as the only reason to continue in place or the only reason to split.

## Test And Automation Code

Keep smoke, E2E, browser automation, validation, and reporting code maintainable. Do not treat these files as disposable merely because they verify other code.

Use smoke tests as a narrow health gate: app starts, critical routes load, basic shell renders, and fatal console or network failures are surfaced. Do not use smoke-only results as final frontend product acceptance for layout, overlays, responsive behavior, interaction polish, screenshots, or user-visible workflow quality.

For frontend delivery, prefer real-browser E2E, agent-browser, Playwright, Cypress, or the project's accepted browser automation path for product acceptance. Smoke can support that path, but it must not replace browser-level validation when UI behavior matters.

AI-driven browser or E2E work must not become unbounded trial-and-error. Keep it evidence-oriented: explicit target flows, viewports, assertions, screenshots/traces, console/network logs, and a stopping condition. If the browser work is broad, iterative, slow, authenticated, third-party dependent, or materially high in time/token cost, confirm the acceptance budget before expanding it.

Structure automation code around explicit responsibilities:

- runner/bootstrap and environment setup
- fixtures, accounts, and test data
- selectors, page objects, and action helpers
- assertions and expected states
- screenshot, console, network, and evidence capture
- reporting, cleanup, and retry policy

If a test or automation file combines three or more of these responsibilities, emit the Maintainability Gate before adding scenarios. If it is already over 1200 lines, split one clear responsibility before expanding it except for a narrow bug fix. If it is over 2000 lines, do not add new scenarios until a recovery slice exists. If it is over 3000 lines, treat it as a maintainability incident.

## Framework Examples

Use examples only to recognize responsibility shape:

- In a UI project, a page that owns data loading, table columns, dialogs, permission rules, charts, import/export, and audit views should usually split presentation blocks, state hooks, constants, and adapters.
- In a backend project, an endpoint handler that owns request parsing, validation, permission checks, transaction control, persistence, domain decisions, and audit logging should usually delegate to explicit boundaries.
- In a worker or job project, scheduling, claiming, execution, retry, compensation, and audit should not all remain tangled once the workflow becomes production-critical.
- In a script-heavy or test-heavy project, parsing, planning, file mutation, browser/session setup, selectors, assertions, evidence capture, error reporting, and CLI output deserve separate functions once reuse or testing matters.

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
- Test automation extraction: run the affected smoke/E2E/browser command and confirm the same scenarios still execute with equivalent evidence.
- Dependency boundary: lint, dependency-cruiser, Semgrep, or review of import direction.
- Size gate: line-count or complexity script, if available.

If no automated check exists, report that and provide the smallest manual review checklist.
