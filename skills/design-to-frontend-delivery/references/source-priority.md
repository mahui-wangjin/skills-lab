# Source Priority

This reference defines baseline evidence ranking for `design-to-frontend-delivery`.
It is a foundational rule layer used by the main skill workflow, not a standalone entry.

## Core Principle

Prefer structured source over raster source.

If any design or prototyping platform can provide structure, style properties, tokens, component mappings, generated code, exported HTML/CSS, Dev Mode-like inspection data, MCP context, or reference implementation snippets, that source must be attempted before screenshots, downloaded images, or visual guessing are used as the baseline.

This is platform-agnostic. Examples include Figma Dev Mode / MCP `get_design_context` / Code Connect, Stitch or design-tool exported HTML, Framer/Webflow/static exports, design-token JSON, component mapping files, generated React/Vue/HTML snippets, or accepted host-project implementation. The specific platform can change; the rule is about source strength.

Screenshots, downloaded renders, and exported images are visual validation or asset evidence. They are not a substitute for available structured source.

## Evidence Ladder

Default from strongest to weakest:

1. Platform or design-tool structured context with component/code mappings: Dev Mode-like inspect data, MCP design context, Code Connect/component maps, tokens, style variables, layer hierarchy, constraints, variants, and generated reference snippets.
2. Exported HTML/CSS/JS or design-tool generated code.
3. User-provided reference code or accepted existing implementation.
4. Explicit host-project shell constraints the user wants preserved.
5. Design screenshots, downloaded renders, mockups, or static images.
6. Agent inference.

Hard-constraint override: when the user explicitly requires preserving host shell boundaries (such as shared header, footer, router frame, or host layout), that shell-preservation rule is mandatory and overrides tier comparison for shell scope. Evidence ladder ranking is applied inside the allowed content scope.

When stronger and weaker sources conflict, do not silently merge them into a new hybrid structure.

## Structured Source Gate

Before classifying an input as visual-only, check whether a stronger structured source is available:

- Does the user provide a design-platform URL, file key, node ID, selection, exported package, plugin/MCP context, or generated-code link?
- Is there a connected tool that can return structure, styles, tokens, component mappings, or reference code?
- Does the project contain exported HTML, design snapshots, Code Connect files, token JSON, screenshots plus metadata, or accepted implementation for the same design?

If yes, attempt the structured path first and record the result in Gate 1:

```md
Structured source check:
- Source attempted: <platform/tool/artifact>
- Result: <available / unavailable / inaccessible / conflicting>
- Baseline decision: <structured source / accepted implementation / visual-only downgrade>
```

Do not skip this check because a screenshot is easier to access.

## No Raster Downgrade Rule

If structured context or reference code is available, do not downgrade to screenshot-based implementation. Use images only to verify final visual fidelity or to extract bitmap assets.

Allowed raster downgrade only when:

- no structured source exists, or
- the structured source is inaccessible after a real attempt, or
- the user explicitly instructs the agent to ignore the stronger source.

When downgrade is needed, ask for confirmation using the visual-only fallback wording below and state which stronger source was attempted or missing.

## Accepted Implementation Definition

`accepted existing implementation` or `accepted current implementation` means implementation that is already approved as the working baseline for this task context, for example:

- Explicitly confirmed by the user as baseline to keep or polish
- Already merged or officially adopted in the target project branch
- Marked in project docs/specs/plans as accepted baseline

The following are not accepted baseline by default:

- Personal WIP branches, draft commits, temporary experiments, or unconfirmed local changes
- Incomplete scaffold code without user or project-level acceptance signal

## What To Preserve

- Preserve structure before visual reinterpretation: section order, wrappers, major grouping, and interaction scaffolding.
- Preserve platform/component semantics from structured sources: layer hierarchy, auto-layout/constraints, style variables, variants, component names, and code-mapped components.
- Preserve explicit shell constraints (shared header, footer, router frame, host layout) and replace only the bounded content area.
- Keep copy and structural anchors from stronger artifacts unless the user explicitly asks to change them.
- Preserve design intent, not raw canvas coordinates: spacing relationships, alignment, typography, color, hierarchy, component states, and responsive behavior matter more than copying `x/y` positions.

## Existing-Project Polishing Rules

When the task is polishing an existing project:

- Treat accepted current implementation as a strong fact source (tier 2), not as disposable draft code.
- Keep behavior-compatible structure unless the user explicitly asks for replacement or transplant.
- If new design artifacts and current implementation disagree, stop and confirm intent: full replacement, partial transplant, or visual alignment only.
- Do not use polishing as implicit permission to redesign hierarchy, rewrite copy, or recompose shell boundaries.

## Conflict Handling

- Use this non-ambiguous decision rule:
- Step 1: enforce explicit shell-preservation constraints first (if user required them).
- Step 2: compare remaining conflicting sources by tier and start from the stronger source.
- Step 3: if the gap is only minor visual detail and does not change structure, interaction path, or acceptance criteria, follow the stronger source and disclose the mismatch.
- Step 4: if the gap changes structure, interaction path, acceptance criteria, or task intent, pause and ask which source wins.
- Never resolve contradictions by silent mixing.

## Allowed Engineering Adaptations

Allowed only when required by target stack or build system:

- Syntax migration (`class` to `className`, `for` to `htmlFor`, and equivalents)
- Rendering conversion (static repeats to mapped rendering, template syntax to framework syntax)
- Asset path and import normalization
- Component extraction without changing visible structure
- Minimal typing, runtime wiring, and accessibility attributes
- Translating design-tool auto-layout, constraints, grid tracks, spacing, tokens, and variants into CSS Flexbox, CSS Grid, normal flow, responsive constraints, `aspect-ratio`, and project components.

## Disallowed By Default

- Redesigning layout, typography, color, hierarchy, or interaction order
- Rewriting copy for style preferences
- Collapsing wrappers only for cleanliness
- Replacing source structure with component-library reinterpretations
- Inventing missing states, content, or interactions from visual guesswork
- Treating a design-platform URL as screenshot-only when Dev Mode-like metadata, MCP context, generated code, token data, or component mapping is available
- Downloading rendered images as the primary implementation baseline when a structured source can be read
- Treating "1:1" or "pixel-perfect" as a literal pixel-parity promise, or as permission to copy design-canvas coordinates with many `position: absolute`, `left/top`, fixed pixel coordinates, or screenshot overlays for ordinary page layout.

## Only-Visual Fallback

If only screenshots or visual mockups are available after the structured source gate (no structured platform context, exported code, reference code, tokens, component mappings, or accepted implementation), do not implement immediately.

If target stack is also unclear at the same time, this fallback confirmation takes priority over stack selection. Ask the only-visual confirmation first; after the user confirms continuing, ask for target stack only if it is still unclear.

Use this confirmation wording before implementation:

> 当前只有设计图或截图，没有导出 HTML、参考代码或现有实现。若继续，我只能按视觉关系做高保真还原，无法保证像素级 100% 一致，尤其无法保证跨响应式断点、浏览器、系统字体渲染和动态内容完全一致。请确认：现在继续做视觉还原，还是你继续提供导出 HTML、参考代码或现有实现，我再按更强基线落地？

Implementation starts only after user confirmation.
