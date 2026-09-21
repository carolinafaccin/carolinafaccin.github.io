#!/usr/bin/env python3
"""Download WordPress images referenced in Hugo markdown files and update links."""

import os
import re
import urllib.request
import urllib.parse
from pathlib import Path

PROJECTS_DIR = Path('content/en/projects')
STATIC_DIR = Path('static/img/projects')
STATIC_DIR.mkdir(parents=True, exist_ok=True)

IMG_PATTERN = re.compile(r'!\[([^\]]*)\]\((https://carolinafaccin\.wordpress\.com/wp-content/uploads/[^)]+)\)')


def clean_filename(url):
    path = urllib.parse.urlparse(url).path
    name = os.path.basename(path)
    return re.sub(r'[^\w.\-]', '_', name)


def download(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r, open(dest, 'wb') as f:
            f.write(r.read())
        return True
    except Exception as e:
        print(f'    ERROR: {e}')
        return False


total_downloaded = 0
total_failed = 0

for md_file in sorted(PROJECTS_DIR.glob('*/index.md')):
    slug = md_file.parent.name
    content = md_file.read_text(encoding='utf-8')
    matches = IMG_PATTERN.findall(content)

    if not matches:
        continue

    print(f'\n{slug}:')
    post_img_dir = STATIC_DIR / slug
    post_img_dir.mkdir(exist_ok=True)

    new_content = content
    for alt, url in matches:
        # Strip query params for the clean URL to download
        clean_url = url.split('?')[0]
        filename = clean_filename(clean_url)
        dest = post_img_dir / filename
        local_path = f'/img/projects/{slug}/{filename}'

        print(f'  {filename} ... ', end='', flush=True)
        if dest.exists():
            print('already exists')
        elif download(clean_url, dest):
            print('ok')
            total_downloaded += 1
        else:
            total_failed += 1
            continue

        # Replace original URL (with or without query params) with local path
        new_content = new_content.replace(f'![{alt}]({url})', f'![{alt}]({local_path})')

    md_file.write_text(new_content, encoding='utf-8')

print(f'\nDone. Downloaded: {total_downloaded}, Failed: {total_failed}')
print('Images saved to static/img/projects/')
