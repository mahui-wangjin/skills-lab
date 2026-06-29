---
name: design-to-frontend-delivery
description: Use when delivering frontend from design artifacts, polishing an existing frontend project, or continuing after design delivery with API/BFF wiring, functional changes, bug fixes, regression fixes, interactions, validation, states, modals, animation, or acceptance quality. Use when fidelity depends on Figma/Dev Mode/MCP/Code Connect source context, source-of-truth choice, structured design/platform context, accepted shell/common surfaces, exact icons/assets/tokens, UI layer ownership, framework/project structure, mock/BFF/API separation, clickable affordances, real-browser acceptance as the primary frontend quality gate, smoke-only limitations, maintainable smoke/E2E/browser automation, or presentation-ready React/Vue/static HTML/mini-program output.
---

# Design to Frontend Delivery

## Single Entry, Three Modes

One run must produce one target frontend result. Do not produce multiple target stacks in one run.

Route by [mode-routing.md](./references/mode-routing.md):

- Auto enter `convert-and-polish` when design artifacts are the main input (design + exported HTML, or design-tool generated code) and the task is to deliver a target frontend implementation.
- Treat design-platform URLs or connected plugins/MCPs that can expose structure, styles, tokens, component mappings, or reference code as design-tool context, not as image-only inputs. For Figma specifically, prefer Dev Mode / MCP design context for the specific node or selection; do not download or render the whole design file/canvas as a default first step.
- Auto enter `polish-existing-project` when an accepted existing frontend project is the main baseline and the task is to keep polishing visual fidelity, interactions, validation, states, modals, animation, or acceptance quality.
- Auto enter `frontend-continuation` when an accepted frontend implementation already exists and the task is follow-up API/BFF wiring, functional changes, bug fixes, regression fixes, or incremental feature work that must preserve unrelated pages and accepted design behavior.
- If both existing project and new design/HTML are present but intent is unclear, stop and ask which path is primary before implementation.

## Layout Fidelity Contract

Treat "1:1", "pixel-perfect", "same as design", or similar user wording as a request for high-fidelity visual reconstruction, not a literal pixel-parity promise and not permission to reproduce design-tool coordinates.

Professional frontend fidelity means preserving visual intent with maintainable implementation:

- Match layout relationships, spacing rhythm, alignment, typography, color, hierarchy, density, component states, and interaction behavior as closely as practical.
- Prefer semantic structure, reusable components, design tokens, CSS variables, Flexbox, CSS Grid, normal document flow, responsive constraints, and aspect-ratio.
- Translate design-tool auto-layout, constraints, grids, spacing, and variants into frontend layout primitives.
- Accept normal browser differences in font rendering, content length, breakpoints, and responsive wrapping when the visual relationship remains correct.
- Do not claim literal 100% pixel equality across responsive breakpoints, browsers, operating systems, font renderers, or dynamic content states.

Do not use `position: absolute`, `left/top`, fixed pixel coordinates, or screenshot-coordinate overlays to drive primary layout regions, repeated cards/rows, responsive columns, forms, dashboards, or ordinary content flow.

Absolute or fixed positioning is allowed for overlays, popovers, tooltips, badges, floating actions, intentional layered decoration, canvas/game/diagram surfaces, or small anchored elements inside a stable relative container.

If a normal page needs many absolute coordinates to look close to the design, stop before continuing and convert the implementation plan to Flex/Grid/flow layout. Record the exception if absolute positioning remains necessary.

## Typography and Asset Fidelity Contract

Treat fonts, icons, images, videos, gradients, shadows, and brand media as implementation assets, not as local-environment assumptions.

Before spending time on repeated visual tweaks:

- Extract the intended font family, weight/style, variable axes if relevant, size, line-height, letter spacing, color, and text wrapping behavior from the strongest available source.
- Verify the implementation can actually load the required font files or approved provider. Do not assume a font exists because it is installed on the agent's or user's machine.
- If a required font, weight, icon, image, or media asset is missing, pause the fidelity loop and either add a licensed project asset, use the project's approved provider/package, or disclose a fallback decision. Do not keep tuning spacing, colors, or coordinates to compensate for a font that is not loaded.
- Include only font files and media that the project has rights to use. When rights are unclear, ask for the asset or use an approved open/provider-backed alternative.
- Validate in the browser after fonts and assets load. High-fidelity visual reconstruction cannot be claimed while key fonts/assets are missing, 404ing, falling back silently, or unverified; literal pixel-perfect parity should not be claimed at all.

