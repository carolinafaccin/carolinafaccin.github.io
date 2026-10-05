# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Carolina Faccin's professional website (`carolinafaccin.github.io`), a static
Hugo site built on the **Blowfish** theme. Migrated from WordPress; deployed to
GitHub Pages. Bilingual: English (default) and Brazilian Portuguese.

## Commands

```bash
hugo server -D        # local dev server with drafts, live reload at :1313
hugo                  # production build into ./public/
hugo --minify         # what CI runs (with --baseURL injected by GitHub Pages)
hugo new content/en/projects/<slug>/index.md   # scaffold from archetypes/
```

Requires **Hugo extended v0.161.1+** (CI pins 0.161.1). The extended build is
mandatory — the theme uses SCSS/asset pipelines.

After cloning, fetch the theme submodule:

```bash
git submodule update --init --recursive
```

## Architecture

**Config is split, not single-file.** All settings live in `config/_default/`,
loaded by Hugo automatically — there is no top-level `hugo.toml`:

- `hugo.toml` — core (baseURL, taxonomies, outputs, pagination)
- `params.toml` — Blowfish params: homepage `layout = "profile"`, custom
  `colorScheme = "carolina"`, Umami analytics
- `languages.en.toml` / `languages.pt-br.toml` — per-language title, author
  block (name/image/headline/bio/links), `contentDir`
- `menus.en.toml` / `menus.pt-br.toml` — nav menus per language

**Content is per-language under `content/<lang>/`.** `content/en/` and
`content/pt-br/` mirror each other. Projects are page bundles:
`content/<lang>/projects/<slug>/index.md` + a `feature.jpg` cover image.
Project front matter: `summary`, `categories` (one of four theme groups, named
per language: Climate & Environment / Clima e Ambiente, Urban Form & Land Use /
Forma Urbana e Uso do Solo, Housing & Inequality / Habitação e Desigualdade,
Regional Development / Desenvolvimento Regional), `featured: <n>` (shows on
the homepage "Selected work" in that order, 1 first; first 3 shown), and the facts-box fields `period`,
`location`, `partners`, `role`, `data`, `tools`. `date` only orders projects
(set it to the end of the period); dates, reading time and sharing are hidden, and the
project cards show `period` instead (`layouts/partials/article-meta/basic.html`).
The two language trees must be kept in sync manually when adding pages.

Project page body pattern: `{{< lead >}}` question, `{{< facts >}}`, then
challenge / approach (with a `{{< flow >}}` + `{{< step >}}` methodology
diagram) / results / why it matters / links / maps (`{{< figs cols="2" >}}` +
`{{< fig src alt caption >}}`). Every figure needs real alt text.
Figures live in `static/img/projects/<slug>/` as WebP, max 2000 px. Five projects have their own public repository (github.com/carolinafaccin/<repo>, cloned next to this one in `~/Repositories`), whose `pipeline.py` draws the figures and copies them to `docs/img/`: `coastal`, `housing-poa`, `floods-rs-2024`, `urb-frag` and `mikripoli` (slug = repo name). `python scripts/figures/from_repos.py [slug]` converts them to WebP here. The older figures (v1 frame, v2 recolor) come from `scripts/figures/frame.py` and `recolor.py`, which skip the repository projects (`SKIP`, `SKIP_FILES`; their `outputs_dir` folders keep the old slugs, mapped by `RENAMED`). Old project URLs (`housing-porto-alegre`, `floods-in-small-cities`, `sociospatial-fragmentation`, `small-cities-dynamics`) redirect through front-matter `aliases`.

**Layout overrides live in `layouts/` and shadow the theme** in
`themes/blowfish/layouts/`. Hugo merges these, with the project root winning.
Notable custom overrides:

- `layouts/partials/home/profile.html` — profile homepage card
- `layouts/about/list.html` — custom About page (pulls
  `assets/img/profile_about.jpeg`, renders a TOC)
- `layouts/shortcodes/category-filter.html` — pill links over
  `site.Taxonomies.categories`
