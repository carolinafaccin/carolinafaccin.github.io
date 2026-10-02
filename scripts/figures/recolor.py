"""v2 figures: v1 frame + original map colors swapped for the brand palette.

Each mapped figure lists source colors (read from the original legend) and the
brand color that replaces them. Replacement is "soft": a pixel is treated as a
mix of the source color and the white map background, so anti-aliased edges are
recolored with the same mix instead of leaving halos. Figures not listed in MAPS
(e.g. MapBiomas legends, multi-category typologies) are copied from v1 as is.

Usage: python scripts/figures/recolor.py [--publish]   (needs Pillow, numpy)
"""
import shutil
import sys

import numpy as np
from PIL import Image

from frame import DATA, ROOT, flatten, frame

# Brand palette
CREAM, GREY, OLIVE = "#FFF8F2", "#DAD2CC", "#383C2F"
SAGE_L, SAGE, SAGE_D = "#CDD7C5", "#93A97E", "#5C704C"
YELLOW, PEACH, ORANGE_L, ORANGE, RUST = "#FDD34A", "#FED2BF", "#F5A078", "#D94400", "#7B2405"
WATER = SAGE_L

FLOODS = {"#f3d9c0": PEACH, "#a3c8e2": WATER, "#e31a1c": ORANGE, "#ff0000": ORANGE}

MAPS = {
    # Suitability: high = sage, medium = yellow, low = light orange, very low / none = rust
    "urban-suitability-index-post-disasters/urban-suitability_02": {
        "#92d050": SAGE_D, "#ffd725": YELLOW, "#ffd854": YELLOW, "#fd9517": ORANGE_L,
        "#c00000": RUST, "#65c0ec": WATER},
    # Risk: none = light sage, low = yellow, medium = orange, high = rust
    "urban-suitability-index-post-disasters/urban-suitability_03": {
        "#fce807": SAGE_L, "#fdee44": SAGE_L, "#8adf97": YELLOW, "#a6e7b0": YELLOW,
        "#fdbf6f": ORANGE, "#fdcc8d": ORANGE_L, "#ff0101": RUST, "#ff3f3f": RUST,
        "#86b5b7": WATER},
    "urban-suitability-index-post-disasters/urban-suitability_04": {
        "#ffce80": PEACH, "#ffe0af": PEACH, "#fb9a03": ORANGE, "#84cfd3": WATER,
        "#c1e7e9": WATER},
    "urban-suitability-index-post-disasters/urban-suitability_07": {
        "#e66101": SAGE_D, "#f0b576": YELLOW, "#b2abd2": ORANGE_L, "#5e3c99": RUST,
        "#84cfd3": WATER},
    "urban-suitability-index-post-disasters/urban-suitability_08": {
        "#ff7f00": SAGE_D, "#8760a3": ORANGE_L, "#dfb3f0": ORANGE_L, "#84cfd3": WATER},
    "urban-suitability-index-post-disasters/urban-suitability_10": {
        "#fcd456": YELLOW, "#f49c37": ORANGE, "#f05043": RUST, "#d7b6a2": PEACH,
        "#84cfd3": WATER},
    **{f"floods-in-small-cities/floods-rs_0{i}": FLOODS for i in range(1, 8)},
    # Population growth: decline = rust/orange, stable = grey, growth = sage
    "coastal/coastal_01": {
        "#d7191c": RUST, "#f59053": ORANGE, "#fcb567": ORANGE_L, "#fce2ad": GREY,
        "#cceaae": SAGE_L, "#7ac473": SAGE, "#226a1d": SAGE_D, "#b56e4d": RUST,
        "#a5bfdd": WATER},
    "coastal/coastal_02": {"#d4271e": RUST, "#fdbf6f": ORANGE_L, "#fecf92": ORANGE_L,
                           "#a5bfdd": WATER},
    "housing-porto-alegre/housing-poa_01": {
        "#fec0c1": PEACH, "#fb9c9a": ORANGE_L, "#fe8083": ORANGE, "#fe4241": RUST,
        "#a0cede": SAGE_L, "#b5df8b": SAGE},
    "housing-porto-alegre/housing-poa_03": {
        "#fe0000": ORANGE, "#ff00ff": RUST, "#f39323": SAGE_D, "#fdee23": YELLOW,
        "#92e0e0": WATER},
    "sociospatial-fragmentation/sociospatial_01": {"#f29eaf": ORANGE_L, "#a5bfdd": WATER},
    "sociospatial-fragmentation/sociospatial_02": {
        "#fdd26f": YELLOW, "#fb7474": ORANGE, "#b099fb": RUST},
    "sociospatial-fragmentation/sociospatial_03": {
        "#d94801": ORANGE, "#fd9243": ORANGE_L, "#752701": RUST, "#9d3401": RUST},
}


def rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], float)


def recolor(im, mapping, tol=26.0):
    a = np.asarray(im, float)
    out = a.copy()
    white = np.array([255.0, 255.0, 255.0])
    best = np.full(a.shape[:2], np.inf)
    chroma = a.max(axis=2) - a.min(axis=2)  # greys and white stay untouched
    for src, dst in mapping.items():
        s, d = rgb(src), rgb(dst)
        v = s - white
        # share of the source color in each pixel (pixel = white + t * (src - white))
        t = np.clip(np.einsum("ijk,k->ij", a - white, v) / (v @ v), 0, 1)
        resid = np.linalg.norm(a - (white + t[..., None] * v), axis=2)
        hit = (resid < tol) & (t > 0.12) & (chroma > 18) & (resid < best)
        out[hit] = white + t[hit][:, None] * (d - white)
        best[hit] = resid[hit]
    return Image.fromarray(out.round().astype(np.uint8))


def main(publish=False):
    for src in sorted((DATA / "v0").glob("*/*")):
        key = f"{src.parent.name}/{src.stem}"
        out = DATA / "v2" / src.parent.name / f"{src.stem}.webp"
        out.parent.mkdir(parents=True, exist_ok=True)
        if key in MAPS:
            img, _ = frame(recolor(flatten(Image.open(src)), MAPS[key]))
            img.save(out, "WEBP", quality=84, method=6)
            print("recolored", key)
        else:
            shutil.copy(DATA / "v1" / src.parent.name / f"{src.stem}.webp", out)
        if publish:
            shutil.copy(out, ROOT / "static/img/projects" / src.parent.name / out.name)


if __name__ == "__main__":
    main(publish="--publish" in sys.argv)
