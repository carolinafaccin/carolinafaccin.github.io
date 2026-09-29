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
`content/<lang>/projects/<slug>/index.md` + a `feature.png` cover image.
Project front matter uses `categories` (used by the category filter) and
`summary`. The two language trees must be kept in sync manually when adding
pages.

**Layout overrides live in `layouts/` and shadow the theme** in
`themes/blowfish/layouts/`. Hugo merges these, with the project root winning.
Notable custom overrides:

- `layouts/partials/home/profile.html` — profile homepage card
- `layouts/about/list.html` — custom About page (pulls
  `assets/img/profile_about.jpeg`, renders a TOC)
- `layouts/shortcodes/category-filter.html` — pill links over
  `site.Taxonomies.categories`
- `layouts/partials/head.html`, `extend-head.html`, `favicons.html`

When changing site appearance, check whether the relevant template is
overridden here before editing the theme submodule (don't edit the submodule).

**Custom color scheme** is `assets/css/schemes/carolina.css` (referenced by
`colorScheme = "carolina"`); extra styles in `assets/css/custom.css`.

## Deploy

Push to `main` triggers `.github/workflows/deploy.yml`: installs Hugo extended,
checks out with `submodules: recursive`, builds with `--minify`, and publishes
`./public` to GitHub Pages. No manual deploy step.

## Setup on a new machine / what lives outside git

Everything needed to build and deploy is in this repo; nothing depends on `data_dir`/`raw_dir` (the Google Drive `Workspace/Data` catalog used by the data repos) or on untracked local files. A fresh clone is verified to build:

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/carolinafaccin/carolinafaccin.github.io.git ~/Repositories/carolinafaccin.github.io
cd ~/Repositories/carolinafaccin.github.io && hugo --minify
```

- Repo is ~950 MB (history of `static/img` and `static/pdf`); the shallow submodule flag skips the theme's history. If cloned without submodules: `git submodule update --init --depth 1`.
- Gitignored and safe to lose (all regenerable or trivial): `public/`, `resources/_gen/`, `.hugo_build.lock`, `venv/` (see `requirements.txt`; only for the deleted migration scripts), `.claude/`, `.remember/`, `.vscode/`, `.aider*`, `.DS_Store`.
- Original WordPress-era images (covers, photos, icon, logos) are only on Google Drive: `Personal/Portfolio/2024_wordpress_v2/` and `Personal/Portfolio/2025_portfolio_id_v3/`. Used versions are already in `static/` and `assets/`.
- Migration scripts were deleted from the tree; recover them from git history (commit `de2b364`).

## Migration scripts (removed)

`wp_to_hugo.py`, `download_images.py`, `rename_images.py` were one-off WordPress migration helpers. They are no longer in the tree (see git history, commit `de2b364`) and are not part of the build.
