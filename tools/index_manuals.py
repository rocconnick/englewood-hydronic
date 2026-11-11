"""Extract PDF search text after adding/replacing a catalog PDF. Requires pdftotext.

Normal refresh/deployment uses this committed output and requires only Python/Node.
Run: python3 tools/index_manuals.py; python3 tools/refresh.py
"""
import hashlib
import json
import re
import shutil
import subprocess
from manuals import D, catalog

if not shutil.which('pdftotext'):
    raise SystemExit('Install Poppler (pdftotext) to extract new manuals.')
documents = []
for m in catalog():
    path = D / 'references' / m['file']
    data = path.read_bytes()
    if not data.startswith(b'%PDF') or hashlib.sha256(data).hexdigest() != m['sha256']:
        raise SystemExit(f'PDF signature/checksum mismatch: {path}')
    result = subprocess.run(['pdftotext', '-layout', str(path), '-'], capture_output=True, check=True)
    raw = result.stdout.decode('utf-8').split('\f')
    if not raw[-1].strip():
        raw.pop()
    pages = [dict(number=i, text=' '.join(re.sub(r'[\x00-\x08\x0b\x0e-\x1f]', ' ', p).split())) for i, p in enumerate(raw, 1)]
    documents.append(dict(id=m['id'], sha256=m['sha256'], page_count=len(pages), sparse_pages=[p['number'] for p in pages if len(p['text']) < 80], pages=pages))
    print(f'{m["id"]}: {len(pages)} pages')
(D / 'references/manual-pages.json').write_text(json.dumps(documents, ensure_ascii=False, separators=(',', ':')) + '\n')
