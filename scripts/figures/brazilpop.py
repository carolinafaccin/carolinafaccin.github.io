"""Figure of the BrazilPop dataset page: the 2010 population grid at 1 km for all of Brazil,
with zooms on São Paulo and Porto Alegre. The national map averages 3x3 cells, so both
show people per km². Text is limited to numbers and place names, so the
same figure serves both languages (the caption on the page says what it is).

Reads the GeoTIFF from the brazilpop outputs_dir on Google Drive (see ~/Repositories/brazilpop,
config/config.local.json) and writes static/img/datasets/brazilpop/population_2010.webp.

Usage: python scripts/figures/brazilpop.py   (needs rasterio, matplotlib and Pillow,
e.g. ~/Repositories/brazilpop/venv/bin/python)
"""
import io
import json
import sys
from pathlib import Path

import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.windows import from_bounds
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import brand  # noqa: E402

OUTPUTS = Path(json.load(open(ROOT.parent / "brazilpop" / "config" / "config.local.json"))["outputs_dir"])
TIF = OUTPUTS / "rasters/2010/01K/BRAZILPOP_POPULACAO-2010_01K_BRAZIL_2010.tif"
OUT = ROOT / "static/img/datasets/brazilpop/population_2010.webp"
FONTS = ROOT.parent / "lina-brand/fonts/source-code-pro"

BINS = [1, 10, 100, 1000, 5000, 1e9]  # people per km²
CMAP = ListedColormap(brand.LARANJA)
NORM = BoundaryNorm(BINS, CMAP.N)
ZOOMS = [("São Paulo", (-47.05, -23.95, -46.25, -23.35)), ("Porto Alegre", (-51.45, -30.25, -50.85, -29.8))]


def show(ax, src, bounds=None, factor=1):
    win = from_bounds(*bounds, src.transform) if bounds else None
    shape = None
    if factor > 1:
        h, w = (round(win.height), round(win.width)) if win is not None else src.shape
        shape = (h // factor, w // factor)
    a = src.read(1, window=win, out_shape=shape, resampling=Resampling.average)
    a = np.where(a >= 1, a, np.nan)
    b = src.window_bounds(win) if win is not None else src.bounds
    ax.imshow(a, cmap=CMAP, norm=NORM, extent=(b[0], b[2], b[1], b[3]), interpolation="nearest")
    ax.set_axis_off()
    ax.set_aspect(1 / np.cos(np.radians((b[1] + b[3]) / 2)))


def main():
    brand.setup(FONTS)
    fig = plt.figure(figsize=(10, 7.2), facecolor=brand.CREAM)
    with rasterio.open(TIF) as src:
        show(fig.add_axes([0.0, 0.08, 0.64, 0.9]), src, (-74.0, -34.0, -34.6, 5.4), factor=3)
        for i, (name, bounds) in enumerate(ZOOMS):
            ax = fig.add_axes([0.66, 0.55 - i * 0.45, 0.32, 0.4])
            show(ax, src, bounds)
            ax.set_title(name, fontsize=13, loc="left", color=brand.INK)
    cax = fig.add_axes([0.06, 0.07, 0.4, 0.022])
    cb = fig.colorbar(plt.cm.ScalarMappable(norm=BoundaryNorm(range(6), CMAP.N), cmap=CMAP), cax=cax,
                      orientation="horizontal", ticks=range(6))
    cb.ax.set_xticklabels(["1", "10", "100", "1,000", "5,000", ""], fontsize=12, color=brand.MUTED)
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=0)
    buf = io.BytesIO()
    fig.savefig(buf, dpi=200, facecolor=brand.CREAM)
    img = Image.open(buf)
    img.thumbnail((2000, 2000), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, "WEBP", quality=85)
    print(OUT, img.size)


if __name__ == "__main__":
    main()
