# Englewood Road Hydronic Heating System

This repository maintains the interactive system guide and HTML knowledge base for the installed heating and domestic hot water system. Browse the [live guide](https://englewood-road-hydronic-guide.ornateshrew4.chatgpt.site/) or the [knowledge base](https://englewood-road-hydronic-guide.ornateshrew4.chatgpt.site/kb/).

| Path | Purpose |
| --- | --- |
| [dist/index.html](dist/index.html) | Interactive plumbing and controls guide |
| [dist/kb/](dist/kb/) | System notes, wiring, diagnostics, and reference index |
| [dist/equipment/](dist/equipment/) | Equipment records and metadata used by the overview |
| [dist/assets/](dist/assets/) | Published photos, styles, scripts, and search index |
| [dist/references/](dist/references/) and [dist/archive/](dist/archive/) | Downloadable manuals, source notes, and historical reference documents |
| [evidence/](evidence/) | Original photos, historical manifest, Markdown snapshot, and migration map |
| [tools/](tools/) | Refresh and validation scripts |
| [.openai/hosting.json](.openai/hosting.json) | Hosting configuration. The publish directory is `dist/`. |

To preview locally, run `python3 -m http.server 8000 --directory dist` from the repository root and open [localhost:8000](http://localhost:8000/). The site uses root-relative URLs, so serve it over HTTP.

Edit the HTML directly. With Python 3 and Node.js on your PATH, run:

```sh
python3 tools/refresh.py
python3 tools/validate.py
```

The refresh script updates the navigation, search index, and overview equipment data. Commit the edited HTML and any generated changes together. Publish `dist/` through the configured Sites project when a deployment is requested.

The evidence manifest and migration map use the original paths as historical identifiers. The Markdown snapshot is reference material. The retired standalone report and its builders remain available in Git history at `1eb0741`.
