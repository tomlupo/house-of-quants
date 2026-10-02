"""Drift guard: the qute-research brand pack is a copy of the site's CSS tokens.

`docs/stylesheets/extra.css` owns the colours; `.qute/brand.json` copies them for
qute-research renderers (TOM-1361). Each pack key names the CSS variable it
copies, so a colour changed in one place and not the other turns this red.

The site is dark-only (mkdocs.yml: `scheme: slate`, no toggle), so the pack is
`single_theme: dark`. Keys the CSS has no token for are listed in UNSOURCED and
stay pack-owned: good/warn/bad are omitted and fall back to qute-research's
neutral dark palette; chart series 1-4 are pack-owned hues readable on the navy.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PACK_OWNER = {
    "bg": "hoq-bg",
    "panel": "hoq-panel",
    "ink": "hoq-text",
    "muted": "hoq-muted",
    "line": "hoq-border",
    "grid": "hoq-panel-soft",
    "chip": "hoq-panel-soft",
    "primary": "hoq-blue",
    "accent": "hoq-blue-strong",
    "header_bg": "md-primary-fg-color",
    "header_ink": "hoq-text",
}
UNSOURCED = {"good", "warn", "bad"}
# chart index -> CSS variable; the other indices are pack-owned
CHART_OWNER = {0: "hoq-blue", 5: "hoq-muted"}


def _norm(v):
    return re.sub(r"\s+", "", v).lower()


def test_brand_pack_equals_the_site_css():
    css = (ROOT / "docs/stylesheets/extra.css").read_text()
    owner = {
        k: _norm(v)
        for k, v in re.findall(r"--([\w-]+):\s*([^;]+);", css)
        if not v.strip().startswith("var(")
    }
    pack = json.loads((ROOT / ".qute/brand.json").read_text())
    assert pack["single_theme"] == "dark" and "light" not in pack
    assert set(pack["dark"]) == set(PACK_OWNER)
    assert not UNSOURCED & set(pack["dark"])
    for k, v in pack["dark"].items():
        assert _norm(v) == owner[PACK_OWNER[k]], k
    for i, token in CHART_OWNER.items():
        assert _norm(pack["chart"][i]) == owner[token], f"chart[{i}]"