## Source-Locked Asset and Detail Contract

Do not fabricate visual assets or design details when the design source, project assets, or accepted implementation already provides them.

Before implementing or polishing visible UI details:

- Resolve every non-trivial icon, illustration, logo, bitmap, SVG, Lottie, decorative shape, gradient, shadow, radius, border, padding, gap, state color, hover/active/focus style, transition, and motion curve from the strongest available source: design tokens, component variants, Dev Mode/MCP inspect data, exported SVG/assets, generated CSS, accepted project components, or existing design-system variables.
- Reuse the project icon system, exported vector asset, Code Connect/component mapping, or existing component variant when available. Do not hand-draw or substitute a similar icon because it is faster.
- Treat hover, active, pressed, focus-visible, selected, disabled, loading, error, and success as state variants with design details, not as optional decoration.
- Keep border width, border color, padding, radius, shadow, outline, opacity, cursor, transition duration/easing, and hit-area density consistent with tokens or the accepted component pattern.
- If a referenced icon/detail asset cannot be found after checking the structured source and project assets, stop the fidelity loop and report the missing asset/detail decision. Ask for the asset, use an explicitly approved fallback, or mark the result conditional. Do not silently create a new icon or arbitrary radius/padding system.
- When the design source and project design system conflict on a detail that affects recognizable identity or interaction behavior, ask which source wins. Do not merge them into a new visual language.

Fabricated details are delivery defects. Examples include replacing a provided remote icon with a manually drawn SVG, using a generic icon from another library without approval, inventing hover colors, rounding sharp corners because it "looks modern", removing rounded corners because a component default is square, changing padding/radius/shadow to fit guessed taste, or using screenshots of icons instead of proper vector/component assets.

## Project Structure Contract

Design delivery must follow the target framework and the existing project's directory conventions. Do not dump route entries, page orchestration, presentational components, fixtures, selectors, styles, assets, and tests into one arbitrary folder or one oversized file.

Before adding files:

- Inspect the current project's routing/page conventions, feature/module folders, shared component folders, mock/fixture locations, style/token system, asset handling, and test/story conventions.
- Reuse the nearest existing pattern when it fits. If the target stack is new or the repository has no clear convention, use the framework's official or widely accepted structure before inventing names.
- Separate responsibilities by change reason: route/page entry, feature orchestration, presentational components, mock/fixture data, display selectors/formatters, local UI state/hooks, styles/tokens/assets, and tests/stories.
- Keep feature-private files close to the feature; move only genuinely shared components, utilities, fixtures, or tokens into shared folders with stable contracts.
- For a one-file static HTML deliverable with no host project, self-contained output is acceptable, but keep data, rendering, styles, and interaction blocks internally separated and avoid turning it into the default for real projects.

Do not create generic dumping grounds such as `components`, `utils`, `helpers`, `mock`, or `data` at random levels when the project already has stronger feature, route, or domain boundaries. Folder names are framework-dependent; responsibility boundaries are mandatory.

## UI Layer Ownership Contract

Before coding or polishing, map each visible UI part to one owning layer. Do not place a component by visual proximity alone.

Use these layer categories as a decision aid, adapting names to the target project:

- App shell layer: persistent layout, global navigation, sidebar, top bar, account area, global route frame, app-wide providers.
- Page frame layer: route-level title, breadcrumbs, page tabs, page toolbar, page-level filters, primary actions, page-level loading/error/empty.
- Content section layer: domain sections inside the page body, grouped panels, forms, charts, summary areas, detail areas.
- Collection item layer: repeated cards, table rows, list items, timeline entries, tree nodes, menu items.
- Local control layer: field groups, inline validation, disclosure state, local menus, local popovers, local action groups.
- Overlay and feedback layer: modal, drawer, confirm, toast, global popover, tooltip, notification, command palette, floating action.
- Decoration and media layer: background, illustration, non-interactive ornament, image/video/media frame, badge decoration, skeleton shimmer.
- Data/state layer: fixtures, display selectors, formatters, local UI state, BFF/API integration state, permissions, domain decisions.

