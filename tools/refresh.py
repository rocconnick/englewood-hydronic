"""Refresh navigation/search from maintained HTML. No Markdown input."""
from pathlib import Path
from html.parser import HTMLParser
import html,json,re
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist';E=html.escape
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
def plain(s):
 p=Text();p.feed(s);return ' '.join(' '.join(p.out).split())
def slug(t):return re.sub(r'[^\w\- ]','',plain(t).lower()).replace(' ','-')
files=sorted(list((D/'kb').glob('*.html'))+list((D/'equipment').glob('*.html'))); pages=[];search=[]
for f in files:
 s=f.read_text();body=re.search(r'<article>(.*?)</article>',s,re.S).group(1)
 # Fill IDs on newer hand-edited headings, preserving old anchors.
 body=re.sub(r'<h([1-6])>(.*?)</h\1>',lambda m:f'<h{m[1]} id="{slug(m[2])}">{m[2]}</h{m[1]}>',body,flags=re.S)
 s=re.sub(r'<article>.*?</article>',lambda m:'<article>'+body+'</article>',s,flags=re.S);f.write_text(s)
 title=plain(re.search(r'<h1[^>]*>(.*?)</h1>',body,re.S).group(1));url=f.relative_to(D).as_posix();group=re.search(r'name="kb-group" content="([^"]+)"',s).group(1)
 headings=[(m[1],plain(m[2])) for m in re.finditer(r'<h[23] id="([^"]+)">(.*?)</h[23]>',body,re.S)]
 pages.append(dict(path=f,title=title,url=url,group=group,headings=headings))
 search.append(dict(title=title,url=url,text=plain(body)))
 parts=re.split(r'(<h[23] id="[^"]+">.*?</h[23]>)',body,flags=re.S)
 for i in range(1,len(parts),2):
  m=re.search(r'id="([^"]+)">(.*?)</h',parts[i],re.S);search.append(dict(title=title+' › '+plain(m[2]),url=url+'#'+m[1],text=plain(parts[i+1])))
for p in pages:
 nav='<a href="../index.html">← Interactive system guide</a><h2 style="font-size:19px;margin-top:20px">Knowledge base</h2><label for="kb-search">Search all records</label><input id="kb-search" type="search" placeholder="Part, zone, terminal…"><div id="results" aria-live="polite"></div><nav aria-label="Knowledge base index">'
 for group in ['Start here','Equipment','Field records','Reference','History']:
  sub=[x for x in pages if x['group']==group];nav+=f'<details {"open" if group==p["group"] or group=="Start here" else ""}><summary>{group}</summary><ul>'
  for x in sub:
   nav+=f'<li><a href="../{x["url"]}"'+(' aria-current="page"' if x==p else '')+f'>{E(x["title"])}</a>'
   if x['headings']:
    nav+='<details '+('open' if x==p else '')+'><summary style="font-size:12px;margin-left:8px">Sections</summary><ul class="section-links">'+''.join(f'<li><a href="../{x["url"]}#{id}">{E(t)}</a></li>' for id,t in x['headings'])+'</ul></details>'
   nav+='</li>'
  nav+='</ul></details>'
 nav+='</nav>'
 s=p['path'].read_text();s=re.sub(r'<!--NAV-->.*?<!--/NAV-->','<!--NAV-->'+nav+'<!--/NAV-->',s,flags=re.S);p['path'].write_text(s)
(D/'assets/search.json').write_text(json.dumps(search,ensure_ascii=False))
# Single equipment metadata source lives in equipment HTML pages.
f=D/'index.html';s=f.read_text();m=re.search(r'(<script id="report-data" type="application/json">)(.*?)(</script>)',s,re.S);data=json.loads(m[2]);data['components']={}
for p in sorted((D/'equipment').glob('*.html')):
 c=json.loads(re.search(r'<script type="application/json" id="component-record">(.*?)</script>',p.read_text(),re.S)[1]);data['components'][c['id']]=c
s=s[:m.start(2)]+json.dumps(data).replace('</','<\\/')+s[m.end(2):];f.write_text(s)
print(f'Refreshed {len(pages)} HTML pages and {len(search)} searchable sections.')
