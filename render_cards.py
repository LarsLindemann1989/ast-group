from html import escape as e

def link(url,text,cls="text-link"):
    ext=' target="_blank" rel="noopener noreferrer"' if url.startswith("http") else ""
    return f'<a class="{cls}" href="{e(url,quote=True)}"{ext}>{text}</a>'

def person(p,compact=False):
    photo=f'<img src="{e(p["image"])}" alt="{e(p["name"])}" loading="lazy" width="400" height="460">' if p.get('image') else f'<span class="initials" aria-label="Portrait unavailable">{e("".join(x[0] for x in p["name"].split()[:2]))}</span>'
    role='Principal investigator' if p['role']=='PI' else p['role']
    if compact:role='Principal investigator' if p['role']=='PI' else 'Postdoctoral researcher' if p['group']=='Postdoctoral researchers' else 'Industrial PhD student' if 'Industrial' in role else 'PhD student'
    return f'<article class="person">{link(p["url"],photo,"portrait")}<h3>{link(p["url"],e(p["name"]),"")}</h3><p class="role">{e(role)}</p>'+('' if compact else f'<p class="interests">{e(p["interests"])}</p>')+'</article>'

def venue(p):
    s=p['venue']
    if p.get('volume'):s+=' '+p['volume']+(('('+p['issue']+')') if p.get('issue') else '')
    if p.get('pages'):s+=', '+p['pages']
    return e(s)

def paper(p,with_year=False):
    authors=e(p['authors']).replace('Lars Lindemann','<strong>Lars Lindemann</strong>')
    links=''.join(link(url,e(label)+' →','paper-link') for label,url in p.get('links',{}).items())
    search=e((p['title']+' '+p['authors']+' '+p['venue']+' '+p['year']).casefold(),quote=True)
    return f'<article class="paper" id="{e(p["id"])}" data-type="{e(p["type"])}" data-year="{p["year"]}" data-search="{search}">'+(f'<span class="paper-year">{p["year"]}</span>' if with_year else '')+f'<div class="paper-content"><h3>{link(p["url"],e(p["title"]),"")}</h3><p class="authors">{authors}</p><p class="venue">{venue(p)}</p><div class="paper-links">{links}</div></div></article>'

def research_image(r,card=False):
    if not r.get('image'):return ''
    image=f'<img src="{e(r["image"])}" alt="{e(r.get("image_alt",r["title"]),quote=True)}" loading="lazy">'
    credit=link(r['image_source'],e(r.get('image_credit','Source figure')),'') if r.get('image_source') else e(r.get('image_credit',''))
    return ('<a class="research-image" href="research.html#'+e(r['id'])+'">'+image+'</a>' if card else '<figure class="research-figure">'+image+('<figcaption>'+credit+'</figcaption>' if credit else '')+'</figure>')

