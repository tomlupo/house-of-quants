# House of Quants — design tokens

How to use the tokens. **Values live in one place, `../assets/css-variables.css`;**
this file names roles and never repeats a value, so it cannot drift. The rules
behind them (the mark, palette, fonts, voice) are in `identity.md`.

The brand is dark only: there is no light theme to switch to.

## Colour roles

| Role | Token | Use |
|---|---|---|
| Page | `--color-background`, with `--glow-page` over `--gradient-page` as the body background | night navy |
| Panel, card, table body | `--color-surface` | |
| Inset panel, chip, chart grid, table head | `--color-surface-soft` | |
| Card fill | `--gradient-card` | the site's cards |
| Header | `--color-header`; `--color-header-glass` for a blurred sticky header | |
| Body text | `--color-text` | |
| Headings | `--color-heading` | h1–h3 |
| Card title | `--color-text-emphasis` | |
| Subtitle under a title | `--color-text-lead` | |
| Copy, captions, axis labels | `--color-text-muted` | |
| The one accent | `--color-primary` | links, kicker, key number, chart series 1 |
| Hover, focus | `--color-accent` | |
| Primary button | `--gradient-accent` fill, `--color-text-on-accent` text, `--glow-accent` shadow | |
| Hairlines | `--color-border`; `--color-border-hover` on hover; `--color-border-faint` round the mark | |
| Positive, negative, caution | `--color-success`, `--color-error`, `--color-warning` | fills and text alike; all pass AA as text |
| Chart series | `--chart-1` … `--chart-5` | in this order; never success/warning/error |

## Type roles

| Role | Tokens |
|---|---|
| Body | `--font-family-base`, `--font-weight-regular`, `--font-size-body` |
| Long copy | `--line-height-copy`, `--copy-max-width`, `--color-text-muted` |
| Headings | `--font-weight-title` (h1), `--font-weight-bold`, `--letter-spacing-heading` |
| Hero title | `--font-size-title`, `--line-height-title`, `--letter-spacing-title` |
| Subtitle | `--font-size-lead`, `--color-text-lead` |
| Eyebrow | class `.hoq-kicker` (`--font-size-kicker`, `--letter-spacing-kicker`, uppercase) |
| Figures | class `.hoq-num` (tabular numerals); `--font-family-mono` for dense grids and code |

## Space, radius, shadow, motion

`--content-max-width`, `--copy-max-width`; `--radius-sm` (mark in a header),
`--radius-md` (buttons), `--radius-lg` (cards), `--radius-xl` (mark as a
visual); `--shadow-card-hover`, `--shadow-visual`, `--glow-visual`;
`--transition-card`.

## Components

Defined in the CSS file: `.hoq-kicker`, `.hoq-card` (with a `strong` title and a
`span` line), `.hoq-num`. The site's layout pieces (`.hoq-hero`, `.hoq-grid`,
`.hoq-visual`, `.hoq-title`, `.hoq-subtitle`, `.hoq-copy`, `.hoq-actions`) live in
the repo's `docs/stylesheets/extra.css` and read only these tokens.

## Tailwind

`../assets/tailwind.config.js` mirrors the CSS values by hand. Class names
follow the roles: `bg-background`, `bg-surface`, `bg-surface-soft`,
`text-foreground`, `text-heading`, `text-lead`, `text-muted`, `text-primary`,
`bg-accent`, `bg-accent-from`, `text-on-accent`, `border-border`,
`text-success`, `text-error`, `bg-chart-1`, `bg-page`, `bg-card`, `shadow-glow`,
`rounded-lg`, `font-mono`, `text-title`, `text-kicker`.

## Copies to keep equal

`tests/test_brand_pack.py` fails when a copy differs from the CSS file:

* `.qute/brand.json` — the qute-research brand pack that report pages wear;
* `docs/stylesheets/brand.css` and `docs/assets/house-of-quants.svg` must stay
  symlinks to the owner;
* `docs/stylesheets/extra.css` must hold no colour;
* `tailwind.config.js` may name only colours the owner holds.

Not checked here (another tree): Quark's pack, `agents/quark/.qute/brand.json`,
stamped by `agents/quark/.qute/PROVENANCE.md`.
