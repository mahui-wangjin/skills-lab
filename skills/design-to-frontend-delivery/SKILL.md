---
name: design-to-frontend-delivery
description: Use for frontend delivery, development, polish, or modification from designs, accepted UI, or requirements. Triggers include Figma/Dev Mode/MCP/Code Connect, source-of-truth, project delivery profiles, design intent maps, framework foundation/page archetype, component/token mapping, UI layers, assets, visible inventories, mock/BFF/API boundaries, API/feature/bugfix continuation, real-browser acceptance, E2E/smoke automation, or frontend output.
---

# Design to Frontend Delivery

## Purpose

Use this as a frontend delivery standard, not only as a design-to-code helper. It applies to design artifacts, requirement-driven frontend pages/flows, accepted UI polish, API/BFF wiring, feature changes, bug fixes, and regression fixes after a UI baseline exists.

One run must produce one target frontend result. Do not produce multiple target stacks in one run.

## Route First

Read [mode-routing.md](./references/mode-routing.md), then choose one mode:

- `convert-and-polish`: design artifacts, exported HTML, generated code, or structured design-platform context are the main input.
- `polish-existing-project`: an accepted existing frontend project is the baseline for visual, interaction, state, or polish quality.
- `frontend-continuation`: an accepted implementation exists and the task is API/BFF wiring, feature work, bugfix, regression fix, or incremental frontend development.

If an existing project and a new design/HTML are both present but the replacement, transplant, or alignment intent is unclear, stop and ask which path is primary.

For Figma or other design platforms, prefer target node/selection/frame Dev Mode, MCP design context, Code Connect, variables/tokens, or generated reference code before screenshots. Do not download or render the whole file/page/canvas as the default first step.

## Required Reference Loading

Load references only when their condition applies, but do not skip required ones:

- Read [frontend-foundation-gate.md](./references/frontend-foundation-gate.md) before implementing or modifying real project pages, flows, route frames, reusable UI, table/list/form surfaces, route/menu/permission behavior, or token/theme usage.
- Read [responsive-foundation-gate.md](./references/responsive-foundation-gate.md) before implementing from a fixed design canvas, building multi-page/dashboard/workbench UI, changing shell/page-frame layout, or fixing viewport/container/overflow/breakpoint/zoom responsive issues.
- Read [frontend-quality-contracts.md](./references/frontend-quality-contracts.md) before visual polish, interaction work, browser acceptance, or final frontend closeout.
- Read [source-priority.md](./references/source-priority.md) for design-platform URLs, plugin/MCP input, design exports, generated code, Dev Mode context, Code Connect mapping, or conflicting sources.
- Read [project-delivery-profile.md](./references/project-delivery-profile.md) when design-platform context, generated code, exported HTML, or codegen/tool output must become code inside a real project, or when target stack, component mapping, token source, i18n, assets, mock/API ownership, directory conventions, or tests are unclear.
- Read [assets-and-visual-fidelity.md](./references/assets-and-visual-fidelity.md) before high-fidelity visual match, typography, icons, images, media, design tokens, screenshots, or repeated "make it closer" polish.
- After routing, read exactly one mode reference: [convert-and-polish.md](./references/convert-and-polish.md), [polish-existing-project.md](./references/polish-existing-project.md), or [frontend-continuation.md](./references/frontend-continuation.md).
- Read [decision-and-scope-rules.md](./references/decision-and-scope-rules.md) when routing, source precedence, foundation ownership, shell preservation, API scope, browser budget, or scope gaps are unclear.
- Read [delivery-checklists.md](./references/delivery-checklists.md) for Gate 1/2/3 fields and final closeout.

## Non-Negotiable Gates

### Frontend Foundation Before Code

Before coding pages, flows, or reusable UI in a real project, lock the framework/project foundation: layout architecture, page archetype, component mapping, token/theme system, state/data boundary, route/menu/permission ownership, table/list pattern, form/validation pattern, scroll/responsive strategy, long-data cases, data volume, and performance assumptions.

If a likely foundation exists but has not been checked, stop. Do not create page-local shells, grids, scroll roots, toolbars, breadcrumbs, overlay roots, table/list/form shells, component ecosystems, token scales, validation systems, permission/navigation logic, or breakpoint schemes.

### Project Delivery Profile Before Codegen

Design-platform output, generated React/Vue/HTML, and Figma-to-code-style tool output are reference material, not final project code. Before turning them into implementation, lock the project delivery profile: target stack/runtime, route and shell ownership, component and token mappings, styling conventions, i18n/copy policy, asset/icon/font policy, mock/API boundary, directory/test conventions, and browser acceptance path.

