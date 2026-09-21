#!/usr/bin/env python3
"""Convert WordPress WXR export to Hugo markdown files."""

import xml.etree.ElementTree as ET
import os
import re
import sys
from datetime import datetime
import html2text

NS = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
}


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return re.sub(r'^-+|-+$', '', text)


def to_markdown(html):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    return h.handle(html)


def convert(xml_file, output_dir):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    channel = root.find('channel')

    count = 0
    for item in channel.findall('item'):
        post_type = item.find('wp:post_type', NS)
        status = item.find('wp:status', NS)

        if post_type is None or status is None:
            continue
        if post_type.text not in ('post', 'page'):
            continue
        if status.text != 'publish':
            continue

        title_el = item.find('title')
        title = title_el.text if title_el is not None and title_el.text else 'Untitled'

        slug_el = item.find('wp:post_name', NS)
        slug = slug_el.text if slug_el is not None and slug_el.text else slugify(title)

        date_el = item.find('wp:post_date', NS)
        date_str = ''
        if date_el is not None and date_el.text:
            try:
                d = datetime.strptime(date_el.text, '%Y-%m-%d %H:%M:%S')
                date_str = d.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            except ValueError:
                pass

        content_html = item.find('content:encoded', NS)
        content = to_markdown(content_html.text) if content_html is not None and content_html.text else ''

        categories, tags = [], []
        for cat in item.findall('category'):
            domain = cat.get('domain', '')
            text = cat.text or ''
            if domain == 'category':
                categories.append(text)
            elif domain == 'post_tag':
                tags.append(text)

        # Build YAML frontmatter
        fm = ['---']
        fm.append(f'title: "{title.replace(chr(34), chr(39))}"')
        if date_str:
            fm.append(f'date: {date_str}')
        if categories:
            fm.append('categories:')
            fm.extend(f'  - "{c}"' for c in categories)
        if tags:
            fm.append('tags:')
            fm.extend(f'  - "{t}"' for t in tags)
        fm.append('draft: false')
        fm.append('---\n')

        post_dir = os.path.join(output_dir, slug)
        os.makedirs(post_dir, exist_ok=True)

        with open(os.path.join(post_dir, 'index.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(fm) + '\n')
            f.write(content)

        print(f'  ✓ {slug}')
        count += 1

    return count


if __name__ == '__main__':
    xml_file = sys.argv[1] if len(sys.argv) > 1 else 'carolinafaccin.WordPress.2026-05-10.xml'
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'content/en/posts'

    print(f'Converting {xml_file}...\n')
    n = convert(xml_file, output_dir)
    print(f'\nDone! {n} items created in {output_dir}/')
    print('\nNext: review the files, then move PT-BR posts to content/pt-br/posts/')
