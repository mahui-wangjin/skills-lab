# Project Delivery Profile

Use this reference when a design artifact, generated UI code, exported HTML/CSS, Dev Mode/MCP context, Code Connect mapping, or Figma-to-code-style tool output must become code inside a real project.

## Core Rule

Generated UI is a reference, not the project contract. The project contract comes from the host application's stack, route shell, components, tokens, data boundary, directory conventions, and browser acceptance path.

Before writing page code, translate the source into two small artifacts:

1. Project delivery profile: how this project expects frontend work to be built.
2. Design intent map: what the design means semantically before it becomes components.

Do not introduce a new stack, UI library, token scale, i18n system, fixture layout, API client, routing scheme, or test harness because a generated snippet contains one.

## Project Delivery Profile Contract

Record this compact contract before codegen, implementation, or broad polish:

```md
Project delivery profile:
- Target stack/runtime: <framework, rendering mode, package manager, language, styling system>
- Route and shell ownership: <app shell, route layout, page wrapper, content slot, breadcrumbs/title/nav owner>
- Page archetype: <list/detail/dashboard/workbench/wizard/form/settings/report/search or project-specific family>
- Component system: <project UI library, internal components, headless primitives, adapters, approved exceptions>
- Design-to-code mapping: <design component/node -> project component/props/variant/token/owner>
- Token/theme source: <CSS variables, Tailwind/config, design tokens, theme object, component variants>
- Styling policy: <utility/class composition, CSS modules, scoped styles, arbitrary-value policy, responsive policy>
- Copy/i18n policy: <literal copy allowed, locale key owner, existing translation system, fallback/blocked>
- Asset/icon/font policy: <project assets, icon system, exported SVG/media, font loading, licensing/source state>
- Data boundary: <static fixture, BFF-shaped mock, real API/BFF, client selectors, domain-owned decisions>
- Directory conventions: <routes/pages, feature modules, components, fixtures, selectors, styles, assets, tests/stories>
- Validation and test surface: <typecheck/lint/unit/component/story/browser/E2E commands or minimum path>
- Browser acceptance path: <viewports/containers, console/network, screenshots/traces, manual review gaps>
```

## Design Intent Map

Extract a source-backed design intent map before building components:

```md
Design intent map:
- Source artifacts: <node/selection/frame, Dev Mode/MCP, Code Connect, exported HTML/CSS, generated code, tokens>
- Semantic regions: <shell/page frame/content sections/repeated groups/local controls/overlays/decoration/data-state>
- Component candidates: <source component/variant/state -> project component candidate>
- Repeated collections: <group name, expected count, item anatomy, representative variants>
- Interaction and states: <default/hover/active/focus/selected/disabled/loading/error/success/empty>
- Content and data roles: <static copy, dynamic fields, formatted values, ids, enums, counts, dates>
- Missing facts: <unknown asset/token/component/copy/data contract + ask/fallback/blocked decision>
```

The map is not a coordinate checklist. It should make ownership, source, reuse, and missing facts explicit so implementation can stay semantic.

## Mapping Rules

- Prefer project components and variants over generated local components.
- Prefer Code Connect, design-system names, component docs, token names, and accepted project patterns over visual similarity.
- Treat generated JSX/HTML/CSS as a draft structure. Keep useful hierarchy and copy, but remap imports, props, tokens, class composition, state handling, assets, and tests to the project profile.
- Use an adapter or wrapper when a design component needs a project-specific variant. Do not create a parallel design-system family from one screen.
- Keep i18n changes inside the existing locale/key convention. Do not invent locale namespaces or keys without a project owner.
- Keep fixture data shaped like the expected BFF/API when known, but do not implement domain decisions in the frontend.
- Preserve source-backed detail facts: icon identity, typography, copy, borders, radii, shadows, motion, and interaction states. Missing facts must be asked, blocked, or marked as approved fallback.

## Red Flags

- Installing or trusting an external codegen skill/tool as the authority for project architecture.
- Copying generated imports, UI libraries, CSS reset, route shell, mock API, or localization shape into a project that already has equivalents.
- Creating page-local Button/Card/Table/Form/Dialog/Toast/Tooltip systems from generated code.
- Treating visual node names as domain model names without checking data/API contracts.
- Creating locale keys, fixture schemas, or API clients inside a page because the generated snippet needed data.
- Claiming production-ready or design-accepted from generated code without real-browser acceptance and project-profile reconciliation.

## Gate Checks

Before implementation:

- project delivery profile is recorded or an existing one is referenced;
- design intent map exists for non-trivial design/platform/codegen inputs;
- unmapped design elements have explicit status: project component, token, adapter, approved fallback, missing/blocked, or out of scope;
- generated code has been reconciled against project shell, components, tokens, data, directory, and test conventions.

At closeout:

- report which project-profile decisions were reused or introduced;
- report the design-to-code mapping result and remaining unmapped facts;
- verify in browser that profile conformance did not break visual intent, responsive fit, interaction, assets, or console/network health.
