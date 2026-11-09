# Working in this repository

- Start with README.md for the layout and local preview commands. Use `dist/` as the canonical site and deployment root.
- Edit topic articles in `dist/kb/` and equipment entries in `dist/equipment/`. Keep each equipment page's `component-record` JSON aligned with its visible text. Edit `dist/index.html` for overview layout and diagrams.
- Distinguish field observations, manufacturer specifications, and inferences. Keep equipment tags and part numbers consistent across pages. Identify unresolved wiring or diagnostic questions explicitly.
- Put publishable image copies in `dist/assets/photos/`. Preserve original photos in `evidence/original-photos/` and keep site links within `dist/`.
- After changes, run `python3 tools/refresh.py` and `python3 tools/validate.py` from the root. Review generated diffs and preview affected pages over HTTP.
- Use `.openai/hosting.json` for the existing Sites project. GitHub and the deployed site are separate. Publish the site when requested.
- Treat the legacy Markdown snapshot and migration records as evidence. Maintain current content in HTML.
