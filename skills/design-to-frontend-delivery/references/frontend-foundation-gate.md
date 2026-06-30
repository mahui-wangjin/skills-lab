# Frontend Foundation Gate

Use this reference before implementing or modifying real project pages, flows, or reusable UI surfaces. It applies to design-to-code, ordinary frontend development, bug fixes that touch UI structure, and polish on an existing project.

## Gate Rule

Do not code a page from an isolated screenshot or one-off local structure when the host project or framework already has frontend foundation primitives.

Before page-level implementation, record these five decisions:

1. Layout architecture: app shell, route layout, page wrapper, content slot, scroll container, sticky/fixed regions, toolbar, tabs, breadcrumbs, overlay roots, grid, spacing, and breakpoints.
2. Page archetype: list, detail, create/edit, dashboard/workbench, wizard, settings/configuration, approval/workflow, graph/canvas, monitoring/logs, report/analytics, search/selection, or a project-specific family.
3. Component mapping: design elements to project components, variants, headless primitives, tokens, or approved exceptions.
4. Token/theme system: color, typography, spacing, radius, shadow, density, motion, breakpoints, and component variants.
5. State/data boundary: state matrix, mock/API/BFF/domain split, route/menu/permission ownership, realistic data shape, and performance assumptions.

If a fixed design canvas, multi-page layout family, dashboard/workbench, shell/page-frame change, or responsive defect is involved, also read `responsive-foundation-gate.md` and record the responsive foundation contract before page styling.

If any likely existing foundation has not been checked, stop. Do not create page-local shells, grids, scroll roots, toolbars, breadcrumbs, overlay roots, table/list/form shells, component ecosystems, token scales, validation systems, permission/navigation logic, or breakpoint schemes until discovery is complete.

Adapters are allowed. Parallel Button/Card/Tabs/Table/List/Modal/Drawer/Form/Toast/Confirm/Tooltip or validation ecosystems are not.

The first page of a new archetype seeds a pattern. Similar later pages must reuse that seed or record a variant, new reusable primitive, or approved exception.

If no clear project foundation exists, choose the framework's official or widely accepted minimal pattern, record it, and keep it reusable.

## Component Mapping

Before creating a generic UI component, check the project and framework for:

- buttons, links, cards/panels, tabs, tables/lists, forms/fields, menus, filters, search, modal/drawer/popover/tooltip, toast/confirm, upload/picker controls, charts, canvas, and feedback states;
- component variants, size/density settings, disabled/loading/error/success states, and accessibility behavior;
- existing wrappers around third-party systems such as Ant Design, shadcn, Radix, MUI, Element Plus, Vben, React Admin, Headless UI, or internal business components.

If a project component fits, reuse it. If the design needs a variant, prefer a documented variant or feature-local adapter. Do not create a new common component family from one page unless the existing system is proven unsuitable.

## Token And Theme Mapping

Use the project token/theme source for:

- color, typography, spacing, radius, shadow, border, density, motion, z-index, and breakpoints;
- CSS variables, Tailwind/config utilities, framework theme objects, design tokens, or component variant props.

Do not invent page-local color scales, spacing scales, radius systems, shadow systems, breakpoint schemes, or density rules. Approved exceptions must be named and reusable.

## Table/List Pattern

Tables and lists must first map to the project pattern for:

- filters/search, filter collapse, toolbar/actions, refresh, column settings, density, fixed columns, pagination, sorting, batch actions, row actions, details entry, loading/empty/error, and narrow viewport behavior.

Do not implement a page-local table/list shell while a project pattern exists.

## Form/Validation Pattern

Forms must first map to the project pattern for:

- form state, field binding, schema or validation library, client validation, server/API error mapping, required/format messages, disabled/submitting states, success/failure feedback, reset/cancel, and return paths.

Do not create a page-local validation ecosystem unless the project has no suitable pattern.

## Route/Menu/Permission Ownership

Route-level facts belong to the project routing and authorization system when it exists:

- route metadata, page title, breadcrumbs, menu active state, return path, route guards, permission-driven actions, and hidden/disabled behavior.

Do not hardcode parallel navigation or permission logic inside the page.

## State/Data/Performance Matrix

Before implementation, list relevant states and realistic data pressure:

- loading, empty, error, permission denied, disabled, submitting, success, failure;
- long text, null/empty values, long lists, formatted numbers/dates/enums, and real content density;
- expected data volume, pagination, virtualization, lazy loading, expensive chart/canvas rendering, and mobile/narrow viewport strategy.

Mock data is a display fixture. Domain decisions, lifecycle transitions, permission decisions, eligibility rules, workflow routing, and cross-record decisions belong to BFF/domain layers unless real frontend ownership is explicitly in scope.
