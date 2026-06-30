# design-to-frontend project delivery profile

## Status

Current.

## Problem

Design-to-code and Figma-to-code-style workflows are useful for extracting structure, copy, styles, and component hints, but generated output can smuggle in a parallel stack: one-off UI components, token scales, route shells, locale shapes, fixture schemas, API clients, and test conventions.

`design-to-frontend-delivery` already requires structured source, frontend foundation, responsive foundation, visible-element inventory, mock/BFF boundaries, and browser acceptance. It still needs an explicit bridge between "what the design/tool generated" and "how this host project builds frontend code".

## Decision

Add `project-delivery-profile.md` as a new reference and wire it into the main skill, foundation gate, convert/polish/continuation modes, delivery checklists, and skill UI prompt.

The gate requires two compact artifacts before implementation when a design platform, generated code, exported HTML/CSS, or codegen/tool output is involved:

- Project delivery profile: target stack/runtime, route and shell ownership, component system, token/theme source, styling policy, copy/i18n policy, asset/icon/font policy, data boundary, directory conventions, tests/stories, and browser acceptance path.
- Design intent map: source artifacts, semantic regions, source components/variants, repeated groups, interactions/states, content/data roles, and missing facts.

Generated code remains reference material. Project architecture must come from the host project and its accepted patterns.

## Non-goals

- Do not add or depend on a specific external Figma-to-code tool.
- Do not create a universal config file format for all projects.
- Do not promise one-shot production code from design artifacts.
- Do not duplicate all frontend foundation, responsive, fidelity, or mock/BFF rules in this spec.
- Do not block project-specific adapters when they are explicitly mapped and scoped.

## Expected effect

Future design-to-code work should start by reconciling source output with the host project's profile. Agents should keep useful structure and design facts from generated code while remapping imports, components, tokens, copy/i18n, fixtures, API boundaries, directories, tests, and browser acceptance to the project.

The skill should reject silent parallel systems: generated local Button/Card/Table/Form/Dialog/Toast families, unrelated UI libraries, local token scales, ad hoc locale keys, page-level fixture schemas, new API clients, or page-local route shells.
