# Design-to-Frontend Framework Foundation Gate

Status: current
Date: 2026-06-30
Owner: skills-lab

## Context

Design-to-frontend agents can produce visually plausible pages while missing the host framework or project frontend foundation. The common failure is starting from each design frame as a standalone page, then later discovering the project already had route layouts, page containers, scroll roots, toolbar/tabs/breadcrumb patterns, overlay roots, spacing/breakpoint primitives, component variants, table/list patterns, form/validation patterns, route/menu/permission ownership, or complete page archetypes.

That failure is costly because every page may grow a different local shell/container/grid/scroll strategy, component set, token scale, state matrix, or validation flow. Later reuse, regression testing, responsive fixes, API integration, and migration become harder even if individual screens looked acceptable at first.

## Decision

`design-to-frontend-delivery` now treats framework foundation discovery as a pre-implementation gate for real projects, multi-page delivery, frontend development, and frontend refinement.

Before page implementation, the agent must discover and record:

- Existing app shell, route layout, page wrapper, content slot, scroll container, sticky/fixed regions, page title/breadcrumbs/tabs, toolbar/action area, filter/search region, overlay roots, grid/spacing/breakpoints, and loading/empty/error surfaces.
- The page archetype or pattern family, such as list, detail, create/edit, dashboard/workbench, wizard, settings/configuration, approval/workflow, graph/canvas, monitoring/logs, report/analytics, search/selection, or a project-specific family already present in the host.
- The mapping from design surface to project layout primitive, page pattern, component family, token/theme system, table/list pattern, form/validation pattern, and route/menu/permission owner.
- The layout ownership decision for width, scroll, sticky behavior, density, spacing, breakpoints, and overlays.
- The state/data/performance matrix for loading, empty, error, permission denied, disabled, submitting, success, failure, long text, null values, long lists, formatted fields, expected data volume, pagination/virtualization/lazy loading, and chart/canvas cost.
- Whether the implementation is exact reuse, an existing-pattern variant, a new reusable primitive, an approved exception, or blocked because no suitable pattern exists.

If the project or framework likely has a layout system, page archetype, component family, token/theme system, route/menu/permission system, table/list pattern, form/validation pattern, or state/data boundary but it has not been checked, the agent must stop before coding pages. It must not create page-local shells, sidebars, topbars, containers, grid systems, spacing scales, scroll roots, toolbars, tabs, breadcrumbs, overlay roots, table/list/form shells, validation systems, permission/navigation logic, or token scales while existing primitives may fit.

The first page of a new archetype may become a pattern seed. From the second similar page onward, the agent must reuse the seed or record a variant/new reusable primitive/approved exception. Parallel page-local layouts are treated as a delivery defect.

## Scope

This gate applies to:

- Design-to-code conversion into an existing frontend project.
- Multi-page frontend delivery.
- New frontend page/flow development in an existing project.
- Polishing an existing project when the current implementation may have drifted from the project or framework foundation.
- Follow-up frontend work where a layout primitive, route frame, page container, component system, token/theme, route/menu/permission, table/list, form/validation, scroll root, or overlay root might be affected.

This gate does not require heavy process for:

- Throwaway single-file static HTML with no host project.
- Isolated prototypes where the user explicitly wants a disposable artifact.
- Tiny local visual fixes that cannot affect page layout ownership.

Even in those lighter cases, the result must not be described as aligned with a host layout system unless that system was actually checked.

## Implementation

The skill now updates:

- `SKILL.md`: keeps a compact entry point with mode routing, required reference loading, non-negotiable frontend gates, Gate 1/2/3 summaries, and final closeout rules.
- `references/frontend-foundation-gate.md`: holds the detailed framework foundation, page archetype, component mapping, token/theme, table/list, form/validation, route/menu/permission, state/data, and performance gate.
- `references/frontend-quality-contracts.md`: holds the cross-mode quality floor for layout fidelity, assets/details, visible inventory, UI ownership, common surfaces, interactions, and real-browser acceptance.
- `references/decision-and-scope-rules.md`: holds ask-vs-decide, scope-gap, and high-cost browser/E2E budget decisions.
- `references/convert-and-polish.md`: adds frontend foundation discovery to Gate 1, the minimum execution contract, a dedicated discovery section, Gate 2, and browser self-test.
- `references/polish-existing-project.md`: adds audits for foundation drift, page-local layout/component/token/state risk, migration cost, and final browser checks.
- `references/frontend-continuation.md`: protects accepted foundation decisions during API wiring, feature work, and bug fixes.
- `references/delivery-checklists.md`: adds foundation discovery, page archetype, component/token mapping, route/menu/permission, state/data/performance, pattern seed/reuse decision, no parallel page-local systems, and closeout reporting.
- `agents/openai.yaml` and `README.md`: surface the trigger and manual smoke scenario for future agents and users.

## Steelman Counter-Review

Objection: "This is too much process for small pages."

Response: The gate is scoped to real projects, multi-page delivery, or layout-affecting polish. Disposable single-file artifacts are explicitly lighter, but they cannot be mislabeled as host-layout aligned.

Objection: "This limits design freedom by forcing existing layouts."

Response: The rule does not force reuse blindly. It requires a reuse/variant/new primitive/exception decision before implementation. If the design genuinely needs a new layout, the output should be a reusable primitive or documented variant, not a page-local workaround.

Objection: "This binds the skill to one framework."

Response: The rule uses framework-neutral concepts: shell, route layout, page wrapper, content slot, scroll container, toolbar, tabs, breadcrumbs, overlay roots, grid, spacing, breakpoints, components, tokens, route metadata, permissions, state matrices, and page archetypes. Concrete names are discovered from the target project.

Objection: "What if the project has no layout system?"

Response: The agent should use the target framework's official or widely accepted minimal layout pattern, record it, and keep it reusable. Lack of a project convention is not permission to create untraceable per-page structures.

Objection: "What if the design source only shows content?"

Response: The existing common-surface and deliverable-surface rules still apply. Content-only can remain content-only, but inside-existing-shell or full-page delivery must map the content into the host layout contract.

## Validation Standard

Validation for this change requires:

- Skill validation with `quick_validate.py` for `skills/design-to-frontend-delivery`.
- Repository discovery with `npx skills add . --list --full-depth`.
- `git diff --check`.
- Keyword inspection for framework layout, page pattern/archetype, component mapping, token/theme, route/menu/permission, state/data/performance, pattern seed/reuse, and page-local system terms across the updated skill, references, README, and docs index.
- A steelman review before commit to ensure the rule remains generic, does not mention a specific project, and does not overburden throwaway prototypes.
