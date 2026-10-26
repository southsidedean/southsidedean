#!/usr/bin/env python3
"""Rebuild the README's "Recent activity" list from Tom's public personal repos.

Usage: scripts/update-whats-new.py [README.md]

Rewrites the lines between the WHATS-NEW markers in place. Only repos owned by
the user account are read, so employer (org) repos can never appear. Forks,
archived and private repos, and the profile repo itself are skipped. Set
GITHUB_TOKEN (or GH_TOKEN) to avoid the unauthenticated API rate limit.
"""

import json
import os
import sys
import urllib.request

USER = "southsidedean"
MAX_REPOS = 8     # most recently pushed repos to look at
MAX_ENTRIES = 8   # lines to show in the README
MAX_RELEASES = 4  # release lines per repo, so one busy repo can't fill the list
START = "<!-- WHATS-NEW:START -->"
END = "<!-- WHATS-NEW:END -->"


def get(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER},
    )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def entries():
    repos = [
        r for r in get(f"users/{USER}/repos?type=owner&sort=pushed&per_page=30")
        if not (r["fork"] or r["archived"] or r["private"]) and r["name"] != USER
    ][:MAX_REPOS]

    found = []
    for repo in repos:
        name, url = repo["name"], repo["html_url"]
        dates = set()

        # Releases come newest first. Keep the newest of each minor version
        # (v0.6.5 stands in for v0.6.0-v0.6.4) so patch releases don't crowd
        # out everything else.
        lines = set()
        for rel in get(f"repos/{USER}/{name}/releases?per_page=50"):
            if rel["draft"] or rel["prerelease"]:
                continue
            line = ".".join(rel["tag_name"].lstrip("v").split(".")[:2])
            if line in lines:
                continue
            if len(lines) == MAX_RELEASES:
                break
            lines.add(line)
            day = rel["published_at"][:10]
            dates.add(day)
            found.append((day, f"Released [{name} {rel['tag_name']}]({rel['html_url']})"))

        day = repo["created_at"][:10]
        dates.add(day)
        found.append((day, f"Created [{name}]({url})"))

        # A push on the same day as a release or creation adds nothing new.
        day = repo["pushed_at"][:10]
        if day not in dates:
            found.append((day, f"Updated [{name}]({url})"))

    found.sort(key=lambda e: e[0], reverse=True)
    return found[:MAX_ENTRIES]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    with open(path, encoding="utf-8") as f:
        text = f.read()

    head, sep, rest = text.partition(START)
    _, sep2, tail = rest.partition(END)
    if not (sep and sep2):
        sys.exit(f"{path}: WHATS-NEW markers not found")

    lines = "\n".join(f"- {day}: {what}" for day, what in entries())
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{head}{START}\n{lines}\n{END}{tail}")


if __name__ == "__main__":
    main()