For each non-trivial component, record or infer:

- Owner layer: which layer owns rendering, state, and lifecycle.
- Parent-child contract: what props/events/slots flow across the boundary.
- State owner: local component, page orchestration, shared shell, overlay provider, fixture, or real API/BFF.
- Placement rule: normal document flow, grid/flex slot, portal/root overlay, or stable anchored element.
- Stacking rule: whether it creates or depends on a stacking context, z-index token, portal root, sticky/fixed boundary, or clipping container.
- Reuse scope: feature-private, page-private, shell/shared, or design-system component.

Layer mistakes are delivery defects. Do not:

- Put page title, breadcrumbs, tabs, page actions, or filters inside repeated cards or arbitrary content panels.
- Put repeated item state, row actions, or item validation in the app shell or global provider.
- Implement global modal/toast/drawer behavior inside a feature card when the project already has overlay roots.
- Let decorative layers capture pointer events, create accidental scroll/stacking contexts, or cover interactive content.
- Use z-index escalation to hide a wrong ownership decision. Fix the layer, portal, clipping, or parent boundary first.
- Nest cards inside cards, page sections inside cards, or shell elements inside content sections unless the target design system explicitly does that.
- Mix data/domain decisions into presentational components just because the visual grouping is nearby.

## Common Surface Contract

Design delivery must account for the product surface around the designed content. If a design artifact only shows a content area, do not silently ignore host shell, navigation, or shared feedback surfaces.

Before implementation:

- Classify the deliverable as `content-only`, `inside-existing-shell`, or `full-page-with-shell`.
- Inspect the target project for existing layout shells and shared surfaces: app layout, header/top bar, sidebar/navigation, breadcrumbs, tabs, action toolbars, user/account area, notification entry, modal/drawer/confirm/toast roots, empty/error/loading patterns, and route guards.
- Reuse the accepted host shell and shared components when the target is an existing project. Do not rebuild parallel headers, sidebars, modal systems, toasts, drawers, or navigation frames because the design screenshot omitted them.
- If the design artifact conflicts with an accepted project shell, preserve the shell boundary and apply the design inside the allowed content area unless the user explicitly chooses replacement.
- If the intended surface cannot be inferred from repository code, project docs, or provided artifacts, ask one scope question before implementation. Do not ask when the repository already makes the shell contract clear.
- If a demo-ready result requires missing public surfaces, recommend the minimum closure set instead of pretending the page is complete.

## Interaction Affordance Contract

Frontend delivery must be usable, not only visible. Every interactive element should communicate that it can be used and should provide a complete local feedback loop for the scope of the deliverable.

For every button, link, menu item, tab, card action, row action, form control, disclosure, dialog, drawer, toast, tooltip, picker, uploader, and route entry:

- Prefer semantic native elements or the project's accessible component primitives. Do not use inert `div`/`span` click targets when `button`, `a`, `input`, `select`, or a proven headless/framework primitive fits.
- Provide appropriate cursor behavior for pointer devices: real click targets use pointer affordance; disabled or non-clickable surfaces must not pretend to be clickable.
- Cover visible states: default, hover, active/pressed, focus-visible, disabled, loading/submitting, selected/current, success, error, and empty where relevant.
- Preserve keyboard and assistive affordances: focus order, focus ring, Escape/close behavior for overlays, aria labels only where semantics do not already express the control, and return paths after closing or completing a flow.
- Keep touch ergonomics in scope for mobile and narrow viewports: controls must be reachable, not overlap, not rely on hover-only discovery, and maintain a usable hit area within the target design system's density.
- Modal, drawer, popover, confirm, and toast flows need open/close paths, overlay/close-button behavior, submit/cancel feedback, loading/failure states, and a non-blocked route back to the main task.
- Do not invent domain decisions to make interactions feel complete. For mock-stage work, keep completion to UI feedback and route/demo flow unless real API/BFF integration is explicitly in scope.

## End-to-End Self-Test Contract

