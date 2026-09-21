#!/usr/bin/env python3
"""Rename project images to a clean professional standard and update all markdown references."""

import os
import re
import urllib.parse
from pathlib import Path

STATIC = Path('static/img/projects')
EN_DIR = Path('content/en/projects')
PTBR_DIR = Path('content/pt-br/projects')

# Short prefix for each project slug
PREFIX = {
    'coastal':                                          'coastal',
    'dispersion-of-covid-19':                          'covid19',
    'floods-in-small-cities':                          'floods-rs',
    'housing-porto-alegre':                            'housing-poa',
    'polycentrism-and-regional-development':           'polycentrism',
    'small-cities-dynamics':                           'small-cities',
    'sociospatial-fragmentation':                      'sociospatial',
    'territorial-division-of-labor-and-urban-network': 'territorial-div',
    'territorial-management-role-of-medium-sized-cities': 'territorial-mgmt',
    'urban-suitability-index-post-disasters':          'urban-suitability',
}

LOCAL_IMG = re.compile(r'!\[([^\]]*)\]\((/img/projects/[^)]+)\)')
WP_IMG = re.compile(r'!\[([^\]]*)\]\((https://carolinafaccin\.wordpress\.com/wp-content/uploads/[^)]+)\)')


def wp_basename(url):
    return os.path.basename(urllib.parse.urlparse(url).path)


for slug, prefix in PREFIX.items():
    img_dir = STATIC / slug
    en_file = EN_DIR / slug / 'index.md'
    ptbr_file = PTBR_DIR / slug / 'index.md'

    if not img_dir.exists() or not en_file.exists():
        continue

    en_content = en_file.read_text(encoding='utf-8')

    # Extract local image paths from EN file in order
    local_matches = LOCAL_IMG.findall(en_content)
    if not local_matches:
        print(f'{slug}: no local images found, skipping')
        continue

    print(f'\n{slug}:')

    # Build old → new mapping based on order in EN file
    old_to_new = {}  # old filename → new filename
    for i, (alt, local_path) in enumerate(local_matches, start=1):
        old_name = os.path.basename(local_path)
        ext = Path(old_name).suffix
        new_name = f'{prefix}_{i:02d}{ext}'
        old_to_new[old_name] = new_name

    # Also build wp_basename → new filename for PT-BR substitution
    # We need to match WP URLs to local files by basename
    local_names_ordered = [os.path.basename(p) for _, p in local_matches]
    wp_matches = WP_IMG.findall(ptbr_file.read_text(encoding='utf-8')) if ptbr_file.exists() else []
    wp_basename_to_new = {}
    for i, (alt, wp_url) in enumerate(wp_matches, start=1):
        basename = wp_basename(wp_url)
        if basename in old_to_new:
            wp_basename_to_new[wp_url] = f'/img/projects/{slug}/{old_to_new[basename]}'
        else:
            # fallback: assign by position
            ext = Path(basename).suffix
            new_name = f'{prefix}_{i:02d}{ext}'
            wp_basename_to_new[wp_url] = f'/img/projects/{slug}/{new_name}'

    # Rename files on disk
    for old_name, new_name in old_to_new.items():
        old_path = img_dir / old_name
        new_path = img_dir / new_name
        if old_path.exists() and old_path != new_path:
            old_path.rename(new_path)
            print(f'  {old_name} → {new_name}')
        elif old_path == new_path:
            print(f'  {new_name} (already named correctly)')

    # Update EN file: replace old local paths with new ones
    new_en = en_content
    for old_name, new_name in old_to_new.items():
        new_en = new_en.replace(
            f'/img/projects/{slug}/{old_name}',
            f'/img/projects/{slug}/{new_name}'
        )
    en_file.write_text(new_en, encoding='utf-8')

    # Update PT-BR file: replace WordPress URLs with new local paths
    if ptbr_file.exists():
        ptbr_content = ptbr_file.read_text(encoding='utf-8')
        new_ptbr = ptbr_content
        for wp_url, local_path in wp_basename_to_new.items():
            new_ptbr = new_ptbr.replace(f'![]({wp_url})', f'![]({local_path})')
            # handle alt text variations
            new_ptbr = re.sub(
                r'!\[([^\]]*)\]\(' + re.escape(wp_url) + r'\)',
                lambda m, lp=local_path: f'![{m.group(1)}]({lp})',
                new_ptbr
            )
        ptbr_file.write_text(new_ptbr, encoding='utf-8')

print('\nDone. Review changes and commit.')
