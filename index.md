# Documents

* [README](README.md) - What this repo is and the edit → build → commit loop.
* [CLAUDE](CLAUDE.md) - Project router: key files, voice/sensitivity/design conventions.
* [STATUS](STATUS.md) - Live status: where the build stands, next steps, open questions.

# Scripts

* [build.py](build.py) - Regenerates index.html from portfolio-src.html (inlines fonts as base64).

# Site files

* portfolio-src.html - The page source (edit this one; placeholders for embedded fonts).
* index.html - Built output served by GitHub Pages (generated, never hand-edited).

# Subdirectories

* fonts/ - woff2 latin subsets (Geist variable, IBM Plex Mono 400/500) inlined at build time.
