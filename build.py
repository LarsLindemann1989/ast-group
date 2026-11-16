"""Build the AST Group website. Edit content/*.md and data/*, not this file."""
import json
import os
import re
import shutil
from datetime import date
from html import escape as e
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml
from render_cards import link, paper, person, research_image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'


def read_yaml(path):
    try:
        return yaml.safe_load((ROOT / path).read_text(encoding='utf-8'))
    except yaml.YAMLError as exc:
        raise ValueError(f'{path}: check the indentation and quoted values. {exc}') from exc


def read_md(path):
    path = Path(path)
    text = path.read_text(encoding='utf-8')
    parts = re.split(r'^---\s*$', text, maxsplit=2, flags=re.M)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'{path}: start with settings between two lines containing ---')
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f'{path}: check the settings above the second --- line. {exc}') from exc
    if not isinstance(meta, dict):
        raise ValueError(f'{path}: settings must be named fields, e.g. title: My title')
    if not meta.get('title'):
        raise ValueError(f'{path}: add a title.')
    meta['html'] = markdown.markdown(parts[2].strip(), extensions=['extra', 'sane_lists'])
    meta['source'] = path.relative_to(ROOT).as_posix()
    return meta


def heading(text):
    return e(str(text).strip()).replace('\n', ' <br>')


def intro(kicker, content):
    description = content.get('description', '')
    return (f'<section class="page-intro wrap"><p class="eyebrow">{e(kicker)}</p>'
            f'<h1>{heading(content["title"])}</h1>'
            + (f'<p class="lead">{e(description)}</p>' if description else '') + '</section>')


D = read_yaml('site.yaml')
PEOPLE = read_yaml('data/people.yaml') or []
ALUMNI = read_yaml('data/alumni.yaml') or []
COURSES = read_yaml('data/courses.yaml') or []
C = {p.stem: read_md(p) for p in (ROOT / 'content').glob('*.md')}
RESEARCH = sorted((read_md(p) for p in (ROOT / 'content/research').glob('*.md')),
                  key=lambda r: (r.get('order', 100), r['title']))
NEWS = sorted((read_md(p) for p in (ROOT / 'content/news').glob('*.md')),
              key=lambda n: str(n['date']), reverse=True)
P = json.loads((ROOT / 'data/publications.json').read_text(encoding='utf-8'))
for p in P:
    p['year'] = str(p['year'])
P.sort(key=lambda p: (-int(p['year']), p['title'].casefold()))
BY_ID = {p['id']: p for p in P}
if len(BY_ID) != len(P):
    raise ValueError('data/publications.json: publication IDs must be unique.')
if len({r.get('id') for r in RESEARCH}) != len(RESEARCH):
    raise ValueError('content/research/: every research area needs a different id.')
for r in RESEARCH:
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r.get('id', '')):
        raise ValueError(f'{r["source"]}: use a lowercase id with hyphens, e.g. safe-learning.')
    if not r.get('summary'):
        raise ValueError(f'{r["source"]}: add a summary for the homepage card.')
    if not isinstance(r.get('order', 100), (int, float)):
        raise ValueError(f'{r["source"]}: order must be a number.')
    for field in ['papers', 'tags']:
        if not isinstance(r.get(field, []), list):
            raise ValueError(f'{r["source"]}: {field} must be a list, or [].')
    for pid in r.get('papers', []):
        if pid not in BY_ID:
            raise ValueError(f'{r["source"]}: paper id {pid!r} is not in data/publications.json.')
for pid in C['home'].get('selected_publications', []):
    if pid not in BY_ID:
        raise ValueError(f'content/home.md: selected publication {pid!r} does not exist.')

# Regenerate output from source; removed content/images cannot remain in the build.
if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(ROOT / 'static', OUT)
repo = os.environ.get('GITHUB_REPOSITORY', '')
branch = os.environ.get('SITE_EDIT_BRANCH', 'main')


def edit_link(source):
    if not repo:
        return ''
    action = 'tree' if source.endswith('/') else 'edit'
    url = f'https://github.com/{repo}/{action}/{quote(branch, safe="")}/{source}'
    return link(url, 'Edit this page', '')


