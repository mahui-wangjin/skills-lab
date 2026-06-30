# design-to-frontend responsive foundation gate

## Status

Current.

## Problem

`design-to-frontend-delivery` already requires frontend foundation discovery, but fixed design canvases can still be translated into page-local breakpoints, fixed grid tracks, and one-off spacing values. That makes responsive behavior depend on individual pages instead of a reusable layout contract.

The rule must be method-level, not tied to any single viewport size. A named viewport, device, or pixel width can be an acceptance sample, but not the responsive method.

## Decision

Add a concise `responsive-foundation-gate.md` reference and wire it into the main skill, foundation gate, checklists, and smoke examples.

The gate treats a design frame as a baseline rather than a viewport contract. Before page styling, agents must record:

- CSS viewport/container model;
- canvas policy;
- shell and content ownership;
- layout primitives;
- tokenized spacing, width, density, and query policy;
- arbitrary CSS/Tailwind value policy;
- fixed-value exceptions;
- representative browser acceptance matrix.

Concrete viewport sizes are examples from the product context, not universal rules. The method starts from CSS viewport/container capability, ownership, reusable layout primitives, and acceptance classes. Arbitrary pixel utilities are allowed only as named exceptions or source-locked details; repeated layout values must be promoted to tokens, variants, layout primitives, or framework config.

## Non-goals

- Do not add a large responsive design textbook.
- Do not prescribe a specific framework or breakpoint scale.
- Do not encode project-specific cases as global skill rules.
- Do not ban fixed values outright; require owner, scope, and fallback.
- Do not ban Tailwind/CSS arbitrary values outright; require an arbitrary-value policy and promotion path when they repeat.

## Expected effect

Future fixed-canvas frontend work should create or reuse a responsive foundation before page-level styling. Later pages in the same archetype should reuse layout primitives or record a variant/exception instead of scattering private breakpoints and spacing scales.
