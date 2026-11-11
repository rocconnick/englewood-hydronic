# Englewood Road Hydronic Heating System

This repository maintains the interactive system guide and HTML knowledge base for the installed heating and domestic hot water system. Browse the [live guide](https://rocconnick.github.io/englewood-hydronic/) or the [knowledge base](https://rocconnick.github.io/englewood-hydronic/kb/).

| Path | Purpose |
| --- | --- |
| [dist/index.html](dist/index.html) | Interactive plumbing and controls guide |
| [dist/kb/](dist/kb/) | System notes, wiring, diagnostics, and reference index |
| [dist/equipment/](dist/equipment/) | Equipment records and metadata used by the overview |
| [dist/assets/](dist/assets/) | Published photos, styles, scripts, and search index |
| [dist/references/](dist/references/) and [dist/archive/](dist/archive/) | Downloadable manuals, source notes, and historical reference documents |
| [evidence/](evidence/) | Original photos, historical manifest, Markdown snapshot, and migration map |
| [tools/](tools/) | Refresh and validation scripts |

To preview locally, run `python3 -m http.server 8000 --directory dist` from the repository root and open [localhost:8000](http://localhost:8000/). Serve the site over HTTP so the knowledge base can load its search index. Site links are relative so the same files also work under the GitHub Pages repository path.

Edit the HTML directly. With Python 3 and Node.js on your PATH, run:

```sh
python3 tools/refresh.py
python3 tools/validate.py
```

The refresh script updates the navigation, search index, and overview equipment data. Commit the edited HTML and any generated changes together. Pushes to `main` trigger the GitHub Pages workflow when they change `dist/`, `tools/`, or the Pages workflow itself. You can also run it manually from the Actions tab. In repository Settings → Pages, select GitHub Actions as the publishing source.

The evidence manifest and migration map use the original paths as historical identifiers. The Markdown snapshot is reference material. The retired standalone report and its builders remain available in Git history at `1eb0741`.

The manual library lives in `dist/references/manuals.json`. It records each PDF's
publisher, actual cover revision, applicability, equipment links, source URLs,
retrieval date, checksum, keywords and useful physical PDF page numbers.
`tools/refresh.py` renders the catalog and equipment reference links from it.

After adding or replacing a PDF, update its catalog record, then run
`python3 tools/index_manuals.py` (requires Poppler's `pdftotext`) before the normal
refresh/validate commands. Commit `dist/references/manual-pages.json` with the
PDFs. Normal refresh and deployment read that committed text without needing
Poppler or network access. Search indexes individual PDF pages and links to
`#page=N`; the full White-Rodgers catalog is preserved while only its relevant
relay page is indexed. Text extraction does not OCR scanned drawings.
