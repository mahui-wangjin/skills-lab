---
name: design-to-frontend-delivery
description: Use when delivering a frontend implementation from design artifacts or polishing an existing frontend project, especially when fidelity depends on choosing the right source of truth, preserving accepted shells, and bringing static pages to presentation-ready quality across React, Vue, static HTML, mini-program, or similar targets.
---

# Design to Frontend Delivery

## Single Entry, Two Modes

One run must produce one target frontend result. Do not produce multiple target stacks in one run.

Route by [mode-routing.md](./references/mode-routing.md):

- Auto enter `convert-and-polish` when design artifacts are the main input (design + exported HTML, or design-tool generated code) and the task is to deliver a target frontend implementation.
- Auto enter `polish-existing-project` when an accepted existing frontend project is the main baseline and the task is to keep polishing interactions, validation, states, modals, animation, or acceptance quality.
- If both existing project and new design/HTML are present but intent is unclear, stop and ask which path is primary before implementation.

## Mandatory Reference Loading Rules

Reference loading is required, not optional:

- When there are multiple fact sources, source conflicts, or visual-only inputs, you must read [source-priority.md](./references/source-priority.md) before implementation decisions.
- After mode is locked, you must read exactly one mode reference before implementation details:
  - `convert-and-polish` -> [convert-and-polish.md](./references/convert-and-polish.md)
  - `polish-existing-project` -> [polish-existing-project.md](./references/polish-existing-project.md)
- For all gate checks and final closeout output, you must read [delivery-checklists.md](./references/delivery-checklists.md) and follow its required artifacts.

## Three Gates

Canonical gate checks and closeout outputs are defined in [delivery-checklists.md](./references/delivery-checklists.md).

1. Gate 1 (pre-start confirmation)
- Lock mode, target stack, baseline artifacts, source-of-truth, scope, non-goals, and shell boundary.

2. Gate 2 (mode-aware middle gate)
- `convert-and-polish`: structure mapping and shell-boundary pass before polish.
- `polish-existing-project`: current-state audit plus scope-gap closure decision before implementation continues.

3. Gate 3 (acceptance and closeout gate)
- Verify demo-ready polish quality and produce final acceptance, risk, documentation update record, and next-step decision.

## Must Ask vs Can Decide

Must ask:

- Target stack is not specified and repository stack is not clear.
- Even for strong-vs-weaker conflicts like exported HTML vs design file/screenshot, if conflict touches structure, interaction path, or acceptance criteria, pause and ask which source is authoritative.
- Strong sources conflict on structure, primary flow, interaction path, or acceptance criteria.
- Existing project and new design/HTML are both present, but replacement/transplant/alignment intent is unclear.
- Only visual artifacts are provided (no exported HTML, no reference code, no accepted implementation).
- Shell preservation boundary is unclear (header/footer/layout/router).

Can decide without asking:

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
- [mode-routing.md](./references/mode-routing.md)
- [convert-and-polish.md](./references/convert-and-polish.md)
- [polish-existing-project.md](./references/polish-existing-project.md)
- [delivery-checklists.md](./references/delivery-checklists.md)
