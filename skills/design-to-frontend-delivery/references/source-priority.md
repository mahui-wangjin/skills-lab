# Source Priority

This reference defines baseline evidence ranking for `design-to-frontend-delivery`.
It is a foundational rule layer used by the main skill workflow, not a standalone entry.

## Evidence Ladder

Default from strongest to weakest:

1. Exported HTML/CSS/JS or design-tool generated code
2. User-provided reference code or accepted existing implementation
3. Explicit host-project shell constraints the user wants preserved
4. Design files, screenshots, mockups, or static images
5. Agent inference

Hard-constraint override: when the user explicitly requires preserving host shell boundaries (such as shared header, footer, router frame, or host layout), that shell-preservation rule is mandatory and overrides tier comparison for shell scope. Evidence ladder ranking is applied inside the allowed content scope.

When stronger and weaker sources conflict, do not silently merge them into a new hybrid structure.

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
- Preserve explicit shell constraints (shared header, footer, router frame, host layout) and replace only the bounded content area.
- Keep copy and structural anchors from stronger artifacts unless the user explicitly asks to change them.

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

## Disallowed By Default

- Redesigning layout, typography, color, hierarchy, or interaction order
- Rewriting copy for style preferences
- Collapsing wrappers only for cleanliness
- Replacing source structure with component-library reinterpretations
- Inventing missing states, content, or interactions from visual guesswork

## Only-Visual Fallback

If only screenshots or visual mockups are available (no exported code, no reference code, no accepted implementation), do not implement immediately.

Use this confirmation wording before implementation:

> 当前只有设计图或截图，没有导出 HTML、参考代码或现有实现。若继续，我只能按视觉稿还原，无法保证与设计产物 100% 一致。请确认：现在继续做视觉还原，还是你继续提供导出 HTML、参考代码或现有实现，我再按更强基线落地？

Implementation starts only after user confirmation.
