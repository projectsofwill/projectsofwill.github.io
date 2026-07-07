# portfolio — router

William Liu's public portfolio page (GitHub Pages user site, <https://projectsofwill.github.io/>).
Live status: `STATUS.md`. Content/voice/sensitivity rules: `Projects/Job Prep/portfolio-design-brief.md`
(cross-repo pointer for local sessions; this repo must still build standalone without it).

## Key files

- `portfolio-src.html` — THE SOURCE. All edits happen here. Contains `{{GEIST}}` / `{{MONO400}}` /
  `{{MONO500}}` placeholders where fonts get inlined.
- `build.py` — regenerates `index.html` from the source (inlines `fonts/*.woff2` as base64).
- `index.html` — BUILT output, what Pages serves. Never hand-edit; always rebuild and commit with the source.

## Conventions

- **Voice:** Will's business register. No em dashes, no exclamation points, no "not just X but Y",
  first person, past tense for shipped work.
- **Sensitivity:** never name Will's employer on the page; no bot handles, IPs, or host vendors;
  demo data is always labeled synthetic; contact via LinkedIn/GitHub only, no email.
- **Design system:** dark default, Harry Atkins-extracted grey token ramp, amber strictly reserved
  for AI-at-the-edges semantics, Geist + IBM Plex Mono (embedded, no CDN). No external requests of
  any kind; the page is fully self-contained.
- The `<meta name="robots" content="noindex">` tag stays until Will declares the page launched,
  then remove it deliberately.
- Commit only when Will asks (a commit publishes within ~15 min via auto-sync, and Pages serves it).
