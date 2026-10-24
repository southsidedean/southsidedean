#!/usr/bin/env bash
# Builds Resume-Tom-Dean.html and Resume-Tom-Dean.pdf from Resume-Tom-Dean.md.
# Needs pandoc and Chrome/Chromium. Set CHROME to override the browser path.
# Usage: scripts/build-resume.sh [output-dir]   (defaults to the repo root)

set -euo pipefail

cd "$(dirname "$0")/.."
out=${1:-.}
mkdir -p "$out"

if [ -z "${CHROME:-}" ]; then
    for c in google-chrome google-chrome-stable chromium chromium-browser \
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
        if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then
            CHROME=$c
            break
        fi
    done
fi
: "${CHROME:?Chrome or Chromium not found; set CHROME to its path}"

pandoc Resume-Tom-Dean.md \
    --from gfm \
    --standalone \
    --embed-resources \
    --css resume/resume.css \
    --metadata pagetitle="Tom Dean - Resume" \
    --output "$out/Resume-Tom-Dean.html"

"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$out/Resume-Tom-Dean.pdf" \
    "file://$(cd "$out" && pwd)/Resume-Tom-Dean.html" 2>/dev/null

echo "Built $out/Resume-Tom-Dean.html and $out/Resume-Tom-Dean.pdf"