Do not claim a frontend delivery is complete until it has been exercised in the running target surface through a real browser or real browser engine, not only inspected in code or checked by a smoke script.

Real-browser acceptance is the primary frontend quality gate. Unit tests, component tests, typecheck, lint, and smoke scripts are supporting evidence; they do not prove layout quality, overlay behavior, responsive fit, asset loading, console/network cleanliness, or user workflow usability by themselves.

Before final closeout:

- Use the project's existing real-browser E2E, agent-browser, Playwright, Cypress, browser automation, screenshot, preview, or Storybook-in-browser workflow when available. Prefer the project's proven browser-level path over inventing a new one.
- If no browser harness exists, run the app in a real browser or browser automation path appropriate to the stack and perform the smallest meaningful browser acceptance path.
- Treat smoke as a fast health gate: app starts, critical routes load, basic shell renders, and fatal console or network failures surface. Smoke is not final product acceptance for frontend UI quality.
- Use real-browser E2E, agent-browser, Playwright, Cypress, or the project's accepted browser automation path when checking layout, overlays, responsive behavior, interaction, screenshots, console errors, failed requests, fonts/assets, clipping, and workflow usability.
- If a smoke/E2E/browser script grows beyond a small route health check or mixes runner setup, fixtures, selectors, actions, assertions, screenshots, reporting, and cleanup, apply maintainability review and split the automation code before adding more scenarios.
- Cover the main happy path plus the surfaces touched by the change: shell/page frame, layer ownership, main content, repeated items, overlays/feedback, forms, route/back paths, loading/empty/error where in scope.
- Verify interactive affordances by doing the actions, not only checking markup: click/tap, keyboard focus where relevant, open/close overlays, submit/cancel, disabled/loading, route return, hover/focus-visible when practical.
- Check desktop and narrow/mobile viewport when the deliverable is responsive or user-facing across viewports.
- Check console errors, failed network/resource requests, missing fonts/assets, overflow/overlap, clipped overlays, blocked scroll, duplicate scrollbars, and z-index/portal issues.
- Keep the self-test scoped to the delivery. Do not expand a mock-stage task into real API/BFF integration just to make E2E pass.
- If real-browser verification or browser debugging cannot run, explicitly remind the user before final acceptance which console/network/runtime/layout/screenshot evidence is missing, what environment/tool/access is needed, and which user-visible risks remain. Mark the result as self-reviewed/conditional or code-level candidate only. Do not call it demo-ready, accepted, fixed, or complete from smoke-only evidence.

## Mock/BFF Boundary Contract

Static, prototype, visual-polish, and mock-data delivery is not API integration unless the user explicitly asks for real API wiring.

In mock-stage frontend work:

- Mock data is a presentation fixture. It may be shaped like a future BFF response to keep JSX clean and replaceable.
- Frontend may keep only lightweight UI state: selected tab, selected item, expanded section, modal open/closed, local form draft, loading/error/empty demo surfaces.
- Frontend may implement presentation-grade client validation and formatting when it is basic UI feedback, not domain eligibility, authorization, or workflow decision-making.
- Frontend may use thin display selectors: grouping already-provided records, counting visible lists, validating tab keys, selecting a fixture by id, and mapping fixture fields into components.
- BFF/domain-owned decisions must stay out of frontend mock logic: derived business metrics, lifecycle/status transitions, eligibility or authorization decisions, allowed-action decisions, integration-status normalization, domain labels derived from business codes, destination or next-action resolution, and cross-record workflow decisions.
- Do not create fake API state machines, polling, caching, optimistic updates, retry policies, permission engines, or domain reducers just to support a static mock page.
- If the future BFF contract is unknown, keep fixtures explicit and local. Name the seam as replaceable data, not as a guessed API contract.

When real API integration is requested, switch scope explicitly: identify the contract source, loading/error/empty behavior, mutation side effects, cache policy, authorization assumptions, and verification path. Do not smuggle those decisions into a mock-only design delivery.

## Continuation Development and Regression Contract

This skill also governs follow-up frontend work after the first design delivery. API wiring, functional changes, bug fixes, and later refinements must preserve accepted design structure, visual details, interaction behavior, and unrelated pages.

