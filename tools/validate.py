from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json,shutil,subprocess
from tempfile import TemporaryDirectory
D=Path(__file__).resolve().parents[1]/'dist'
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  for k in ['href','src']:
   if k in d:self.links.append(d[k])
pages={};errors=[]
for f in D.rglob('*.html'):
 p=Parse();p.feed(f.read_text());pages[f.resolve()]=p
 if len(p.ids)!=len(set(p.ids)):errors.append(f'Duplicate IDs: {f}')
for f,p in pages.items():
 for url in p.links:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path and not u.fragment:continue
  dest=(D/u.path.lstrip('/') if u.path.startswith('/') else f.parent/u.path).resolve() if u.path else f
  dest=Path(unquote(str(dest)))
  if dest.is_dir():dest=dest/'index.html'
  if not dest.exists():errors.append(f'{f.name}: missing {url}')
  elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'{f.name}: missing anchor {url}')
s=(D/'index.html').read_text();data=json.loads(re.search(r'<script id="report-data" type="application/json">(.*?)</script>',s,re.S)[1])
for key,url in data['photos'].items():
 if not (D/url).exists():errors.append('Missing photo '+url)
for id in re.findall(r'data-id="([^"]+)"',s):
 if '${' in id:continue
 if id not in data['components']:errors.append('Missing component '+id)
node = shutil.which('node')
if not node:
 raise SystemExit('Node.js is required to check the overview JavaScript.')
with TemporaryDirectory() as tmp:
 for i,js in enumerate(re.findall(r'<script>(.*?)</script>',s,re.S)):
  p=Path(tmp)/f'overview-{i}.js'
  p.write_text(js)
  r=subprocess.run([node,'--check',str(p)],capture_output=True,text=True)
  if r.returncode:errors.append(r.stderr)
print('\n'.join(sorted(set(errors))) if errors else f'PASS: {len(pages)} HTML pages, internal links/anchors, photo references, component IDs, and overview JavaScript.')
raise SystemExit(bool(errors))
