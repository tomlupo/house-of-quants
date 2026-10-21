"""Drift guard: every copy of the House of Quants brand equals its one owner.

The owner is the brand skill's `.claude/skills/hoq-brand/assets/css-variables.css`
(Tom, 2026-10-21: a full HoQ brand skill, which Quark also wears). The site
loads it as `docs/stylesheets/brand.css`, a symlink, so the site cannot hold
a second copy. These tests fail when:

- the symlinks stop pointing at the owner (site CSS and site logo);
- `docs/stylesheets/extra.css` gets a colour literal back (a second copy);
- `.qute/brand.json`, the qute-research pack (TOM-1361), differs from the owner;
- `tailwind.config.js`, the hand mirror, names a colour the owner lacks.

The site is dark-only (mkdocs.yml: `scheme: slate`, no toggle), so the pack is
`single_theme: dark`. Chart series stay clear of good/warn/bad, so a series
never reads as a signal. Quark's copy lives in another tree
(`agents/quark/.qute/`) and is stamped by its PROVENANCE note, not checked here.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".claude/skills/hoq-brand"
OWNER = SKILL / "assets/css-variables.css"
LOGO = SKILL / "assets/logo/house-of-quants.svg"

# pack palette key -> owner token
PACK_OWNER = {
    "bg": "color-background",
    "panel": "color-surface",
    "ink": "color-text",
    "muted": "color-text-muted",
    "line": "color-border",
    "grid": "color-surface-soft",
    "chip": "color-surface-soft",
    "primary": "color-primary",
    "accent": "color-accent",
    "good": "color-success",
    "warn": "color-warning",
    "bad": "color-error",
    "header_bg": "color-header",
    "header_ink": "color-text",
}
COLOUR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)")


def _norm(v):
    return re.sub(r"\s+", "", v).lower()


def _owner():
    tokens = dict(re.findall(r"--([\w-]+):\s*([^;]+);", OWNER.read_text()))
    assert len(tokens) > 40, f"read {len(tokens)} tokens from {OWNER}"
    return {k: _norm(v) for k, v in tokens.items()}


def test_site_wears_the_owner_through_symlinks():
    for link, target in (
        (ROOT / "docs/stylesheets/brand.css", OWNER),
        (ROOT / "docs/assets/house-of-quants.svg", LOGO),
    ):
        assert link.is_symlink(), f"{link} must be a symlink to the owner"
        assert link.resolve() == target.resolve(), link


def test_site_loads_brand_before_extra():
    mk = (ROOT / "mkdocs.yml").read_text()
    assert mk.index("stylesheets/brand.css") < mk.index("stylesheets/extra.css")


def test_extra_css_holds_no_colour_literal():
    css = (ROOT / "docs/stylesheets/extra.css").read_text()
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    assert not COLOUR.findall(css), "a colour in extra.css is a second copy"


def test_brand_pack_equals_the_owner():
    owner = _owner()
    pack = json.loads((ROOT / ".qute/brand.json").read_text())
    assert pack["single_theme"] == "dark" and "light" not in pack
    assert set(pack["dark"]) == set(PACK_OWNER)
    for k, v in pack["dark"].items():
        assert _norm(v) == owner[PACK_OWNER[k]], k
    chart = [owner[k] for k in sorted(owner) if k.startswith("chart-")]
    assert [_norm(c) for c in pack["chart"]] == chart
    assert _norm(pack["font"]) == owner["font-family-base"]
    assert _norm(pack["mono"]) == owner["font-family-mono"]
    assert (ROOT / ".qute" / pack["logo"]).resolve() == LOGO.resolve()


def test_chart_series_never_read_as_signals():
    owner = _owner()
    signals = {owner[t] for t in ("color-success", "color-warning", "color-error")}
    chart = {v for k, v in owner.items() if k.startswith("chart-")}
    assert not chart & signals


def _luminance(hex_):
    c = [int(hex_[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def _contrast(a, b):
    hi, lo = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def test_every_ink_passes_aa_on_every_surface():
    """WCAG AA: 4.5:1 for text, 3:1 for chart marks (identity.md § Contrast)."""
    owner = _owner()
    surfaces = [
        "color-background",
        "color-surface",
        "color-surface-soft",
        "color-header",
    ]
    inks = [
        "color-text",
        "color-heading",
        "color-text-emphasis",
        "color-text-lead",
        "color-text-muted",
        "color-primary",
        "color-accent",
        "color-success",
        "color-warning",
        "color-error",
    ]
    marks = [k for k in owner if k.startswith("chart-")]
    low = [
        (ink, bg, round(_contrast(owner[ink], owner[bg]), 2))
        for ink in inks + marks
        for bg in surfaces
        if _contrast(owner[ink], owner[bg]) < (3.0 if ink in marks else 4.5)
    ]
    for end in ("color-accent-from", "color-accent-to"):
        r = _contrast(owner["color-text-on-accent"], owner[end])
        if r < 4.5:
            low.append(("color-text-on-accent", end, round(r, 2)))
    assert not low, low


def test_tailwind_mirror_names_only_owner_colours():
    owner_colours = {_norm(c) for c in COLOUR.findall(OWNER.read_text())}
    tw = (SKILL / "assets/tailwind.config.js").read_text()
    used = {_norm(c) for c in COLOUR.findall(tw)}
    assert used, "tailwind.config.js names no colour"
    assert used <= owner_colours, sorted(used - owner_colours)
