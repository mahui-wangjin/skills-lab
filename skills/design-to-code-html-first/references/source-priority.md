# Source Priority Reference

Use this file when a design-to-code request includes multiple artifacts, conflicting artifacts, or only visual material.

## Evidence Ladder

Default from strongest to weakest:

1. Exported HTML, CSS, JS, or design-tool generated code
2. User-provided reference code or an accepted existing implementation
3. Explicit host-project constraints the user wants preserved, such as shared header, footer, shell, or routing frame
4. Design files, screenshots, mockups, or static images
5. Agent inference

Do not silently merge stronger and weaker sources into a third invented structure.

## What Counts As Reference Code

Treat the following as strong implementation artifacts:

- Stitch, Figma Dev Mode, Framer, Webflow, or similar exported HTML and CSS
- Static prototype pages
- Existing accepted pages in the target project
- User-provided snippets that clearly define DOM structure, content, or interaction scaffolding
- Existing shared shell files when the user explicitly says they must remain unchanged

Treat the following as weaker visual guidance:

- PNG, JPG, PDF, screenshot, or mockup only
- Manually described visual ideas without code
- Approximate layout references from unrelated products

## Conflict Handling

- If exported code and a screenshot differ in small details, prefer the exported code and call out the mismatch.
- If reference code and the current project implementation differ, ask whether the task is replacement, partial transplant, or visual alignment only.
- If the mismatch changes structure, interaction, or acceptance criteria, stop and ask the user which source wins.
- Never resolve contradictions by inventing a new hybrid structure without telling the user.

## Allowed Engineering Adjustments

These changes are allowed when required by the target stack or build system:

- Convert `class` to `className`, `for` to `htmlFor`, and similar syntax migrations
- Replace static loops or repeated blocks with framework list rendering
- Normalize asset paths, imports, and route links
- Split large markup into components without changing visible structure
- Add types, tests, accessibility attributes, and minimal runtime wiring
- Preserve existing header, footer, or shell and replace only the bounded content area when the user asks for that

## Disallowed Without Explicit Approval

Do not do these by default:

- Redesign spacing, typography, color, or component hierarchy
- Rewrite copy because it feels redundant or crowded
- Collapse wrappers or flatten DOM for cleanliness alone
- Replace the original structure with a component-library interpretation
- Invent missing content, states, or interactions from visual guesses
- Treat a screenshot as permission to ignore stronger code artifacts

## Only-Visual Fallback

If only visual material exists, do not implement immediately. First confirm that the user accepts a visual-only restoration path and understands the fidelity risk.

Recommended Chinese wording:

> 当前只有设计图或截图，没有导出 HTML、参考代码或现有实现。若继续，我只能按视觉稿还原，无法保证与设计产物 100% 一致。请确认：现在继续做视觉还原，还是你继续提供导出 HTML、参考代码或现有实现，我再按更强基线落地？

Implementation must wait for the user's confirmation.
