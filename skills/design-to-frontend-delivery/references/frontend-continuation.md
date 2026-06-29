# Frontend Continuation

Use this mode after a frontend implementation has been accepted and the task is API/BFF wiring, a functional change, a bug fix, a regression fix, or incremental feature work. The default responsibility is to preserve the accepted design and prevent unrelated regressions.

## 1. Continuation Gate

Before implementation, record:

```md
Continuation contract:
- Accepted baseline: <commit / route / design artifact / screenshot / story / user-approved behavior>
- Change type: <API/BFF integration | functional change | bug fix | regression fix | mixed>
- Scope: <pages/components/flows to change>
- Non-goals: <visual redesign / shell replacement / unrelated pages / domain policy changes>
- API or behavior contract source: <OpenAPI/schema/docs/code/current BFF/mock/user decision>
- Impact surface: <routes, shared components, hooks, store/cache, API clients, tokens/assets, tests/stories>
- Regression surface: <known consumers and flows that must not change>
- Self-test path: <real-browser acceptance path; smoke/unit/component checks only as supporting evidence>
- Blocking question: <none or one question that changes scope/acceptance>
```

Do not proceed if the accepted baseline is unclear. Ask whether the current implementation is the baseline to preserve or whether the user expects replacement from a newer design.

## 2. API/BFF Integration Rules

When real data integration is in scope:

1. Identify the contract source before coding: schema, OpenAPI, existing client, BFF route, typed SDK, mock contract, or explicit user-provided shape.
2. Reuse the project's existing data-fetching stack, cache/query pattern, API client, error handling, auth/permission pattern, and loading/empty/error components.
3. Keep domain decisions at the BFF/domain layer. Frontend may format display-ready fields, select visible records, and manage local UI state; it should not invent lifecycle transitions, permission decisions, eligibility rules, retry policies, or cross-record workflow decisions.
4. Model user-visible states: initial loading, empty, success, error, retry/reload, submitting, success feedback, failure feedback, disabled while pending, and stale/refetch state when the project already uses it.
5. Mutations need explicit side effects: what cache invalidates, what route changes, what toast/confirm appears, what optimistic update is allowed, and what rollback/error path exists.
6. If the real contract conflicts with the mock/design shape, do not silently reshape business meaning in the component. Add a mapper/view-model boundary or ask for the intended behavior.

## 3. Functional Change and Bugfix Rules

For feature changes and fixes:

1. Reproduce or locate the current behavior first when possible: route, story, test, screenshot, or browser path.
2. Make the smallest change that satisfies the contract. Do not use a bugfix as permission to restructure unrelated layout, replace icons, change visual tokens, or redesign flows.
3. Preserve accepted detail facts: icon identity, copy, component hierarchy, page frame, shell boundary, border/padding/radius/shadow, hover/focus/disabled/loading states, and responsive behavior unless explicitly in scope.
4. If the fix touches shared components, shared tokens, hooks, selectors, API clients, store/cache, route guards, overlay roots, or form primitives, identify every known consumer and run a focused regression check.
5. If a shared change is risky, prefer a feature-local adapter, prop, variant, or wrapper over changing global behavior.
6. Do not create parallel duplicate implementations for the same API, formatter, component, modal, toast, or validation pattern unless the existing pattern is proven unsuitable.

## 4. Non-Regression Checklist

Before closeout:

- The changed route/page still preserves accepted shell, page frame, UI layer ownership, public surfaces, icons/assets, state variants, and design token details.
- Other known consumers of changed shared code still render or test correctly.
- API/BFF states cover loading, empty, error, success, submitting, disabled, and failure feedback when relevant.
- Overlay/feedback flows still open, close, submit/cancel, recover from failure, and return to the main task.
- Console errors, failed requests, missing assets/fonts/icons, overflow, clipping, duplicate scrollbars, and z-index regressions have been checked in the touched flow through a real browser or browser engine.
- If full E2E is too heavy, run the smallest meaningful focused real-browser path plus targeted unit/component tests for changed logic. Smoke-only evidence is conditional and cannot prove frontend UI quality.
- If browser debugging cannot run, remind the user before closeout that console/network/runtime/layout/screenshot evidence is missing, name the blocked tool or access path, and downgrade the result to conditional/code-level candidate.

## 5. Closeout Requirement

Final output for this mode must include:

- baseline preserved;
- exact change delivered;
- API/behavior contract source;
- affected surfaces and protected unrelated surfaces;
- regression checks run;
- untested or conditional risk.

If regression checks or browser debugging cannot run, mark the result conditional/self-reviewed, remind the user what evidence is missing and what is needed to obtain it, and provide a manual route-by-route checklist. Do not claim the change is safe for unrelated pages without evidence.
