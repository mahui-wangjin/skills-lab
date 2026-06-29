# Decision And Scope Rules

Use this reference when routing, source precedence, frontend foundation ownership, shell preservation, API scope, browser budget, or polish scope is unclear.

## Ask One Critical Question

Ask only one critical question at a time, and only when the answer can change routing, scope, implementation ownership, or acceptance.

Ask before implementation when:

- target stack is not specified and repository stack is not clear;
- strong sources conflict on structure, primary flow, interaction path, or acceptance criteria;
- existing project and new design/HTML are both present but intent is unclear;
- only visual artifacts are provided and no stronger source is available;
- a design platform appears capable of structured context but cannot be accessed after a real attempt;
- the project appears to have frontend foundation systems but the correct owner cannot be determined after a real attempt;
- shell, route frame, common surface, or layout preservation is unclear;
- required source-backed assets, icons, fonts, component variants, borders, states, or motion details cannot be located;
- API/BFF scope is requested but contract, side effects, cache, authorization, or regression surface is unclear;
- browser acceptance would require high-cost exploratory E2E.

## Decide Without Asking

Decide without asking when the repository or source evidence is clear:

- structured platform context, generated code, tokens, component mappings, or exported HTML are available: use them as source and use screenshots only for validation;
- target stack is unstated but the current project stack is explicit;
- an existing layout, page archetype, component, token/theme, table/list/form pattern, route metadata, permission rule, overlay root, or shared shell clearly fits: reuse it;
- the change is a small local fix whose owner and regression surface are obvious;
- minimum browser acceptance is scoped to the changed page or flow.

## Scope Gaps

In `polish-existing-project`, run scope-gap detection after current-state audit.

If the named scope is not enough for a demo-ready result, report:

- named scope;
- uncovered layers or states;
- expected completion level if only the named scope is done;
- minimum closure set needed for the requested acceptance level.

Recommend minimum closure by default, not full polish. Do not expand scope without user confirmation.

## Browser Budget Decision

Minimum real-browser acceptance is a normal frontend gate and should not trigger repeated user questions.

Ask before broad or exploratory AI E2E when it includes multi-route regression sweeps, many viewports, repeated visual-diff loops, authenticated or third-party flows, slow environments, or materially high time/token cost.

When asking for browser budget, provide target flows, viewports, evidence to collect, expected time/cost, stopping condition, and what remains for human review.
