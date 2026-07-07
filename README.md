# portfolio

William Liu's public portfolio site, served by GitHub Pages at <https://projectsofwill.github.io/>.
A single self-contained page with two views (RevOps Systems, AI Infrastructure), dark by default,
fonts embedded, no external requests, no tracking.

**How to work on it:** edit `portfolio-src.html` (the source, with font placeholders), then run
`python build.py` to regenerate `index.html` (the built page Pages serves). Never hand-edit
`index.html`. Commit both files together; the site updates on push.
