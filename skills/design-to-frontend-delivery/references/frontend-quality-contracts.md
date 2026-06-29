# Frontend Quality Contracts

Use this reference for frontend delivery, development, polish, and regression work. It defines the quality floor that applies across design-to-code and ordinary UI changes.

## Layout Fidelity

Treat "1:1", "pixel-perfect", "same as design", and similar wording as high-fidelity visual intent, not literal pixel parity and not permission to copy design-tool coordinates.

Preserve layout relationships, spacing rhythm, alignment, typography, color, hierarchy, density, component states, and interaction behavior with maintainable implementation. Prefer semantic structure, reusable components, tokens, CSS variables, Flexbox, CSS Grid, normal flow, responsive constraints, and aspect-ratio.

Do not use `position: absolute`, `left/top`, fixed coordinates, or screenshot overlays for primary layout, repeated rows/cards, responsive columns, forms, dashboards, or ordinary content flow. Absolute/fixed positioning is acceptable for overlays, popovers, tooltips, badges, floating actions, intentional layering, canvas/game/diagram surfaces, and small anchored elements inside stable containers.

## Typography, Assets, And Details

Fonts, icons, images, video, gradients, shadows, and brand media are implementation assets, not local-environment assumptions.

Before repeated visual tweaks:

- confirm font family, weight/style, variable axes, size, line-height, letter spacing, color, and wrapping behavior;
- verify required fonts and media load through project assets, approved providers, or explicit fallback;
- stop if key fonts/assets are missing, 404ing, silently falling back, or unlicensed;
- do not tune spacing, colors, or coordinates to compensate for missing fonts/assets.

Do not fabricate assets or details when the design source, project assets, or accepted implementation provides them. Resolve icons, media, borders, padding, radius, shadow, states, transitions, and motion from tokens, component variants, Dev Mode/MCP data, exports, generated CSS, or accepted project components. If a required asset/detail cannot be found, ask, use an approved fallback, or mark the result conditional.

## Visible-Element Inventory

For Figma, design-platform, high-fidelity, or repeated polish work, build a compact visible-element inventory before coding or final polish. It is a source-to-implementation contract, not a coordinate checklist.

Cover non-trivial shell/frame/section/item/control/overlay/media/state surfaces, icons/assets, buttons/tabs/badges/progress/tables/lists/dividers/borders/forms/menus/toolbars, key text/numbers/status copy, and state details.

For each non-trivial item or repeated group, map:

- source: Figma node/component/asset/token, Dev Mode/MCP field, Code Connect mapping, generated CSS, exported asset, accepted component, or screenshot fallback;
- implementation: component/file, project token, asset path, icon import, fixture/state owner, or browser selector;
- status: exact reuse, project mapping, approved fallback, missing/blocked, or out of scope.

Gate 3 must reconcile the running browser against this inventory. Missing elements, wrong counts, inert controls, substituted assets, 404s, overflow, overlap, clipping, and wrong states are defects.

## UI Layer Ownership

Map every non-trivial visible part to an owner layer before coding or polish:

- app shell, page frame, content section, collection item, local control, overlay/feedback, decoration/media, and data/state.

Record owner, parent-child contract, state owner, placement rule, stacking/clipping rule, and reuse scope when the component is non-trivial.

Do not put page title, breadcrumbs, tabs, page actions, or filters inside repeated cards or arbitrary content panels. Do not put row/item state in the app shell. Do not create global modal/toast/drawer behavior inside feature cards when overlay roots exist. Do not fix wrong ownership with z-index escalation.

## Common Surface And Interaction

Classify the deliverable as `content-only`, `inside-existing-shell`, or `full-page-with-shell`. Reuse accepted shells, route frames, navigation, breadcrumbs, toolbars, modal/drawer/confirm/toast roots, route guards, and loading/empty/error patterns when the target is an existing project.

Every visible interactive element must have semantic controls or project accessible primitives, pointer affordance, hover/active/focus-visible, disabled/loading states, keyboard/touch basics, close/return paths, and feedback. Do not use inert `div`/`span` click targets when a native or proven component primitive fits.

## Browser Acceptance

Real-browser acceptance is the primary frontend quality gate. Unit tests, component tests, typecheck, lint, and smoke scripts are supporting evidence only.

Before final closeout, use the project's real-browser E2E, agent-browser, Playwright, Cypress, browser automation, browser-backed screenshots/traces, preview, or Storybook-in-browser workflow. If no harness exists, run the smallest meaningful real-browser acceptance path.

Treat smoke as a fast health gate: app starts, critical routes load, basic shell renders, and fatal console/network failures surface. Smoke is not final product acceptance for layout, overlays, responsive fit, asset loading, console/network cleanliness, or workflow usability.

AI browser work is evidence collection. Record commands, assertions, traces/screenshots, console/network logs, and interaction steps. Ask before high-cost exploratory E2E: broad cross-route coverage, many viewports, repeated visual diff/polish loops, large regression sweeps, authenticated or third-party flows, slow environments, or materially high time/token cost.

If real-browser verification or browser debugging cannot run, tell the user which console/network/runtime/layout/screenshot evidence is missing, what environment/tool/access is needed, and which risks remain. Mark the result self-reviewed/conditional or code-level candidate; do not call it demo-ready, accepted, fixed, or complete from smoke-only evidence.
