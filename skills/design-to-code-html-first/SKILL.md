---
name: design-to-code-html-first
description: Use when converting a design into frontend code across React, Vue, static HTML, mini-program, or similar stacks, especially when the user may provide exported HTML/CSS/JS, design-tool generated code, existing implementation, screenshots, or mockups and fidelity depends on choosing the strongest source of truth first instead of recreating the UI from appearance alone.
---

# Design To Code HTML First

## Overview

Prioritize the strongest implementation artifact before writing code. The goal of this skill is not to produce the prettiest rewrite. The goal is to preserve structure, copy, layout, and interaction semantics as closely as the available source allows.

Read `references/source-priority.md` when the request includes multiple artifacts, conflicting artifacts, or only visual material.

## Workflow

1. Identify every available artifact: exported HTML/CSS/JS, design-tool code, existing implementation, screenshots, specs, and target project constraints.
2. Rank them with the source priority rules below.
3. Tell the user which artifact will be treated as the source of truth and why.
4. Translate structure first. Keep DOM hierarchy, copy, section order, wrappers, spacing hooks, and interaction scaffolding unless the target stack makes a direct carry-over impossible.
5. Apply only the minimum engineering adaptations required by the target stack.
6. If only visual material exists, stop and ask for confirmation before implementing.

## Source Priority

Use this default priority unless the user explicitly overrides it:

1. Exported HTML/CSS/JS or design-tool generated code
2. User-provided reference code or accepted existing implementation
3. Target-project shell constraints that the user explicitly wants preserved, such as shared header, footer, router shell, or host layout
4. Design files, screenshots, mockups, or static images
5. Your own visual inference

If a higher-priority and lower-priority artifact conflict, do not silently blend them. Either follow the stronger source and call out the mismatch, or pause and ask the user which source wins.

## Core Rules

- Prefer structural translation over visual recreation.
- Preserve the existing app shell when the user says header, footer, or layout chrome must stay unchanged. Replace only the bounded content area.
- Keep text, section order, wrapper depth, and major class or grouping structure whenever the stronger artifact provides them.
- Make framework conversions mechanically: `class` to `className`, inline handlers to framework handlers, template loops to mapped data, asset paths to project paths, and invalid HTML to valid equivalents.
- Do not "improve" layout, rewrite copy, swap components, or simplify DOM just because it looks cleaner.
- Do not treat a screenshot as permission to invent missing states, missing content, or a new structure.
- When artifacts are incomplete, missing, or contradictory, surface the gap explicitly.

## Only-Visual Fallback

If the user has provided only screenshots, mockups, or a visual design without exported code or reference implementation:

1. State that a pure visual reconstruction cannot guarantee 100% fidelity.
2. Ask the user to choose between continuing with visual restoration now or providing stronger reference artifacts first.
3. Wait for confirmation before implementing.
4. If the conversation is in Chinese, load `references/source-priority.md` and use the provided Chinese confirmation wording.

## Implementation Checklist

Before editing code, verify:

- The source of truth is explicitly chosen.
- Non-goals are explicit, for example "keep existing header and footer".
- Direct carry-over artifacts have been copied or translated before any manual rewrite.
- Framework-specific changes are minimal and justified.
- Any unresolved conflicts or missing references have been raised to the user.
