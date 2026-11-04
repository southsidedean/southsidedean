#!/usr/bin/env python3
"""Compare the project logos in Tom's local repos, so a new one doesn't reuse an old one.

Usage: scripts/check-logos.py [--sheet out.html] [repos-dir]

Reads every *logo*.svg in the checkouts under repos-dir (default: the folder that
holds this repo) and compares each repo's logos with the other repos' logos, by
the shapes they're drawn with and ignoring colors. It fails on a copy of another
repo's logo, or on two or more shapes in common. The monitor frame some logos
share is a family look, so it's only listed. --sheet writes a page showing every
logo side by side: shape matching can't tell when two different drawings look
alike, so look at the page before using a new logo.
"""

import html
import itertools
import os
import sys
import xml.etree.ElementTree as ET

SKIP_DIRS = {".git", ".backups", ".terraform", "node_modules"}
# Monitor frame and stand: (tag, x, y, width, height, rx)
FRAME = {
    ("rect", ("height", "42"), ("rx", "9"), ("width", "56"), ("x", "4"), ("y", "8")),
    ("rect", ("height", "4"), ("rx", "2"), ("width", "16"), ("x", "24"), ("y", "53")),
}
PAINT = {"fill", "stroke", "opacity", "stroke-linecap", "stroke-linejoin", "style", "class"}


def shapes(path):
    """Return the set of shapes in an SVG, without their colors."""
    found = set()
    for el in ET.parse(path).getroot().iter():
        tag = el.tag.rsplit("}", 1)[-1]
        if tag not in ("svg", "g", "title", "desc", "defs"):
            found.add((tag, *sorted((k, v) for k, v in el.attrib.items() if k not in PAINT)))
    return found


def find_logos(root):
    """Return {repo name: [logo paths]} for the repos under root."""
    logos = {}
    for repo in sorted(os.listdir(root)):
        top = os.path.join(root, repo)
        if not os.path.isdir(os.path.join(top, ".git")):
            continue
        for folder, dirs, files in os.walk(top):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in sorted(files):
                if "logo" in name.lower() and name.lower().endswith(".svg"):
                    logos.setdefault(repo, []).append(os.path.join(folder, name))
    return logos


def write_sheet(path, logos):
    cells = []
    for repo, paths in logos.items():
        for logo in paths:
            with open(logo, encoding="utf-8") as f:
                drawing = f.read()
            background = "#0d1117" if "dark" in os.path.basename(logo) else "#ffffff"
            cells.append(
                f'<figure style="margin:0;padding:12px;background:{background};text-align:center">'
                f'<div style="width:128px;margin:auto">{drawing}</div>'
                f'<figcaption style="color:#808080;font-size:13px">{html.escape(repo)}<br>'
                f"{html.escape(os.path.basename(logo))}</figcaption></figure>"
            )
    with open(path, "w", encoding="utf-8") as f:
        f.write(
            '<!doctype html><meta charset="utf-8"><title>Project logos</title>'
            '<body style="margin:0;font-family:sans-serif;background:#808080">'
            '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:4px">'
            + "".join(cells) + "</div>\n"
        )


def main(args):
    sheet = None
    if args[:1] == ["--sheet"]:
        sheet, args = args[1], args[2:]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    logos = find_logos(root)
    if not logos:
        sys.exit(f"No logos found under {root}")
    drawn = {path: shapes(path) for paths in logos.values() for path in paths}

    problems = 0
    framed = sorted(repo for repo, paths in logos.items() if any(FRAME <= drawn[p] for p in paths))
    for repo_a, repo_b in itertools.combinations(logos, 2):
        for a, b in itertools.product(logos[repo_a], logos[repo_b]):
            shared = (drawn[a] & drawn[b]) - FRAME
            if drawn[a] == drawn[b] or len(shared) >= 2:
                problems += 1
                print(f"FAIL {repo_a}/{os.path.basename(a)} and {repo_b}/{os.path.basename(b)}: "
                      f"{len(shared)} shapes in common beyond the frame")

    print(f"{len(drawn)} logos in {len(logos)} repos, {problems} problems")
    print("On the monitor frame: " + ", ".join(framed))
    if sheet:
        write_sheet(sheet, logos)
        print(f"Wrote {sheet}. Look at it before using a new logo.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
