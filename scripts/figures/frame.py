"""v1 figures: standard frame, content untouched.

Trims the uniform margin around each original figure (figures/v0 in data_dir),
then centers it on a white canvas in one of four fixed formats chosen by aspect
ratio: wide 2:1 (2000x1000), landscape 4:3 (2000x1500), portrait 3:4 (1500x2000)
or square (1800x1800),
with the same relative padding. Writes WebP to figures/v1 in data_dir and, with
--publish, copies them to static/img/projects/<slug>/<name>.webp.

Usage: python scripts/figures/frame.py [--publish]   (needs Pillow, numpy)
"""
import json
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = Path(__file__).resolve().parents[2]
DATA = Path(json.load(open(ROOT / "scripts" / "config.local.json"))["data_dir"]) / "figures"
CANVAS_BG = (255, 255, 255)  # white: blends with the maps' own background (cream looked boxed on the dark theme)
PAD = 0.04                   # padding as a share of the canvas short side
FORMATS = {"wide": (2000, 1000), "landscape": (2000, 1500), "portrait": (1500, 2000), "square": (1800, 1800)}


def trim(im, tol=12):
    """Crop the margin whose color matches the corners (white, grey, etc.)."""
    a = np.asarray(im.convert("RGB")).astype(int)
    corners = np.array([a[0, 0], a[0, -1], a[-1, 0], a[-1, -1]])
    bg = np.median(corners, axis=0)
    diff = np.abs(a - bg).max(axis=2) > tol
    rows, cols = np.where(diff.any(axis=1))[0], np.where(diff.any(axis=0))[0]
    if len(rows) == 0:
        return im
    m = 6  # keep a hairline of the original margin
    return im.crop((max(cols[0] - m, 0), max(rows[0] - m, 0),
                    min(cols[-1] + m + 1, im.width), min(rows[-1] + m + 1, im.height)))


def flatten(im):
    """Composite transparency onto white so transparent margins can be trimmed."""
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        return Image.alpha_composite(bg, im).convert("RGB")
    return im.convert("RGB")


def frame(im):
    im = trim(flatten(im))
    r = im.width / im.height
    fmt = ("wide" if r >= 1.7 else "landscape" if r >= 1.15
           else "portrait" if r <= 0.87 else "square")
    W, H = FORMATS[fmt]
    pad = int(min(W, H) * PAD)
    scale = min((W - 2 * pad) / im.width, (H - 2 * pad) / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), CANVAS_BG)
    canvas.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    return canvas, fmt


def main(publish=False):
    for src in sorted((DATA / "v0").glob("*/*")):
        slug, name = src.parent.name, src.stem
        out = DATA / "v1" / slug / f"{name}.webp"
        out.parent.mkdir(parents=True, exist_ok=True)
        img, fmt = frame(Image.open(src))
        img.save(out, "WEBP", quality=84, method=6)
        print(f"{slug}/{name}: {fmt}")
        if publish:
            shutil.copy(out, ROOT / "static/img/projects" / slug / f"{name}.webp")


if __name__ == "__main__":
    main(publish="--publish" in sys.argv)
