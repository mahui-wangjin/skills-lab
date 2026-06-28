# Assets and Visual Fidelity

This reference is mandatory for high-fidelity design delivery, typography-heavy pages, media-rich screens, browser screenshots, visual comparison, or any repeated "make it closer" polish loop.

## Core Rule

Do not tune around missing assets.

If the design depends on a font, font weight, icon set, bitmap, video, animation, token, gradient, shadow, border, radius, spacing value, state style, or brand media that is not available to the implementation, stop the polish loop and resolve the asset/detail fact first. Missing typography often changes text width, line breaks, hierarchy, perceived spacing, and layout density; adjusting CSS around a fallback font creates churn and usually makes the final project worse once the real font arrives. Missing icons and component detail tokens create a different failure: the page may look "close" while it silently leaves the design system.

## Gate 1 Asset Inventory

Before implementation or serious polish, record an inventory:

```md
Typography and asset inventory:
- Fonts: <family + weights/styles/variable axes + source>
- Font delivery: <self-hosted @font-face / provider package or CDN / system fallback / missing>
- Font license/provenance: <confirmed / user-provided / open provider / unknown>
- Images/media: <source files, export paths, remote URLs, placeholders, missing>
- Icons/illustrations: <project icon library / component mapping / exported SVG / remote asset / missing / approved fallback>
- Design tokens: <colors, borders, radii, shadows, spacing, opacity, motion tokens source>
- Interaction detail variants: <hover / active / pressed / focus-visible / selected / disabled / loading / error / success source>
- Fallback decisions: <none / approved fallback / blocked pending asset>
```

Use the strongest available source: design-platform inspect data, Dev Mode/MCP, generated code, exported HTML/CSS, token JSON, component mapping, or accepted implementation. Screenshots are only visual evidence unless no stronger source exists.

## Font Loading Rules

1. Match the actual design font family, weight/style, line-height, letter spacing, and variable axes when available.
2. Verify the required font files or provider are present in the project, dependency, CDN, or approved asset source. A font installed on one local machine is not a project asset.
3. Prefer WOFF2 for web delivery when a web font file is available; use `@font-face` with explicit `font-family`, `src`, `font-weight`, `font-style`, and `font-display`.
4. Preload only critical above-the-fold web fonts that are known by URL and likely needed immediately. Do not preload every weight or decorative font.
5. Do not commit commercial or user-provided fonts unless the user/project confirms usage rights. If rights are unclear, ask for a licensed asset or choose an approved open/provider-backed fallback.
6. If only a fallback is available, document it as a visual risk. Do not claim high-fidelity typography parity, and never claim literal pixel-level equality.
7. For Figma/MCP workflows, remember that local desktop fonts may not be available to a server-side design agent. If the platform reports missing fonts, resolve by adding/uploading the font where the platform and implementation can access it, or by choosing an approved fallback.

## Asset Completeness Rules

- Images and media must come from project assets, design exports, approved remote URLs, or user-provided files. Do not leave blurred placeholders, random stock replacements, missing background images, or broken media while claiming fidelity.
- Icons should reuse the project icon system, mapped component, exported vector asset, or explicit remote/design asset. Approximate hand-drawn replacements are allowed only for prototypes and must be disclosed.
- If the remote/design source already contains the icon, do not recreate it manually, pick a similar icon from another library, trace it from a screenshot, or replace it with a generic symbol. Fetch/export/reuse the provided asset or ask for access.
- If an icon is semantically meaningful, preserve both the glyph and the interaction role. A generic "settings", "edit", "arrow", or "close" substitution is a defect when the design source provides a different glyph.
- Raster assets need stable dimensions or aspect-ratio constraints so late loading cannot shift the layout.
- SVGs, videos, Lottie files, and background images count as assets. Verify their import path, bundler handling, MIME/load behavior, and responsive cropping.
- Do not use screenshots of text, cards, buttons, or ordinary UI as implementation shortcuts when semantic HTML/CSS can render them.

## Detail Token Rules

Visual details are part of the source contract:

1. Border width/color, radius, padding, gap, shadow, opacity, outline, backdrop, blur, transition duration/easing, cursor, and hit-area density must come from design inspect data, tokens, generated CSS, exported HTML/CSS, accepted project components, or the nearest existing component variant.
2. Hover, active, pressed, focus-visible, selected/current, disabled, loading, submitting, error, success, and empty states are state variants. Do not invent them from personal taste; map them from the source or project pattern.
3. Rounded vs sharp corners are not stylistic afterthoughts. Preserve the source radius unless the project design system explicitly standardizes the component differently.
4. If the design shows a sharp corner, do not round it because the current UI trend does. If it shows rounded geometry, do not square it because a default browser/component style did.
5. If token names differ across design and project, map intent to the closest stable project token and record the mapping. Do not introduce one-off values unless no token/component variant exists and the exception is local.
6. When the detail source is missing, mark it as fallback/conditional and ask for the source when it affects recognizable identity, component state, or acceptance.

## Browser Verification

Before Gate 3, validate in the running target:

1. Open the page in a real browser or Playwright when the project supports it.
2. Wait for used fonts before screenshots when possible, for example with `document.fonts.ready`.
3. Check key text nodes with computed styles: `font-family`, `font-weight`, `font-style`, `font-size`, `line-height`, `letter-spacing`, and whether text wraps like the design.
4. Check `document.fonts.status`, `document.fonts.check("<weight> <size> <family>")` for critical fonts when supported, and the network panel/test output for font/image 404s.
5. Inspect rendered icons and state variants, not only static layout. Confirm clickable controls show the intended cursor/hover/focus/disabled/loading details where practical.
6. Capture desktop and mobile screenshots only after fonts and assets have loaded. Note that screenshot baselines are environment-sensitive; compare in a stable OS/browser setup.
7. Inspect console and network errors. Broken fonts/assets make the fidelity result conditional at best.

## Failure Responses

- Missing font file: add a licensed self-hosted asset or approved provider package/CDN; otherwise mark blocked or fallback.
- Missing weight/style: add the specific file/variant, not just the family name.
- Wrong line breaks: first verify loaded font and weight before changing widths or letter spacing.
- Figma missing-font alert: install/upload the same font style/version or replace it explicitly in the design; do not infer from screenshots.
- Asset 404: fix import/public path or bundler config before visual tuning.
- Placeholder media: replace with the actual asset or mark the delivery as prototype-only.
- Remote/design icon exists but is inaccessible: ask for export/access or mark blocked/conditional. Do not silently redraw it.
- Missing radius/spacing/shadow/state token: map to an accepted project token/component variant and disclose the mapping; if it changes visual identity, ask before proceeding.

## Gate 3 Closeout Requirement

A high-fidelity delivery closeout must state:

- whether required fonts/assets are bundled, provided by an approved provider, inherited from the existing project, or missing;
- whether required icons/details/tokens were reused, mapped, or marked fallback/conditional;
- whether browser verification confirmed actual font loading, asset requests, rendered icon identity, and key state details;
- any fallback typography/media/icon/detail decisions and their visual risk;
- whether screenshot/visual comparison happened after fonts were ready.

If any critical font or asset is missing, the verdict cannot be "passed" for high-fidelity visual reconstruction. Use "conditional" or "blocked pending asset". Do not use "pixel-perfect" or "100% pixel match" as a delivery verdict.