Also extract a design intent map before coding: semantic regions, UI layer owners, component variants, repeated collections, interaction/state variants, content/data roles, and missing source facts. Do not create a parallel stack, component family, token scale, locale system, fixture layout, or API client because generated code happened to contain one.

### Responsive Foundation Before Page Styling

A fixed design frame is a baseline, not the viewport contract. Before translating fixed-frame geometry into page classes, lock the responsive foundation: CSS viewport model, canvas policy, shell/content ownership, reusable layout primitives, tokenized spacing/width/density rules, container-query vs viewport-breakpoint policy, fixed-value exceptions, and browser acceptance matrix.

Do not treat a named viewport, device, or pixel width as the method. Do not scatter arbitrary page-local breakpoints, fixed grid tracks, fixed-height patches, arbitrary pixel utilities, one-off spacing scales, or whole-page proportional scaling to make individual screens fit. If proportional scaling is intentionally used, record it as an explicit exception with its scope, accessibility trade-off, and browser evidence.

### Source-Backed Fidelity

Treat "1:1", "pixel-perfect", and "same as design" as high-fidelity visual intent, not literal pixel parity and not permission to copy coordinates.

Use semantic structure, project components, tokens, CSS variables, Flexbox/Grid, normal flow, and responsive constraints. Do not use absolute/fixed coordinates or screenshot overlays for ordinary layout, repeated rows/cards, forms, dashboards, or responsive content.

Fonts, icons, images, media, borders, radii, shadows, states, motion, and other recognizable details must come from structured design context, tokens, component variants, exports, generated CSS, project assets, or accepted components. Missing assets/details require an ask, approved fallback, or conditional result.

### Ownership And Interaction

Map non-trivial visible UI to owning layers: app shell, page frame, content section, collection item, local control, overlay/feedback, decoration/media, and data/state.

Reuse accepted shells, route frames, navigation, breadcrumbs, toolbars, modal/drawer/confirm/toast roots, route guards, loading/empty/error patterns, components, tokens, and interaction primitives. Do not fix wrong ownership with z-index escalation or create parallel component/overlay ecosystems.

Every visible interactive element must use semantic controls or project accessible primitives, pointer affordance, hover/active/focus-visible, disabled/loading states, keyboard/touch basics, close/return paths, and feedback.

### Mock/API Boundary

Mock data is a display fixture. Frontend may own lightweight UI state, thin display selectors, and presentation-grade validation.

Domain decisions, lifecycle transitions, permission decisions, eligibility rules, workflow routing, retry policy, polling, optimistic updates, and cross-record decisions belong to BFF/domain layers unless real frontend ownership is explicitly in scope.

### Real-Browser Acceptance

Real-browser acceptance is the primary frontend quality gate. Unit tests, component tests, typecheck, lint, and smoke scripts are supporting evidence only.

Smoke is only a health gate: app starts, critical routes load, basic shell renders, and fatal console/network failures surface. It is not final product acceptance for layout, overlays, responsive fit, asset loading, console/network cleanliness, or workflow usability.

Ask before high-cost exploratory E2E. If real-browser verification or browser debugging cannot run, tell the user what console/network/runtime/layout/screenshot evidence is missing, what environment/tool/access is needed, and which risks remain. Mark the result self-reviewed, conditional, or code-level candidate.

## Three Gates

Use [delivery-checklists.md](./references/delivery-checklists.md) as the canonical field list.

- Gate 1: lock mode, target stack, baseline, source of truth, project delivery profile, design intent map, frontend foundation, visible inventory, surface boundary, scope, non-goals, and browser acceptance path.
- Gate 2: settle the mode-specific middle gate before polish or broad implementation. Foundation, project profile, design-to-code mapping, component/token mapping, UI ownership, common surfaces, state/data boundary, interaction affordance, visible-element mapping, and regression surface must be clear.
- Gate 3: verify in a real browser or browser engine. Include fonts/assets, visible inventory reconciliation, layout/page-pattern fit, project profile conformance, component/token reuse, state/data resilience, UI ownership, interactions, public surfaces, and affected regressions.

## Closeout Standard

Final frontend closeout must state the mode, project delivery profile, design intent mapping, foundation/page-pattern decision, source status, component/token reuse, visible inventory reconciliation, browser evidence, smoke/unit/component evidence if used, unresolved missing assets/details, browser-debugging gaps, and remaining risks. Do not call the result accepted, demo-ready, fixed, or complete from smoke-only evidence.
