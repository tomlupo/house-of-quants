---
name: hoq-brand
description: Applies the House of Quants brand identity, as the House of Quants site sets it — the fan-chart mark, a dark-only night-navy palette with one sky-blue accent, Roboto typography, voice. Use for any House of Quants output and for Quark's research pages: HTML reports and dashboards, qute-research pages, React/Tailwind/CSS, charts, slides. The qute-research brand packs (.qute/brand.json here, agents/quark/.qute/brand.json) are copies of these tokens.
---

# House of Quants Brand Guidelines

## Overview

House of Quants is Tom's independent quantitative research publication
("Quantitative Research & Solutions"), published at
https://tomlupo.github.io/house-of-quants/. It is the brand of his published
research, and Quark's research pages wear it too (Tom, 2026-10-21).

There is no brand book. The source is the site itself: its stylesheet, its
`mkdocs.yml` and its mark. This skill is the master. The site loads this
skill's CSS file directly, and every other copy is checked against it.

**Keywords**: house of quants, hoq, quark, branding, visual identity, quant research, dark theme, logo, tailwind, css variables, design tokens, reports, charts

## Files

| File | Holds |
|---|---|
| `assets/css-variables.css` | **every brand value** (the owner) + base component classes |
| `assets/tailwind.config.js` | the same values for Tailwind (hand mirror, colours checked) |
| `assets/logo/*.svg` | the mark: the site's own file, and the same file without its tile |
| `references/identity.md` | the site's rules: the mark, full palette with RGB, contrast table, fonts and licences, layout, voice |
| `references/design-tokens.md` | which token to use for which role |

## Brand voice & tone

Read `references/identity.md` § Voice for the quoted source lines.

- **English.** First person singular when Tom speaks about his work ("My work
  sits between quantitative research, engineering, and implementation");
  impersonal in research text.
- **Practical and reproducible.** Conclusions are "implementation-aware". Say
  what would change in a real portfolio, not only what the backtest shows.
- **Honest about evidence.** Separate robust conclusions from assumptions and
  open questions. Name what was not tested.
- **Discreet.** "Most production systems and proprietary research remain
  private." Show reasoning, methods and selected code, never client data or
  private strategy parameters.
- **Plain.** Short sentences, no hype, no superlatives about returns.
- **Every report says it is not investment advice.**

### Research structure

A longer piece follows the site's template: research question, motivation,
data and universe, methodology, results, robustness checks, implementation
considerations, conclusions, selected code or notebook.

## Visual identity in brief

Read `references/identity.md` before designing; this is the summary.

- **Dark only.** Night navy pages, light inks, one accent. There is no light
  theme; do not invent one. The page has a faint blue glow at the top.
- **One accent: sky blue.** Links, the eyebrow, the key number, chart series 1,
  the primary button (a blue gradient with dark text and a soft glow).
- **Mark:** always the SVG from `assets/logo/`. Use the tiled file anywhere, or
  the transparent one on a dark panel. Round its corners and never recolour it.
- **Signals:** green up, red down, amber caution (derived). Chart series never
  use these three hues.
- **Type:** Roboto for all text, Roboto Mono for code and dense grids, with
  tabular figures in tables. Headings are tight (negative letter-spacing).
  Eyebrows are small uppercase sky blue with wide spacing.
- **Shape:** hairline borders in translucent blue, 16 px cards that lift on
  hover, 10 px buttons, generous space.

## Reports

HTML reports are built with the qute-research reporting library. They wear the
brand through a `.qute/brand.json` pack (`single_theme: dark`), which is a copy
of the CSS tokens:

- `.qute/brand.json` in this repo, checked by `tests/test_brand_pack.py`;
- `agents/quark/.qute/brand.json` (workspace tree, edited live). It has the same
  colours, fonts and mark, and Quark's own name, eyebrow and footer. Its
  `PROVENANCE.md` names this skill and the commit it copies.

## Usage

### CSS variables

Link `assets/css-variables.css` (the site serves it at
`https://tomlupo.github.io/house-of-quants/stylesheets/brand.css`), or copy its
`:root` block. Style through the tokens (`var(--color-primary)`,
`var(--font-family-base)`). Load Roboto from Google Fonts:
`https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Roboto+Mono:wght@400;700&display=swap`.
An offline report embeds the fonts or falls back to the system stack.

### Tailwind

Copy or extend `assets/tailwind.config.js`. Class names follow the role names
(`bg-surface`, `text-muted`, `bg-accent`, `bg-chart-1`).

### Changing a value

1. Change it in `assets/css-variables.css`. The site picks it up because
   `docs/stylesheets/brand.css` is a symlink to this file.
2. Change it in `tailwind.config.js` and `.qute/brand.json`. Run `pytest tests`,
   which fails until the copies match.
3. Change it in `agents/quark/.qute/brand.json`, then update the commit in
   `agents/quark/.qute/PROVENANCE.md`.
4. If the value is a text or background colour, the same tests check its
   contrast (AA). Update the table in `references/identity.md` § Contrast.
