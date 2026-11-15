"""Catch broken local links/images and structural errors before publishing."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parent / 'dist'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.errors, self.h1 = path, [], [], [], 0
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1 += 1
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        for key in ['href', 'src']:
            if attrs.get(key):
                self.refs.append(attrs[key])
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('An image needs descriptive alt text.')

pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
errors = []
if not (ROOT / 'index.html').exists():
    errors.append('No homepage was generated.')
for path, page in pages.items():
    prefix = path.name + ': '
    errors.extend(prefix + message for message in page.errors)
    if page.h1 != 1:
        errors.append(prefix + f'Expected one main heading, found {page.h1}. Use ## or ### in page text.')
    errors.extend(prefix + f'Duplicate anchor: {key}' for key,n in Counter(page.ids).items() if n > 1)
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith('/'):
            errors.append(prefix + f'Use a relative link so GitHub project paths work: {ref}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_relative_to(ROOT.resolve()) or not target.exists():
            errors.append(prefix + f'Missing local file: {ref}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(prefix + f'Missing section: {ref}')
if errors:
    print('\n'.join(errors),file=sys.stderr)
    sys.exit(1)
print(f'Checked {len(pages)} pages: local links, images, anchors, and page headings passed.')
