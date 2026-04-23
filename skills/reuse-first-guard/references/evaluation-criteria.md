# Evaluation Criteria

## Quick Checklist

Use this checklist before recommending custom build:

1. Does the framework or hosting platform already solve most of the need?
2. Is there a managed service that removes operational burden?
3. Is there a mature open-source option with acceptable maintenance cost?
4. Can code generation cover the non-differentiated glue work?
5. Does custom build create long-term ownership that the team actually wants?

If the answer to any of the first four questions is a clear "yes", custom build needs justification.

## Reuse Path Order

Check options in this order and stop when one path is clearly strong enough:

1. Official capability
2. Managed service / SaaS
3. Mature open-source library or starter
4. Generate the thin layer
5. Build from scratch

Use the strongest viable path as the baseline recommendation.

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
- Is this area a commodity capability or a business differentiator?
- What is the real constraint: delivery speed, cost, compliance, security, performance, lock-in, or control?
- Does the team already operate a proven tool in this area?
- Would custom build create meaningful product advantage, or only maintenance burden?

## Allow-Custom-Build Exceptions

Recommend or conditionally allow custom build only when at least one of these is true:

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

- Default bias: mature validation library or form framework
- Custom build bias: low
- Typical reasons against custom build: repeated edge cases, UX drift, inconsistent validation behavior

### File Upload and File Handling

- Default bias: native file input for selection, then proven upload library or platform integration for real upload workflows
- Custom build bias: very low once requirements include dedupe, queueing, retries, progress, validation, or async upload lifecycle
- Typical reasons against custom build: duplicate state bugs, edge-case explosion, accessibility drift, retry/error complexity, backend coupling
- Special note: if backend upload is not defined yet, stop at the thinnest local shell and do not grow a demo chooser into a custom uploader

### Workflow or Orchestration

- Default bias: existing workflow engine or platform feature
- Custom build bias: conditional
- Typical reasons to allow custom build: business-specific orchestration logic is the product core

## Suggested Language

Use direct language:

- "This looks like a commodity capability, so custom build is not the default."
- "A managed option removes most of the maintenance burden here."
- "Custom build is only justified if you need control for compliance, security, performance, or core differentiation."
- "I recommend a short POC before committing to custom build."
