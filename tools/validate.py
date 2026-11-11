from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json,shutil,subprocess
from tempfile import TemporaryDirectory
from manuals import catalog
import hashlib
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
manual_pages=json.loads((D/'references/manual-pages.json').read_text())
manual_text={m['id']:m for m in manual_pages}
manuals=catalog()
if len(manual_text)!=len(manual_pages) or len({m['id'] for m in manuals})!=len(manuals):errors.append('Duplicate manual IDs')
if set(manual_text)!={m['id'] for m in manuals}:errors.append('Manual catalog/page index IDs differ')
for m in manuals:
 p=D/'references'/m['file'];text=manual_text.get(m['id'],{})
 if not p.exists() or not p.read_bytes().startswith(b'%PDF'):errors.append('Missing/invalid PDF '+str(p));continue
 if hashlib.sha256(p.read_bytes()).hexdigest()!=m['sha256'] or p.stat().st_size!=m['bytes']:errors.append('PDF checksum/size mismatch '+str(p))
 if text.get('sha256')!=m['sha256']:errors.append('Stale PDF page extraction '+m['id'])
 count=text.get('page_count',0)
 if [x['number'] for x in text.get('pages',[])]!=list(range(1,count+1)):errors.append('Invalid PDF page sequence '+m['id'])
 for n in [t['page'] for t in m['topics']]+m.get('index_pages',[]):
  if not 1<=n<=count:errors.append('Invalid PDF page reference '+m['id'])
 for id in m['components']:
  if id not in data['components']:errors.append('Unknown manual equipment '+id)
node = shutil.which('node')
if not node:
 raise SystemExit('Node.js is required to check the overview JavaScript.')
with TemporaryDirectory() as tmp:
 for i,js in enumerate(re.findall(r'<script>(.*?)</script>',s,re.S)):
  p=Path(tmp)/f'overview-{i}.js'
  p.write_text(js)
  r=subprocess.run([node,'--check',str(p)],capture_output=True,text=True)
  if r.returncode:errors.append(r.stderr)
r=subprocess.run([node,'--check',str(D/'assets/kb.js')],capture_output=True,text=True)
if r.returncode:errors.append(r.stderr)
print('\n'.join(sorted(set(errors))) if errors else f'PASS: {len(pages)} HTML pages, links/anchors, photos, component IDs, {len(manuals)} PDF checksums/page indexes, and site JavaScript.')
raise SystemExit(bool(errors))
