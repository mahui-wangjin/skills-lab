---
name: design-to-frontend-delivery
description: Use when delivering a frontend implementation from design artifacts or polishing an existing frontend project, especially when fidelity depends on choosing the right source of truth, using structured design/platform context before screenshots, preserving accepted shells, avoiding coordinate-copy layouts, verifying fonts/assets in the project instead of relying on the local machine, following framework/project structure, keeping mock/BFF responsibilities separate, and bringing static pages to presentation-ready quality across React, Vue, static HTML, mini-program, or similar targets.
---

# Design to Frontend Delivery

## Single Entry, Two Modes

One run must produce one target frontend result. Do not produce multiple target stacks in one run.

Route by [mode-routing.md](./references/mode-routing.md):

- Auto enter `convert-and-polish` when design artifacts are the main input (design + exported HTML, or design-tool generated code) and the task is to deliver a target frontend implementation.
- Treat design-platform URLs or connected plugins/MCPs that can expose structure, styles, tokens, component mappings, or reference code as design-tool context, not as image-only inputs.
- Auto enter `polish-existing-project` when an accepted existing frontend project is the main baseline and the task is to keep polishing interactions, validation, states, modals, animation, or acceptance quality.
- If both existing project and new design/HTML are present but intent is unclear, stop and ask which path is primary before implementation.

## Layout Fidelity Contract

Treat "1:1", "pixel-perfect", "same as design", or similar user wording as a fidelity goal, not permission to reproduce design-tool coordinates.

Professional frontend fidelity means preserving visual intent with maintainable implementation:

- Match layout relationships, spacing rhythm, alignment, typography, color, hierarchy, density, component states, and interaction behavior as closely as practical.
- Prefer semantic structure, reusable components, design tokens, CSS variables, Flexbox, CSS Grid, normal document flow, responsive constraints, and aspect-ratio.
- Translate design-tool auto-layout, constraints, grids, spacing, and variants into frontend layout primitives.
- Accept normal browser differences in font rendering, content length, breakpoints, and responsive wrapping when the visual relationship remains correct.

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
- Validate in the browser after fonts and assets load. High-fidelity or "pixel-perfect" cannot be claimed while key fonts/assets are missing, 404ing, falling back silently, or unverified.

## Project Structure Contract

Design delivery must follow the target framework and the existing project's directory conventions. Do not dump route entries, page orchestration, presentational components, fixtures, selectors, styles, assets, and tests into one arbitrary folder or one oversized file.

Before adding files:

- Inspect the current project's routing/page conventions, feature/module folders, shared component folders, mock/fixture locations, style/token system, asset handling, and test/story conventions.
- Reuse the nearest existing pattern when it fits. If the target stack is new or the repository has no clear convention, use the framework's official or widely accepted structure before inventing names.
- Separate responsibilities by change reason: route/page entry, feature orchestration, presentational components, mock/fixture data, display selectors/formatters, local UI state/hooks, styles/tokens/assets, and tests/stories.
- Keep feature-private files close to the feature; move only genuinely shared components, utilities, fixtures, or tokens into shared folders with stable contracts.
- For a one-file static HTML deliverable with no host project, self-contained output is acceptable, but keep data, rendering, styles, and interaction blocks internally separated and avoid turning it into the default for real projects.

Do not create generic dumping grounds such as `components`, `utils`, `helpers`, `mock`, or `data` at random levels when the project already has stronger feature, route, or domain boundaries. Folder names are framework-dependent; responsibility boundaries are mandatory.

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

## Mandatory Reference Loading Rules

Reference loading is required, not optional:

- When the input is a design-platform URL, connected plugin/MCP, design export, generated code, Dev Mode context, Code Connect/component mapping, or any artifact that may contain structure/style metadata, you must read [source-priority.md](./references/source-priority.md) before deciding whether the task is visual-only.
- When there are multiple fact sources, source conflicts, or visual-only inputs, you must read [source-priority.md](./references/source-priority.md) before implementation decisions.
- When the task involves high-fidelity visual match, typography, icons, images, media, design tokens, browser screenshots, or repeated "make it closer" polish, you must read [assets-and-visual-fidelity.md](./references/assets-and-visual-fidelity.md) before Gate 2 or any final fidelity claim.
- After mode is locked, you must read exactly one mode reference before implementation details:
  - `convert-and-polish` -> [convert-and-polish.md](./references/convert-and-polish.md)
  - `polish-existing-project` -> [polish-existing-project.md](./references/polish-existing-project.md)
- For all gate checks and final closeout output, you must read [delivery-checklists.md](./references/delivery-checklists.md) and follow its required artifacts.

## Three Gates

Canonical gate checks and closeout outputs are defined in [delivery-checklists.md](./references/delivery-checklists.md).

1. Gate 1 (pre-start confirmation)
- Lock mode, target stack, baseline artifacts, source-of-truth, scope, non-goals, and shell boundary.
- Record the project/framework structure convention that will own new route entries, feature files, components, fixtures, styles, assets, and tests.
- Record typography and asset facts: required font families/weights, image/icon/media sources, availability, license/provenance status when known, and fallback decision if any asset is missing.
- For design-platform inputs, record whether structured source was attempted and what result it returned before using screenshots/images as a baseline.

2. Gate 2 (mode-aware middle gate)
- `convert-and-polish`: structure mapping and shell-boundary pass before polish.
- `polish-existing-project`: current-state audit plus scope-gap closure decision before implementation continues.

3. Gate 3 (acceptance and closeout gate)
- Verify demo-ready polish quality, including actual browser-loaded fonts/assets, and produce final acceptance, risk, documentation update record, and next-step decision.

## Must Ask vs Can Decide

Must ask:

- Target stack is not specified and repository stack is not clear.
- Even for strong-vs-weaker conflicts like exported HTML vs design file/screenshot, if conflict touches structure, interaction path, or acceptance criteria, pause and ask which source is authoritative.
- Strong sources conflict on structure, primary flow, interaction path, or acceptance criteria.
- Existing project and new design/HTML are both present, but replacement/transplant/alignment intent is unclear.
- Only visual artifacts are provided (no exported HTML, no reference code, no accepted implementation).
- A platform appears capable of structured context or reference code, but the agent cannot access it after a real attempt; ask whether to wait for the stronger source or proceed with a visual-only downgrade.
- Shell preservation boundary is unclear (header/footer/layout/router).

Can decide without asking:

- A design-platform URL or plugin/MCP returns structured design context, Dev Mode-style metadata, component mappings, tokens, generated code, exported HTML/CSS, or reference code: use that as the structure/style source and use screenshots only for visual validation.
- Design plus exported HTML with clear target stack: go `convert-and-polish`.
- Explicit request to continue polishing current project: go `polish-existing-project`.
- HTML and design are both provided without conflict: HTML is structure source, design is visual validation source.
- Target stack is not stated but current project stack is explicit: keep the current stack.

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
- [delivery-checklists.md](./references/delivery-checklists.md)