- `layouts/partials/head.html` (home title from `params.homeTitle`, social
  image fallback), `extend-head.html` (Source Code Pro), `favicons.html`
- `layouts/partials/recent-articles/main.html` — homepage "Selected work" (ordered by `featured`) +
  "See all projects" button
- `layouts/partials/header/basic.html` — copy of theme header, only adds logo alt
- `layouts/shortcodes/facts.html`, `flow.html`, `step.html`, `figs.html`,
  `fig.html` — project page components, styled in `assets/css/custom.css`
- `i18n/en.yaml`, `i18n/pt-br.yaml` — strings for the above

When changing site appearance, check whether the relevant template is
overridden here before editing the theme submodule (don't edit the submodule).

**Brand identity** lives in the private repository `lina-brand` (sibling folder in
`~/Repositories`; designer Juji, 2025): typeface Source Code Pro; palette cream #FFF8F3,
peach #FFD5C2, yellow #FFD348, orange #D94701, rust #7E2704, sage #92A87E, light sage
#CCD5C2, dark olive #383D2F, ink #1F2417; motif is thin street-block linework. Files
here that come from it (do not edit, run `npm run sync` in lina-brand):
`assets/css/schemes/carolina.css` (`colorScheme = "carolina"`), `static/icon.png`,
`assets/img/icon.png`, the favicons (`static/favicon.ico`, `favicon.svg`, `apple-touch-icon.png`,
`icon-192.png`; linked in `layouts/partials/favicons.html` with `static/site.webmanifest`)
and `scripts/brand.py` (colors for the covers and the v2 recolor).
Extra styles in `assets/css/custom.css`.

**Project covers** are generated from OpenStreetMap street networks of each study
area in brand colors (background = theme group). Scripts: `scripts/covers/`
(`fetch.py` downloads via Overpass, `render.py` draws 1600x900 JPGs; needs
Pillow). `assets/img/social.jpg` is the default share image.

## Deploy

Push to `main` triggers `.github/workflows/deploy.yml`: installs Hugo extended,
checks out with `submodules: recursive`, builds with `--minify`, and publishes
`./public` to GitHub Pages. No manual deploy step.

## Setup on a new machine / what lives outside git

Everything needed to build and deploy is in this repo; the build does not depend on `outputs_dir`/`sources_dir` or on untracked local files. A fresh clone is verified to build:

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/carolinafaccin/carolinafaccin.github.io.git ~/Repositories/carolinafaccin.github.io
cd ~/Repositories/carolinafaccin.github.io && hugo --minify
```

- `scripts/config.local.json` (gitignored; template in `scripts/config.local.json.example`) sets `outputs_dir` = Google Drive `Meu Drive/Workspace/Data/outputs/carolinafaccin.github.io`. The project report PDFs are mirrored there under `pdf/` (same structure as `static/pdf/`), as the first step of moving them out of the repo: once they are shared on Drive, replace the `/pdf/...` links in the urban-suitability pages with Drive links and delete `static/pdf/`.
- Repo is ~950 MB (history of `static/img` and `static/pdf`); the shallow submodule flag skips the theme's history. If cloned without submodules: `git submodule update --init --depth 1`.
- Gitignored and safe to lose (all regenerable or trivial): `public/`, `resources/_gen/`, `.hugo_build.lock`, `venv/` (see `requirements.txt`; only for the deleted migration scripts), `.claude/`, `.remember/`, `.vscode/`, `.aider*`, `.DS_Store`.
- Original WordPress-era images (covers, photos, icon, logos) are only on Google Drive: `Personal/Portfolio/2024_wordpress_v2/` and `Personal/Portfolio/2025_portfolio_id_v3/`. Used versions are already in `static/` and `assets/`.
- Migration scripts were deleted from the tree; recover them from git history (commit `de2b364`).

## Migration scripts (removed)

`wp_to_hugo.py`, `download_images.py`, `rename_images.py` were one-off WordPress migration helpers. They are no longer in the tree (see git history, commit `de2b364`) and are not part of the build.
