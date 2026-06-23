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

## Migration scripts (gitignored)

`wp_to_hugo.py`, `download_images.py`, `rename_images.py` are one-off WordPress
migration helpers run inside `venv/`. They are excluded from git and not part of
the build.
