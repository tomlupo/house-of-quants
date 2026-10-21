# House of Quants — visual identity

What the House of Quants site establishes, for agents that cannot open it.
There is no brand book: the site IS the identity. Sources, all read on
2026-10-21:

| Source | What it gives |
|---|---|
| https://tomlupo.github.io/house-of-quants/ — `stylesheets/extra.css`, md5 `b920f95f139ec94099bf8a52417eda23` (equal to the repo's file at `9f3def2`) | every colour, radius, shadow and type setting |
| `mkdocs.yml` | Material theme, `scheme: slate`, no palette toggle, no `font:` key |
| `docs/assets/house-of-quants.svg` (now `../assets/logo/house-of-quants.svg`) | the mark and its own colours |
| `docs/index.md`, `docs/about.md`, `docs/research/index.md`, `README.md` | voice, positioning, the research template |

Token values live in `../assets/css-variables.css`; this file holds the rules.
"Site" below means the source above; "derived" means the site does not give it.

## The mark

| File (`../assets/logo/`) | Source | Use on |
|---|---|---|
| `house-of-quants.svg` | the site's logo and favicon, unchanged | anywhere: it carries its own night tile |
| `house-of-quants-transparent.svg` | the same file without the background tile (one `<rect>` removed, nothing redrawn) | dark panels where a tile would box the mark |

The mark is a fan chart: a glowing bell curve over a dashed grid, one point
marked on its right shoulder (a target, `#2aaeea` with a white ring), and a row
of dots under the axis. Its own colours are the brand's blues: glow `#57c6ff`,
curve `#e8f8ff`, grid `#1b3850`, tile from `#0d2740` to `#03070c`.

Rules (site practice, not a written book):

* **Use the SVG.** Never retype "House of Quants" as a logotype beside it in
  another face; the site sets the name in Roboto next to the mark.
* **Dark only.** The mark is light lines on night blue. On a light page the
  transparent variant disappears; use the tiled file or do not place it.
* **Corners:** the tile is rounded — 8 px at header size (`--radius-sm`),
  22 px as a hero visual (`--radius-xl`), with a faint blue border and a soft
  blue glow behind it.
* **Size:** 2 rem (32 px) square in the site header; 260–360 px in the hero.
  32 px is the site's smallest use (also the favicon source); the grid and
  dots are hairlines, so do not go smaller.
* The file is 4 KB and inlines under qute-research's 200 KB logo cap.

## Colour

The brand is **dark only** (evidence: `scheme: slate` with no toggle; every
ink is light; the mark carries its own night tile). There is no light palette,
and none is derived: a report that must print on white is out of this brand.

### Surfaces (site)

| Name | HEX | RGB | Role |
|---|---|---|---|
| Night | `#060b12` | 6 / 11 / 18 | page |
| Panel | `#0b1420` | 11 / 20 / 32 | panel |
| Panel soft | `#0e1a29` | 14 / 26 / 41 | inset panel, chip, chart grid |
| Header | `#08111c` | 8 / 17 / 28 | header (Material primary) |

The page is not flat: a vertical gradient `#07101a` → `#050911` with a faint
blue radial glow at the top centre. The header and tabs are glass:
`rgba(5, 10, 17, .94)` with a 14 px backdrop blur and a hairline border.

### Inks (site)

| Name | HEX | RGB | Role |
|---|---|---|---|
| Ice | `#eaf6ff` | 234 / 246 / 255 | body text |
| Heading | `#f5fbff` | 245 / 251 / 255 | h1–h3 |
| Emphasis | `#f2faff` | 242 / 250 / 255 | card titles |
| Lead | `#cde9f8` | 205 / 233 / 248 | the subtitle under a title |
| Mist | `#9eb5c6` | 158 / 181 / 198 | copy, captions |
| On accent | `#04101a` | 4 / 16 / 26 | text on the blue button |

### The one accent (site)

