"""Figures of projects that have their own repository: copy the README figures of each
repository (docs/img/*.png, next to this repository in ~/Repositories) to
static/img/projects/<slug>/ as WebP, at most 2000 px wide.

The figures themselves are drawn by each repository's pipeline.py. Projects listed here are
skipped by frame.py and recolor.py (see SKIP there).

Usage: python scripts/figures/from_repos.py [slug ...]   (needs Pillow)
"""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
REPOS = ROOT.parent

# site slug -> (repository, figures in page order)
PROJECTS = {
    "coastal": ("coastal", ["map_urban_expansion", "urban_timeline", "urban_growth", "land_replaced",
                            "landcover_change", "map_landcover"]),
    "housing-poa": ("housing-poa", ["map_neighborhoods", "map_form", "form_by_neighborhood", "map_period_income",
                                    "map_typology", "typology_profile", "map_mcmv", "map_case_studies"]),
    "floods-rs-2024": ("floods-rs-2024", ["map_region", "flooded_by_municipality", "share_flooded",
                                          "map_lajeado_estrela", "map_encantado_mucum", "map_santa_cruz",
                                          "map_rio_pardo", "map_candelaria", "map_marques_de_souza", "map_sinimbu"]),
    "urb-frag": ("urb-frag", ["map_index", "index_profile", "map_indicators", "map_expansion",
                              "growth_and_developments", "map_location"]),
    "mikripoli": ("mikripoli", ["map_tracts", "map_neighborhoods"]),
}
MAX_WIDTH = 2000


def publish(slug):
    repo, names = PROJECTS[slug]
    dest = ROOT / "static" / "img" / "projects" / slug
    dest.mkdir(parents=True, exist_ok=True)
    for name in names:
        im = Image.open(REPOS / repo / "docs" / "img" / f"{name}.png").convert("RGB")
        if im.width > MAX_WIDTH:
            im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
        im.save(dest / f"{name}.webp", "WEBP", quality=84, method=6)
        print(f"{slug}/{name}.webp {im.size[0]}x{im.size[1]}")


if __name__ == "__main__":
    for slug in sys.argv[1:] or PROJECTS:
        publish(slug)