Before changing an accepted frontend implementation:

- Identify the accepted baseline: commit, route, design artifact, screenshot evidence, story, test, or user-approved current behavior.
- Classify the work as visual refinement, API/BFF integration, functional change, bug fix, regression fix, or mixed scope.
- Map the impact surface: routes/pages, shared shell, page frame, shared components, design tokens/assets, state stores, hooks, API clients, fixtures, tests/stories, and browser flows that may be affected.
- Reuse existing API clients, query/cache patterns, form primitives, validation rules, error boundaries, loading/empty/error components, permission gates, and mutation feedback patterns before introducing new ones.
- Keep API/BFF contracts separate from visual components. Components receive display-ready props or thin view models; they do not invent domain status transitions, authorization decisions, retry policies, or cross-page workflow rules.
- Protect unrelated pages. If a shared component, token, API client, hook, selector, or fixture changes, run or add focused regression checks for the other known consumers.
- Preserve design facts. A bug fix or API connection is not permission to replace icons, change radii, remove hover/focus states, collapse layers, or redesign shell/content boundaries unless that is explicitly in scope.
- If browser debugging cannot run for a bug, visual defect, interaction defect, or regression, remind the user that browser evidence is missing and downgrade the result to conditional/code-level candidate.
- Close with a regression note: what changed, what was intentionally untouched, which affected surfaces were tested, and which risks remain.

## Mandatory Reference Loading Rules

Reference loading is required, not optional:

- When the input is a design-platform URL, connected plugin/MCP, design export, generated code, Dev Mode context, Code Connect/component mapping, or any artifact that may contain structure/style metadata, you must read [source-priority.md](./references/source-priority.md) before deciding whether the task is visual-only. For Figma URLs, parse or use the file/node context and attempt node-level Dev Mode/MCP structured data first; whole-file screenshots or full-canvas downloads are not a valid first source attempt.
- When there are multiple fact sources, source conflicts, or visual-only inputs, you must read [source-priority.md](./references/source-priority.md) before implementation decisions.
- When the task involves high-fidelity visual match, typography, icons, images, media, design tokens, browser screenshots, or repeated "make it closer" polish, you must read [assets-and-visual-fidelity.md](./references/assets-and-visual-fidelity.md) before Gate 2 or any final fidelity claim.
- After mode is locked, you must read exactly one mode reference before implementation details:
  - `convert-and-polish` -> [convert-and-polish.md](./references/convert-and-polish.md)
  - `polish-existing-project` -> [polish-existing-project.md](./references/polish-existing-project.md)
  - `frontend-continuation` -> [frontend-continuation.md](./references/frontend-continuation.md)
- For all gate checks and final closeout output, you must read [delivery-checklists.md](./references/delivery-checklists.md) and follow its required artifacts.

## Three Gates

Canonical gate checks and closeout outputs are defined in [delivery-checklists.md](./references/delivery-checklists.md).

1. Gate 1 (pre-start confirmation)
- Lock mode, target stack, baseline artifacts, source-of-truth, scope, non-goals, and shell boundary.
- Record the UI layer ownership map for shell, page frame, content sections, repeated items, local controls, overlays/feedback, decoration/media, and data/state ownership.
- Record the deliverable surface contract: `content-only`, `inside-existing-shell`, or `full-page-with-shell`.
- Record common surface decisions: existing shell/navigation/toolbar/modal/drawer/toast/confirm roots to reuse, public surfaces that are out of scope, and missing surfaces that affect demo readiness.
- Record the minimum execution contract: what will be built, what will be reused, primary interactions/states, minimum closure level, non-goals, and the single blocking question if one remains.
- Record the project/framework structure convention that will own new route entries, feature files, components, fixtures, styles, assets, and tests.
- Record typography, asset, and detail facts: required font families/weights, exact icon/image/media sources, design tokens, border/padding/radius/shadow/motion/state details, availability, license/provenance status when known, and fallback decision if any asset/detail is missing.
- For design-platform inputs, record whether structured source was attempted and what result it returned before using screenshots/images as a baseline.