| Name | HEX | RGB | Role |
|---|---|---|---|
| Sky | `#77cfff` | 119 / 207 / 255 | links, kicker, chart series 1 |
| Sky strong | `#43b8ff` | 67 / 184 / 255 | hover, focus (Material accent) |
| Button gradient | `#2f9fe8` → `#6bcfff` | | the primary button, 135° |

Borders are the accent at low alpha: `rgba(130, 205, 255, .16)` by default,
`.36` on hover, `.12` around the hero mark.

### Signals and chart series (derived)

The site shows no signal colours. Success `#4CC08A`, warning `#E0A458` and error
`#E36358` are qute-research's neutral dark values: HoQ report pages already
rendered them before they were named. Chart series (TOM-1361): sky first, then
lavender `#B39DDB`, aqua `#4FD1C5`, pink `#F48FB1`, mist last — kept clear of the
three signals so a series never reads as good or bad.

### Contrast (WCAG, checked 2026-10-21 on the owner's values)

| Ink | on Night | on Panel | on Panel soft | on Header |
|---|---|---|---|---|
| Ice (text) | 17.97 | 16.85 | 15.96 | 17.27 |
| Heading | 18.91 | 17.73 | 16.79 | 18.18 |
| Lead | 15.60 | 14.63 | 13.86 | 15.00 |
| Mist (muted) | 9.28 | 8.70 | 8.24 | 8.92 |
| Sky (primary) | 11.42 | 10.71 | 10.14 | 10.98 |
| Sky strong (accent) | 8.96 | 8.40 | 7.96 | 8.61 |
| Success | 8.66 | 8.12 | 7.69 | 8.32 |
| Warning | 9.04 | 8.48 | 8.03 | 8.69 |
| Error | 5.82 | 5.45 | 5.17 | 5.59 |

On-accent text on the button gradient: 6.62 (dark end) to 10.96. Every pair
passes AA for body text (4.5), so no fill needs an `-ink` text variant. Chart
series all clear 7:1 on every surface.

## Typography

| Font | Source | Licence | Use |
|---|---|---|---|
| **Roboto** 300 / 400 / 700 | Material's default (`mkdocs.yml` sets no font); loaded from Google Fonts | free (Apache 2.0) | everything |
| **Roboto Mono** 400 / 700 | Material's default code face | free (Apache 2.0) | code, dense numeric grids |

* Headings are tight: letter-spacing `-0.025em`; h1 at weight 720 (Google
  serves Roboto in 300/400/700, so it renders at 700).
* The hero title is huge and tighter still: `clamp(2.6rem, 7vw, 5.5rem)`,
  line-height `.96`, letter-spacing `-0.055em`.
* The kicker (eyebrow) is small uppercase sky blue, weight 700, spaced `.14em`.
* Copy runs at 1 rem, line-height 1.75, at most 42 rem wide, in mist.

## Layout cues (site)

* A hero split in two: text left (kicker, title, lead, copy, two buttons),
  the mark right with a blurred blue glow behind it. One column under 820 px,
  mark first.
* Cards in a three-column grid: a gradient panel, hairline border, 16 px
  radius; on hover they rise 3 px and the border brightens.
* Buttons: 10 px radius. Primary is the blue gradient with a soft glow and
  dark text; secondary is outlined with the hairline border.
* Content at most 1280 px wide. Lots of night around it.

## Voice (site copy)

* **English**, plain, first person singular on the about page ("My work sits
  between…"); impersonal elsewhere.
* **Positioning:** "Independent quantitative research"; "Quantitative
  Research & Solutions". Author: Tomasz Wilczega, CFA.
* **What the work promises:** "practical, reproducible work and
  implementation-aware conclusions"; research that "separate[s] robust
  conclusions from assumptions or open questions".
* **Discretion:** "Most production systems and proprietary research remain
  private." Public material shows reasoning, methods and selected code.
* **Disclaimer** on every report: not investment advice.
* **Research template** (`docs/research/index.md`): question, motivation, data
  and universe, methodology, results, robustness checks, implementation
  considerations, conclusions, selected code.
