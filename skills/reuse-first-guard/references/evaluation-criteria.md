# Evaluation Criteria

## Quick Checklist

Use this checklist before recommending custom build:

1. Does the current codebase already contain a module, page, component, adapter, helper, test, fixture, template, starter, or demo with the same technical shape?
2. Does the framework or hosting platform already solve most of the need?
3. Is there a managed service that removes operational burden?
4. Is there a mature open-source option with acceptable maintenance cost?
5. Can code generation cover the non-differentiated glue work?
6. Does custom build create long-term ownership that the team actually wants?

If the answer to any of the first five questions is a clear "yes", custom build needs justification.

## Reuse Path Order

Check options in this order and stop when one path is clearly strong enough:

1. Current codebase implementation, example, template, fixture, or test pattern
2. Official capability from the already chosen framework or platform
3. Managed service / SaaS
4. Mature open-source library or starter
5. Generate the thin layer
6. Build from scratch

Use the strongest viable path as the baseline recommendation.

## Project-Local Reuse

Treat the current repository as the first reuse surface. Before recommending a new abstraction, dependency, or from-scratch implementation, check whether the surrounding code already has the same technical shape.

Look for:

- same responsibility shape: modules, services, controllers, DTOs, adapters, guards, middleware, jobs, workers, and tests
- same UX shape: pages, routes, forms, tables, filters, drawers, modals, tabs, state views, and browser-test flows
- same governance shape: permissions, audit, error handling, validation, idempotency, observability, naming, and file layout
- vendored framework examples, playgrounds, generated starters, internal templates, fixtures, seeds, and mocks

Prefer this order when a local pattern exists:

1. Reuse the existing API/component directly.
2. Copy and adapt the nearest proven local example.
3. Add a thin extension point to the existing pattern.
4. Write only the missing delta.

Do not treat a new business object as proof that the technical implementation must be new.

## Visual Layer vs Behavior Layer

When the user wants custom UI, do not assume the behavior must also be custom-built.

Use this split by default:

- Visual layer: layout, styling, tokens, motion, branding, copy presentation
- Behavior layer: accessibility semantics, focus management, keyboard behavior, validation state, file selection, queue state, retries, async lifecycle

Decision rule:

1. Keep custom UI if needed for product fit.
2. Reuse native browser capability or headless primitives for behavior first.
3. Only allow custom behavior when reuse options clearly fail a real constraint.

If the task is drifting from custom visuals into custom commodity state management, stop and re-run the reuse-first decision.

## Decision Questions

Use the smallest useful question set:

- What new thing is being introduced: dependency, service, infrastructure, module, or major refactor?
- What existing local implementation has the closest technical shape?
- Is this area a commodity capability or a business differentiator?
- What is the real constraint: delivery speed, cost, compliance, security, performance, lock-in, or control?
- Does the team already operate a proven tool in this area?
- Would custom build create meaningful product advantage, or only maintenance burden?

## Allow-Custom-Build Exceptions

Recommend or conditionally allow custom build only when at least one of these is true:

- The user explicitly asked for a fresh implementation or no reuse.
- A documented project-local reuse check found no suitable existing pattern.
- The capability is a core business differentiator.
- Compliance, privacy, or data residency rules rule out standard hosted options.
- Security requirements exceed what reasonable reuse options can provide.
- Performance or scale constraints make common options insufficient.
- Vendor lock-in is strategically unacceptable.
- Long-term TCO is clearly lower than adopting and operating reuse options.

Prefer "Conditionally" over "Yes" when the rationale is plausible but still needs proof through a prototype, benchmark, or risk check.

## Lightweight Comparison Dimensions

When Stage 2 is needed, compare only the dimensions that can change the decision:

- Delivery speed
- Operational complexity
- Direct cost
- Maintenance cost
- Ecosystem maturity
- Security and compliance fit
- Performance headroom
- Migration or exit cost

Do not turn this into a full procurement memo unless the user explicitly asks.

## Common Scenario Patterns

### Authentication

- Default bias: official auth solution, hosted auth provider, or mature auth framework
- Custom build bias: very low
- Typical reasons against custom build: security surface, compliance burden, maintenance burden

### Payments

- Default bias: existing payment platform or PSP integration
- Custom build bias: almost never for payment rails
- Typical reasons against custom build: compliance, liability, reconciliation complexity

### Search

- Default bias: hosted search or established search engine integration
- Custom build bias: low unless search quality is the product itself
- Typical reasons against custom build: indexing complexity, ranking maintenance, ops burden

### Forms and Validation

- Default bias: current local form/schema/test pattern, then mature validation library or form framework
- Custom build bias: low
- Typical reasons against custom build: repeated edge cases, UX drift, inconsistent validation behavior

### File Upload and File Handling

- Default bias: native file input for selection, then proven upload library or platform integration for real upload workflows
- Custom build bias: very low once requirements include dedupe, queueing, retries, progress, validation, or async upload lifecycle
- Typical reasons against custom build: duplicate state bugs, edge-case explosion, accessibility drift, retry/error complexity, backend coupling
- Special note: if backend upload is not defined yet, stop at the thinnest local shell and do not grow a demo chooser into a custom uploader

### Workflow or Orchestration

- Default bias: existing local workflow pattern, then workflow engine or platform feature
- Custom build bias: conditional
- Typical reasons to allow custom build: business-specific orchestration logic is the product core

## Suggested Language

Use direct language:

- "This looks like a commodity capability, so custom build is not the default."
- "This repo already has a nearby pattern; copy and adapt that before creating a parallel implementation."
- "A managed option removes most of the maintenance burden here."
- "Custom build is only justified if you need control for compliance, security, performance, or core differentiation."
- "I recommend a short POC before committing to custom build."
