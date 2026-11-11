"""Render the reference catalog and load its committed PDF page search records."""
from pathlib import Path
import html
import json
import re

D = Path(__file__).resolve().parents[1] / 'dist'
E = html.escape


def catalog():
    return json.loads((D / 'references/manuals.json').read_text())['manuals']


def render_library():
    manuals = catalog()
    equipment = {}
    for path in sorted((D / 'equipment').glob('*.html')):
        record = json.loads(re.search(r'id="component-record">(.*?)</script>', path.read_text(), re.S)[1])
        equipment[record['id']] = (path, record)
    rows = []
    for key, (path, record) in equipment.items():
        matches = [m for m in manuals if key in m['components']]
        links = ' · '.join(f'<a href="#{m["id"]}">{E(m["title"])}</a>' for m in matches)
        if not matches:
            links = 'Exact manufacturer/model not recorded; no model-specific manual assigned. Photograph the nameplate or markings.'
        rows.append(f'<tr><td><a href="../equipment/{path.name}">{E(record["name"])}</a><br>{E(record["model"])}</td><td>{links}</td></tr>')
        block = '<!--MANUALS--><h2 id="manuals">Manuals and references</h2>'
        if matches:
            block += '<ul>' + ''.join(f'<li><a href="../kb/documents.html#{m["id"]}">{E(m["title"])}</a> — {E(m["applicability"])}</li>' for m in matches) + '</ul>'
        else:
            block += '<p>Model-specific documentation is pending identification. See <a href="../kb/documents.html#coverage">documentation coverage and identification gaps</a>.</p>'
        block += '<!--/MANUALS-->'
        s = path.read_text()
        if '<!--MANUALS-->' in s:
            s = re.sub(r'<!--MANUALS-->.*?<!--/MANUALS-->', lambda _: block, s, flags=re.S)
        else:
            s = s.replace('<script type="application/json" id="component-record">', block + '<script type="application/json" id="component-record">')
        path.write_text(s)
    parts = [f'<h1 id="documents-and-manuals">Documents and manuals</h1><p>{len(manuals)} indexed equipment references, including {sum(bool(m["retrieved"]) for m in manuals)} PDFs downloaded November 11, 2026. Search by model, part, terminal, symptom or fault code using “Search all records.” PDF results open at the matching physical PDF page; the catalog link gives applicability and source context.</p>',
             '<p>Manufacturer specifications describe products; field observations describe this installation. A family or candidate match does not establish replacement compatibility or as-built wiring. Extracted text may miss scanned drawings, symbols or tables; consult the original PDF. PDF page numbers below count from the first PDF page and can differ from printed page numbers.</p>',
             '<p><a href="#coverage">Equipment coverage and identification gaps</a> · <a href="#source-notes">Source and search notes</a></p>']
    page_data = {x['id']: x for x in json.loads((D / 'references/manual-pages.json').read_text())}
    for m in manuals:
        pdf = '../references/' + m['file']
        p = page_data[m['id']]
        components = ' · '.join(f'<a href="../equipment/{equipment[k][0].name}">{E(equipment[k][1]["name"])}</a>' for k in m['components'])
        source = f'<a href="{E(m["source_url"], quote=True)}">Source</a>' if m['source_url'] else 'Source URL not recorded in the original bundle'
        parts.append(f'<h2 id="{m["id"]}">{E(m["title"])}</h2><p class="badge">{E(m["applicability"])}</p><p><a href="{pdf}">Download PDF</a> · {p["page_count"]} pages · {m["bytes"] / 1048576:.2f} MB · {source}</p><dl><dt>Publisher / revision</dt><dd>{E(m["publisher"])} · {E(m["revision"])}</dd><dt>Acquired</dt><dd>{m["retrieved"] or "Previously bundled; acquisition date unknown"}</dd><dt>Equipment</dt><dd>{components}</dd></dl><p><strong>Applicability:</strong> {E(m["qualification"])}</p><p>{E(m["summary"])}</p>')
        if m['topics']:
            parts.append('<ul>' + ''.join(f'<li><a href="{pdf}#page={t["page"]}">PDF p. {t["page"]}: {E(t["title"])}</a></li>' for t in m['topics']) + '</ul>')
        if m.get('index_pages'):
            parts.append('<p>Search indexes selected relevant PDF pages: ' + ', '.join(map(str, m['index_pages'])) + '. The full catalog remains available above.</p>')
        if p['sparse_pages']:
            parts.append('<p>Pages with little extractable text (drawings, blank or scanned pages): ' + ', '.join(map(str, p['sparse_pages'])) + '. Open the PDF to inspect them.</p>')
        parts.append(f'<p><small>Search terms: {E(m["keywords"])}</small></p>')
    parts.append('<h2 id="coverage">Equipment coverage and identification gaps</h2><p>This table covers every equipment record in the system. Unidentified air eliminator, expansion tanks, gauge, manifold, transformer and room thermostats require markings before an exact manual can be selected. General system references are labelled accordingly. The lower-right external relay remains unidentified.</p><table><thead><tr><th>Equipment / recorded identity</th><th>References or next identification step</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>')
    parts.append('<h2 id="source-notes">Source and search notes</h2><p>Original PDFs are preserved locally. Manufacturer-hosted copies were preferred; legacy manufacturer documents were obtained from public mirrors when needed. The BuyTaco table is labelled as a distributor reference. Revision and applicability are recorded above. The machine-readable <a href="../references/manuals.json">catalog</a> records source/download URLs, acquisition dates and SHA-256 checksums. <a href="../references/manual-pages.json">Page text</a> supports local search; no network service is needed after the site loads. Search does not OCR images and does not replace reading diagrams.</p><p>Later-generation Polaris Series 200/201 instructions, European Caleffi data and duplicate downloads were excluded. Exact legacy A303XX0003 module documentation was not located; the later A3031003 guide is explicitly qualified. Nest hardware generation and unrecorded component identities remain open.</p><h2 id="original-bundle">Other preserved bundle references</h2><p>These retain their historical context; see <a href="09-reference-sources.html">source notes</a>.</p><ul><li><a href="../references/Info-on-water-heaters.txt">Water-heater source notes (TXT)</a></li><li><a href="../references/pasted.txt">Radiant and contractor notes (TXT)</a></li><li><a href="../archive/Englewood_Rd_Heating_System_Master_Reference_v0.1.docx">Historical master reference (DOCX)</a></li><li><a href="../archive/Englewood_Rd_Heating_System_Master_Reference_v0.1.pdf">Historical master reference (PDF)</a></li></ul>')
    path = D / 'kb/documents.html'
    s = path.read_text()
    s = re.sub(r'<article>.*?</article>', lambda _: '<article>' + ''.join(parts) + '</article>', s, flags=re.S)
    s = re.sub(r'<footer>.*?</footer>', '<footer>Reference library · Updated November 11, 2026 · <a href="maintenance.html">Evidence and maintenance</a></footer>', s, flags=re.S)
    path.write_text(s)


def search_records():
    by_id = {m['id']: m for m in catalog()}
    entries = []
    for doc in json.loads((D / 'references/manual-pages.json').read_text()):
        m = by_id[doc['id']]
        for page in doc['pages']:
            if not page['text'] or m.get('index_pages') and page['number'] not in m['index_pages']:
                continue
            entries.append(dict(title=f'{m["title"]} · PDF p. {page["number"]}', url=f'references/{m["file"]}#page={page["number"]}', text=page['text'], kind='pdf', context_url='kb/documents.html#' + m['id']))
    return entries