2. Gate 2 (mode-aware middle gate)
- `convert-and-polish`: structure mapping, UI layer ownership pass, common-surface pass, shell-boundary pass, and interaction-affordance pass before polish.
- `polish-existing-project`: current-state audit, UI layer ownership audit, common-surface audit, interaction-affordance audit, plus scope-gap closure decision before implementation continues.
- `frontend-continuation`: accepted baseline, impact surface, API/feature/bugfix contract, affected consumers, regression plan, and non-regression boundary before implementation continues.

3. Gate 3 (acceptance and closeout gate)
- Verify demo-ready polish quality or continuation-change safety with E2E/self-test evidence, including actual browser-loaded fonts/assets, exact icons/details, layer ownership, public surfaces, usable interactive affordances, and affected-regression coverage. Produce final acceptance, risk, documentation update record, and next-step decision.

## Must Ask vs Can Decide

Must ask:

- Target stack is not specified and repository stack is not clear.
- Even for strong-vs-weaker conflicts like exported HTML vs design file/screenshot, if conflict touches structure, interaction path, or acceptance criteria, pause and ask which source is authoritative.
- Strong sources conflict on structure, primary flow, interaction path, or acceptance criteria.
- Existing project and new design/HTML are both present, but replacement/transplant/alignment intent is unclear.
- Only visual artifacts are provided (no exported HTML, no reference code, no accepted implementation).
- A platform appears capable of structured context or reference code, but the agent cannot access it after a real attempt; ask whether to wait for the stronger source or proceed with a visual-only downgrade.
- Shell preservation boundary is unclear (header/footer/layout/router).
- Deliverable surface is unclear and cannot be inferred from repository conventions or provided artifacts: `content-only`, `inside-existing-shell`, or `full-page-with-shell`.
- A required icon, illustration, token, radius/padding/shadow/motion detail, or state variant appears in the source but cannot be located in the project/assets after a real attempt.
- API/BFF integration scope is requested but the contract source, mutation side effects, cache policy, authorization expectation, or regression surface cannot be inferred from project code/docs.

Can decide without asking:

- A design-platform URL or plugin/MCP returns structured design context, Dev Mode-style metadata, component mappings, tokens, generated code, exported HTML/CSS, or reference code: use that as the structure/style source and use screenshots only for visual validation. For Figma, use the target node/selection context before screenshots; avoid whole-canvas image fetches unless the user explicitly asks for an overview image or structured access is unavailable after a real attempt.
- Design plus exported HTML with clear target stack: go `convert-and-polish`.
- Explicit request to continue polishing current project: go `polish-existing-project`.
- Explicit request to wire API/BFF, modify behavior, fix bugs, or protect unrelated pages in an accepted frontend implementation: go `frontend-continuation`.
- HTML and design are both provided without conflict: HTML is structure source, design is visual validation source.
- Target stack is not stated but current project stack is explicit: keep the current stack.
- Existing project has an accepted shell, route frame, shared modal/toast/drawer roots, or navigation pattern and the user did not ask to replace it: reuse the existing common surfaces and implement inside that boundary.
- A matching icon/detail/token exists in the design export, project asset system, or accepted design-system component: reuse it and do not ask to substitute.

## Question Style Constraints

- Ask only one critical question at a time.
- Ask only questions that can change execution routing, scope, or acceptance decisions.
- Do not ask questions that can already be decided from repository code, project docs, or provided artifacts.

## Scope Gap Detection and Minimum-Closure Expansion

In `polish-existing-project`, run scope-gap detection after current-state audit:

- If named scope is not enough for a demo-ready result, report:
  - named scope
  - uncovered layers
  - expected completion level if only named scope is done
  - recommended minimum-closure expansion set
- Recommend minimum closure by default, not full polish by default.
- Do not expand scope without user confirmation.

## References

- [source-priority.md](./references/source-priority.md)
- [assets-and-visual-fidelity.md](./references/assets-and-visual-fidelity.md)
- [mode-routing.md](./references/mode-routing.md)
- [convert-and-polish.md](./references/convert-and-polish.md)
- [polish-existing-project.md](./references/polish-existing-project.md)
- [frontend-continuation.md](./references/frontend-continuation.md)
- [delivery-checklists.md](./references/delivery-checklists.md)
