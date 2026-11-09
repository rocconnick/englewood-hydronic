# Standalone interactive field guide

Primary output: `../report/index.html`, titled **Englewood Road Hydronic Heating System**. This replaces the prior HTML presentation.

## Rebuild

```sh
python3 reporting/build.py
```

Requires Python 3 and Pillow. No web access, Graphviz, JavaScript libraries, or remote assets are needed. On this Mac, a bundled interpreter is available at `/Users/dominickrocco/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.

- `guide/build.py`: curated equipment records, seven interactive SVG diagrams, single-copy photo embedding, and source-note ingestion.
- `guide/template.html`: report narrative, CSS, native JavaScript interactions, and accessibility/print behavior.
- `../notes/13-guide-synthesis.md`: current synthesis and superseding corrections.
- Legacy `template.html.j2` and `diagrams/*.dot` are retained as historical source only; the new build does not use them.

## Source contract

Topic Markdown and original photographs remain the authoritative evidence record. When findings change, update the applicable Markdown first, then update the curated equipment/narrative/diagram source above. Rebuild the HTML and review diagrams and links. Historical Markdown chapters are embedded verbatim, with a notice about superseded observations.

The build embeds photo derivatives with orientation normalized, maximum dimension 1920 pixels, JPEG quality 86. It does not alter the original images. Every original photo selected for the report has one encoded copy in the HTML data store, reused by the UI. The file is approximately 23 MiB. Manufacturer PDFs are linked, not embedded; internet is needed for external links only.

## Features

- Seven diagram views: plant/basement, main loop, Mix 1, Mix 2, domestic water, control relationships, partial electrical schematic.
- Keyboard-focusable diagram components, hover photo previews, click/tap detail dialogs, photo enlargement, zoom controls, and horizontal scrolling on phones.
- Equipment search, five operating walkthroughs, zone map, known issues and parts crosswalk, embedded photo library, searchable/downloadable Markdown chapters.
- Print styling includes all diagram views and operating sequences.

## Evidence conventions

Solid lines identify traced/documented relationships; dashed purple routes mark inferred or incomplete control paths. Equipment blocks are functional assemblies. Hydronic drawings use directional circulator symbols, valve symbols, labeled sensor bubbles, and junction dots; crossings without dots are separate. They are explanatory schematics, not complete installation wiring or construction drawings.

Do not turn tentative stages, sensor endpoints, replacement candidates, or controller logic into confirmed connections. Do not infer a ZCM failure from connected TELESTAT R1/R2 voltage alone.