def page(file, title, body, active='', source='content/home.md'):
    nav = ''.join(f'<a href="{p}"' + (' aria-current="page"' if active == n else '')
                  + f'>{n}</a>' for n, p in [('Research', 'research.html'), ('People', 'people.html'),
                    ('Publications', 'publications.html'), ('Teaching', 'teaching.html'), ('Contact', 'contact.html')])
    address = '<br>'.join(e(line) for line in D['address'])
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#ffffff"><meta name="description" content="{e(D['description'],quote=True)}"><title>{e(title)} · AST Group · ETH Zürich</title><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="hero-video.css"><script src="site.js" defer></script><script src="hero-video.js" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a><div class="institution"><div class="wrap institution-inner"><a class="eth" href="https://ethz.ch/en.html" aria-label="ETH Zürich homepage"><img src="assets/eth-zurich.svg" alt="ETH Zürich" width="180" height="30"></a>{link(D['institution_url'],e(D['institution']),'institution-name')}</div></div>
<header class="header"><div class="wrap nav-row"><a class="brand" href="index.html">{e(D['short_name'])}</a><button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="nav">Menu <span aria-hidden="true">＋</span></button><nav id="nav" aria-label="Main navigation">{nav}</nav></div></header><main id="main">{body}</main>
<footer><div class="wrap footer-top"><div><strong>{e(D['name'])}</strong><p>{e(D['institution'])} · ETH Zürich<br>{address}</p></div><div>{link('mailto:'+D['email'],e(D['email']))}<p>{link(D['scholar'],'Google Scholar')}&nbsp; · &nbsp;{link('contact.html','Contact')}</p></div></div><div class="wrap footer-bottom"><span>© {date.today().year} AST Group</span><div>{link('imprint.html','Imprint')}{link('privacy.html','Privacy')}{edit_link(source)}</div></div></footer></body></html>'''
    (OUT / file).write_text(html, encoding='utf-8')


def research_cards():
    return '<div class="research-grid">' + ''.join(
        f'<article class="research-tile" data-research-id="{e(r["id"])}">{research_image(r,True)}'
        f'<h3>{link("research.html#"+r["id"],e(r["title"]),"")}</h3><p>{e(r["summary"])}</p>'
        + link('research.html#'+r['id'], 'Explore this area →', 'more-link') + '</article>' for r in RESEARCH) + '</div>'


news_html = ''
for n in NEWS:
    day = date.fromisoformat(str(n['date']))
    news_html += f'<article class="news-item"><time datetime="{day.isoformat()}">{day.strftime("%d %B %Y")}</time><h3>'
    news_html += (link(n['url'], e(n['title']), '') if n.get('url') else e(n['title'])) + '</h3>' + n['html'] + '</article>'
limit = int(C['home'].get('featured_people', 6))
if limit < 0:
    raise ValueError('content/home.md: featured_people must be zero or a positive integer.')
video_path = C['home'].get('hero_video')
poster_path = C['home'].get('hero_poster')
video_description = C['home'].get('hero_video_description', 'Research demonstration')
hero_media = (
    '<div class="hero-media">'
    + (f'<img class="hero-video-poster" src="{e(poster_path, quote=True)}" alt="{e(video_description, quote=True)}" aria-hidden="true">' if poster_path else '')
    + f'<video class="hero-video" autoplay muted loop playsinline preload="auto" aria-label="{e(video_description, quote=True)}"'
    + (f' poster="{e(poster_path, quote=True)}"' if poster_path else '')
    + f'><source src="{e(video_path, quote=True)}" type="video/mp4">Your browser does not support HTML5 video.</video>'
    + '<button type="button" class="hero-video-toggle" aria-label="Pause video">Pause video</button>'
    + '</div>'
) if video_path else ''
hero_class = 'hero has-media' if hero_media else 'hero'
home_hero = (
    f'<section class="wrap {hero_class}"><div class="hero-copy">'
    f'<p class="affiliation">{e(D["institution"])} · ETH Zürich</p>'
    f'<h1>{heading(C["home"]["title"])}</h1>'
    f'<div class="intro-text markdown">{C["home"]["html"]}</div>'
    f'<div class="actions">{link("people.html", "Meet our team →")}{link("contact.html", "Work with us →")}</div>'
    f'</div>{hero_media}</section>'
)
home = home_hero + f'''<section class="wrap section home-research" id="research"><div class="section-heading inline"><h2>Research</h2>{link('research.html','Explore our research →','more-link')}</div>{research_cards()}</section><div class="soft-band" id="about"><div class="wrap two-column"><section><p class="eyebrow">About the group</p><h2>{heading(C['about']['title'])}</h2><div class="markdown">{C['about']['html']}</div>{link('lars-lindemann.html','About Lars Lindemann →','more-link')}</section><section><p class="eyebrow">Latest news</p>{news_html}</section></div></div><section class="wrap section"><div class="section-heading inline"><h2>People</h2>{link('people.html','All researchers & collaborators →','more-link')}</div><div class="people-grid home-people">{''.join(person(p,True) for p in PEOPLE[:limit])}</div></section><section class="wrap section selected-publications"><div class="section-heading inline"><h2>Selected publications</h2>{link('publications.html','Browse the publication archive →','more-link')}</div>{''.join(paper(BY_ID[pid],True) for pid in C['home'].get('selected_publications',[]))}</section>'''
page('index.html', D['name'], home)

body = intro('Research', C['research'])
if C['research']['html']:
    body += '<div class="wrap prose">' + C['research']['html'] + '</div>'
body += '<nav class="wrap research-index" aria-label="Research areas">' + ''.join(f'<a href="#{e(r["id"])}"><span>{i:02}</span>{e(r["title"])}<span aria-hidden="true">↓</span></a>' for i,r in enumerate(RESEARCH,1)) + '</nav>'
for i,r in enumerate(RESEARCH,1):
    body += f'<section class="wrap research-detail" id="{e(r["id"])}" data-research-id="{e(r["id"])}"><div class="research-detail-heading"><span class="area-number">{i:02}</span><h2>{e(r["title"])}</h2></div><div class="research-layout' + (' reverse' if i%2==0 else '') + '"><div class="research-description"><p class="lead">' + e(r['summary']) + '</p><div class="markdown research-markdown">' + r['html'] + '</div><div class="tags">' + ''.join('<span>'+e(t)+'</span>' for t in r.get('tags',[])) + '</div></div>' + research_image(r) + '</div>'
    if r.get('papers'):
        body += '<div class="representative-papers"><h3>Representative papers</h3><ul>' + ''.join('<li>' + link(BY_ID[pid]['url'], e(BY_ID[pid]['title']), '') + '<span>' + e(BY_ID[pid]['venue']) + ' · ' + BY_ID[pid]['year'] + '</span></li>' for pid in r['papers']) + '</ul></div>'
    body += '</section>'
body += '<section class="wrap closing"><h2>Explore the work behind these ideas.</h2>' + link('publications.html','Browse all publications →') + '</section>'
page('research.html','Research',body,'Research','content/research/')

body = intro('People',C['people'])
groups = list(dict.fromkeys(p['group'] for p in PEOPLE))
for group in groups:
    body += f'<section class="wrap people-section"><h2 class="group-title">{e(group)}</h2><div class="people-grid">' + ''.join(person(p) for p in PEOPLE if p['group']==group) + '</div></section>'
body += '<section class="wrap alumni"><h2 class="group-title">Alumni</h2><ul>' + ''.join('<li>'+e(p)+'</li>' for p in ALUMNI) + '</ul></section>'
page('people.html','People',body,'People','data/people.yaml')

years = sorted({p['year'] for p in P},reverse=True)
body = intro('Publications',C['publications'])
body += '<section class="wrap publications-section"><div class="publication-tools"><label class="search"><span>Search publications</span><input type="search" id="publication-search" placeholder="Title, author, venue, or year…"></label><label class="type-select"><span>Publication type</span><select id="publication-type"><option value="all">All types</option><option value="journal">Journal articles</option><option value="conference">Conference & workshop papers</option><option value="preprint">Preprints</option><option value="thesis">Thesis</option></select></label><button class="reset-filters" id="reset-filters">Reset</button></div><div class="archive-topline"><p id="result-count" aria-live="polite">' + str(len(P)) + ' records</p><div>' + link(D['scholar'],'Google Scholar →') + link('publications.bib','Download BibTeX ↓') + '</div></div><div class="publication-layout"><nav class="year-nav" aria-label="Publication years">' + ''.join(f'<a href="#year-{y}" data-year-link="{y}">{y}</a>' for y in years) + '</nav><div id="papers">'
for y in years:
    body += f'<section class="publication-year" id="year-{y}" data-year-group="{y}"><h2>{y}<span>{sum(p["year"]==y for p in P)}</span></h2>' + ''.join(paper(p) for p in P if p['year']==y) + '</section>'
body += '</div></div><p id="no-results" hidden>No matching publications. Try another title, author, or year.</p><aside class="source-note"><strong>About this archive</strong>' + C['publications']['html'] + '</aside></section>'
page('publications.html','Publications',body,'Publications','data/publications.json')
bib = []
for p in P:
    kind = {'journal':'article','conference':'inproceedings','preprint':'misc','thesis':'phdthesis'}[p['type']]
    fields = {'title':p['title'],'author':p['authors'].replace(', ',' and '),'year':p['year'],'url':p['url']}
    fields['journal' if kind=='article' else 'booktitle' if kind=='inproceedings' else 'note'] = p['venue']
    if p.get('arxiv'):
        fields.update(eprint=p['arxiv'],archivePrefix='arXiv')
    for field in ['volume','pages','issue']:
        if p.get(field):
            fields['number' if field=='issue' else field] = str(p[field])
    bib.append('@' + kind + '{' + p['id'] + ',\n' + ',\n'.join('  '+k+' = {'+v.replace('&',r'\&')+'}' for k,v in fields.items()) + '\n}')
(OUT/'publications.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf-8')

c = C['teaching']
body = intro('Teaching & student projects',c)
body += '<section class="wrap student-callout"><div><p class="eyebrow">Student projects</p><h2>' + heading(c['callout_title']) + '</h2><div class="markdown">' + c['html'] + '</div></div>' + link(c['callout_link'],e(c['callout_label']),'button primary') + '</section><section class="wrap teaching-list"><h2 class="group-title">Teaching archive</h2><p class="muted">' + e(c['archive_note']) + '</p>'
body += ''.join(f'<article class="course"><p class="eyebrow">{e(item["term"])}</p><div><h3>{e(item["title"])}</h3><p>{e(item["details"])}</p></div></article>' for item in COURSES)
body += '<div class="closing">' + link(c['supervision_url'],'Previous thesis supervision record →') + '</div></section>'
page('teaching.html','Teaching',body,'Teaching','content/teaching.md')

c = C['lars-lindemann']
body = intro('Principal investigator',c)
body += '<section class="wrap bio-layout"><aside><img class="bio-portrait" src="' + e(c['image'],quote=True) + '" alt="' + e(c['title'],quote=True) + '" width="400" height="460"><div class="bio-links">' + link('mailto:'+D['email'],'Email Lars →') + link(D['scholar'],'Google Scholar →') + link(c['profile_url'],'ETH profile →') + '</div></aside><div class="prose">' + c['html'] + '</div></section>'
page('lars-lindemann.html',c['title'],body,'People','content/lars-lindemann.md')

c = C['contact']
body = intro('Contact & opportunities',c)
body += '<section class="wrap contact-grid"><div class="contact-card"><p class="eyebrow">Research & collaboration</p><div class="markdown">' + c['html'] + '</div>' + link('mailto:'+D['email'],e(D['email'])+' →','contact-email') + '</div><div class="address-card"><div class="map-mark" aria-hidden="true">Zürich<span>47.38° N / 8.55° E</span></div><p class="eyebrow">Visit us</p><h2>ETH Zürich</h2><address>' + '<br>'.join(e(s) for s in [D['institution'],D['name'],*D['address']]) + '</address>' + link(c['map_url'],'Open map →') + '</div></section>'
page('contact.html','Contact & opportunities',body,'Contact','content/contact.md')
for key in ['imprint','privacy']:
    c = C[key]
    page(key+'.html',c['title'],intro('Site information',c)+'<section class="wrap prose legal">'+c['html']+'</section>',source=c['source'])

print(f'Built 9 pages, {len(P)} publication records, and {len(RESEARCH)} research areas.')
