"""Build index.html from portfolio-src.html by inlining the fonts as base64 data URIs.

Run from the repo root: python build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = [
    ("{{GEIST}}", "fonts/geist.woff2"),
    ("{{MONO400}}", "fonts/plexmono-400.woff2"),
    ("{{MONO500}}", "fonts/plexmono-500.woff2"),
    ("{{SHOT1}}", "shots/mandarin-1.webp"),
    ("{{SHOT2}}", "shots/mandarin-2.webp"),
    ("{{SHOT3}}", "shots/mandarin-3.webp"),
    ("{{SHOT4}}", "shots/mandarin-4.webp"),
]


def main():
    src = (ROOT / "portfolio-src.html").read_text(encoding="utf-8")
    for placeholder, asset_path in ASSETS:
        if placeholder not in src:
            raise SystemExit(f"placeholder {placeholder} missing from source")
        b64 = base64.b64encode((ROOT / asset_path).read_bytes()).decode()
        src = src.replace(placeholder, b64)
    # The source is a head+body fragment (kept that way for Artifact previews, which
    # supply their own document skeleton). For Pages, wrap it into a full document.
    head, sep, body = src.partition("</style>")
    if not sep:
        raise SystemExit("could not find </style> to split head from body")
    doc = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        + head + sep + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    )
    out = ROOT / "index.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
