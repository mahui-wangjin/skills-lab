# Responsive Foundation Gate

Use this reference when a frontend task involves a fixed design canvas, desktop/tablet/mobile variants, multi-page UI, dashboard/workbench layout, shell/page-frame changes, or any responsive bug involving viewport, container width/height, zoom, density, wrapping, overflow, or breakpoints.

## Core Rule

A design frame is a baseline, not the viewport contract. The method starts from CSS viewport/container capability, ownership, and layout primitives; named device or pixel sizes are only representative acceptance samples.

Before page-level styling, translate the design into a reusable responsive foundation. Do not scatter page-local arbitrary breakpoints, fixed grid tracks, or one-off spacing values to make individual screens fit.

## Responsive Foundation Contract

Record this compact contract before coding or broad polish:

```md
Responsive foundation:
- Design baseline: <frame roles and what each one proves; frame sizes are samples only>
- Viewport model: <CSS viewport classes, not physical monitor resolution>
- Canvas policy: <centered max canvas / fluid container / constrained stretch / explicit scale exception>
- Shell ownership: <nav/topbar/rail/content slot/overlay/scroll owner>
- Container ownership: <which wrapper owns width, gap, padding, scroll, sticky, clipping>
- Layout primitives: <page frame / stack / cluster / grid / two-column / aside / panel group>
- Token strategy: <CSS variables/theme utilities for spacing, gaps, widths, density, z-index>
- Query policy: <container queries first for component fit; viewport breakpoints for shell/archetype shifts>
- Arbitrary value policy: <which CSS/Tailwind arbitrary values are source-locked exceptions vs promoted to tokens/primitives>
- Fixed-value exceptions: <allowed anchors, media frames, charts/canvas, or source-locked geometry>
- Acceptance matrix: <representative viewport/container classes + overflow/overlap/wrapping/overlay checks; concrete sizes are samples only>
```

The acceptance matrix should use representative viewport/container classes from the product context. Concrete sizes may appear as test cases, but they must not become the rule.

## Decision Rules

- Use container queries when a component's fit depends on its parent after sidebars, padding, or panels take space.
- Use viewport breakpoints for shell, navigation, page archetype, and major layout shifts.
- Define rules by capability ranges and ownership first, then choose sample viewport sizes for browser evidence.
- Use fluid tokens such as `clamp()` or theme variables for spacing and gaps when the same layout should breathe across sizes.
- Treat Tailwind/CSS arbitrary values such as `min-h-[...]`, `grid-cols-[...]`, `gap-[...]`, and `@min-[...]` as implementation exceptions. If a value appears in a layout family, promote it to a token, named component variant, layout primitive, or framework config.
- Avoid fixed heights as the primary responsive fit mechanism. Prefer normal flow, `minmax()`, `fr`, `auto`, `min-h-0`, `aspect-ratio`, clear scroll ownership, and container-managed density before per-element height patches.
- Keep text, hit targets, and accessibility intent readable. Proportional whole-page scaling is an explicit exception, not the default responsive model.
- Keep fixed pixel geometry only when it represents stable source-locked media, chart, canvas, icon, avatar, or anchored detail; name the owner and fallback.
- The first page of an archetype may seed responsive primitives. Later pages must reuse the primitive or record a variant/exception.

## Red Flags

- Treating physical screen resolution as the responsive basis instead of CSS viewport/container size.
- Copying a fixed design frame into page-local `min-*` classes on every page.
- Chaining many arbitrary pixel utilities to make one viewport look right without naming the layout primitive they belong to.
- Using whole-page `zoom`/`transform: scale()` to hide missing layout rules.
- Letting one page define a private spacing, density, grid, or breakpoint scale.
- Verifying only the design baseline viewport while claiming responsive fit.

## Gate 3 Checks

In a browser or browser engine, check representative viewport classes for:

- no horizontal page overflow unless intentionally scoped;
- no overlapping text, controls, sticky/fixed regions, or overlays;
- expected wrapping, truncation, scrolling, and panel collapse behavior;
- shell, content slot, and overlay roots still owned by the intended layer;
- fonts/assets loaded before judging layout density.
