# Assets and Visual Fidelity

This reference is mandatory for high-fidelity design delivery, typography-heavy pages, media-rich screens, browser screenshots, visual comparison, or any repeated "make it closer" polish loop.

## Core Rule

Do not tune around missing assets.

If the design depends on a font, font weight, icon set, bitmap, video, animation, token, gradient, shadow, or brand media that is not available to the implementation, stop the polish loop and resolve the asset fact first. Missing typography often changes text width, line breaks, hierarchy, perceived spacing, and layout density; adjusting CSS around a fallback font creates churn and usually makes the final project worse once the real font arrives.

## Gate 1 Asset Inventory

Before implementation or serious polish, record an inventory:

```md
Typography and asset inventory:
- Fonts: <family + weights/styles/variable axes + source>
- Font delivery: <self-hosted @font-face / provider package or CDN / system fallback / missing>
- Font license/provenance: <confirmed / user-provided / open provider / unknown>
- Images/media: <source files, export paths, remote URLs, placeholders, missing>
- Icons/illustrations: <project icon library / exported SVG / missing / fallback>
- Design tokens: <colors, radii, shadows, spacing, motion tokens source>
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
- Icons should reuse the project icon system or exported vector assets. Approximate hand-drawn replacements are allowed only for prototypes and must be disclosed.
- Raster assets need stable dimensions or aspect-ratio constraints so late loading cannot shift the layout.
- SVGs, videos, Lottie files, and background images count as assets. Verify their import path, bundler handling, MIME/load behavior, and responsive cropping.
- Do not use screenshots of text, cards, buttons, or ordinary UI as implementation shortcuts when semantic HTML/CSS can render them.

## Browser Verification

Before Gate 3, validate in the running target:

1. Open the page in a real browser or Playwright when the project supports it.
2. Wait for used fonts before screenshots when possible, for example with `document.fonts.ready`.
3. Check key text nodes with computed styles: `font-family`, `font-weight`, `font-style`, `font-size`, `line-height`, `letter-spacing`, and whether text wraps like the design.
4. Check `document.fonts.status`, `document.fonts.check("<weight> <size> <family>")` for critical fonts when supported, and the network panel/test output for font/image 404s.
5. Capture desktop and mobile screenshots only after fonts and assets have loaded. Note that screenshot baselines are environment-sensitive; compare in a stable OS/browser setup.
6. Inspect console and network errors. Broken fonts/assets make the fidelity result conditional at best.

## Failure Responses

- Missing font file: add a licensed self-hosted asset or approved provider package/CDN; otherwise mark blocked or fallback.
- Missing weight/style: add the specific file/variant, not just the family name.
- Wrong line breaks: first verify loaded font and weight before changing widths or letter spacing.
- Figma missing-font alert: install/upload the same font style/version or replace it explicitly in the design; do not infer from screenshots.
- Asset 404: fix import/public path or bundler config before visual tuning.
- Placeholder media: replace with the actual asset or mark the delivery as prototype-only.

## Gate 3 Closeout Requirement

A high-fidelity delivery closeout must state:

- whether required fonts/assets are bundled, provided by an approved provider, inherited from the existing project, or missing;
- whether browser verification confirmed actual font loading and asset requests;
- any fallback typography/media decisions and their visual risk;
- whether screenshot/visual comparison happened after fonts were ready.

If any critical font or asset is missing, the verdict cannot be "passed" for high-fidelity visual reconstruction. Use "conditional" or "blocked pending asset". Do not use "pixel-perfect" or "100% pixel match" as a delivery verdict.
