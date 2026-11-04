# How this repository works

This repo is my GitHub profile page and the source of my resume. GitHub shows `README.md` on my profile, and the resume is a Markdown file that gets built into HTML and PDF and published as a GitHub Release. Here's how the pieces fit together, in case you want to build something like it for yourself.

## What's in it

| File | What it does |
| --- | --- |
| `README.md` | The profile page. The Recent activity list is generated; the rest is written by hand. |
| `Resume-Tom-Dean.md` | The resume, and the only copy I edit. |
| `resume/resume.css` | Styles for the HTML and PDF builds, including the print layout that keeps the PDF to three pages. |
| `resume/LinkedIn-Tom-Dean.md` | The resume reworked as paste-ready LinkedIn text, kept in step with the resume. |
| `Short-Bio-Tom-Dean.txt` | A short third-person bio. |
| `scripts/build-resume.sh` | Builds the HTML with pandoc, then prints it to PDF with headless Chrome. |
| `scripts/check-content-policy.sh` | Fails the build if something I've ruled out shows up in the published files. |
| `scripts/update-whats-new.py` | Rebuilds the Recent activity list from the GitHub API. |
| `.github/workflows/` | The three workflows described below. |

The built HTML and PDF are never committed. They only exist as release assets.

## How an edit gets made

Nothing goes straight to `main`. A ruleset blocks direct pushes, force pushes, and deleting the branch, and it requires a linear history. Every change goes through a branch and a pull request:

1. Edit the Markdown on a branch. To see the result locally, run `scripts/build-resume.sh dist`.
2. Open a pull request. The content checks run on it.
3. When the required checks pass, squash-merge it. GitHub deletes the branch.
4. If the resume changed, the release workflow publishes a new version a minute or so later.

I make some edits by hand in VS Code and talk others through with Claude Code. Either way, Claude Code reviews the changes, keeps the resume, README, bio, and LinkedIn text consistent, and opens the pull requests. I review and merge each one myself.

## The checks

`content-checks.yml` runs on every pull request, on every push to `main`, and every Monday, which catches links that have died since the last change.

| Check | Tool | What it catches |
| --- | --- | --- |
| Content policy | `scripts/check-content-policy.sh` | Leftover draft markers, an old email address, phone numbers, and other things I've decided must not ship |
| Resume builds | pandoc and Chrome | A resume that won't build. The HTML and PDF are uploaded as a `resume-preview` artifact, so I can check the page count before merging. |
| Spelling | codespell | Typos |
| Markdown lint | markdownlint-cli2 | Broken or inconsistent Markdown |
| Secrets scan | gitleaks | Credentials committed by accident |
| Workflow lint | actionlint and zizmor | Mistakes and security problems in the workflows themselves |
| Links | lychee | Dead links. This one isn't required, because outside sites go down and would block merges. |

The content policy is a plain list of regular expressions in a shell script, so adding a rule takes one line.

## How the resume is published

`release-resume.yml` runs when the resume, its styles, or the build script changes on `main`. It builds both files and creates a release tagged `resume-YYYY-MM-DD-<commit>`, marked as the latest.

Every link to my resume points at the latest release:

```text
https://github.com/southsidedean/southsidedean/releases/latest/download/Resume-Tom-Dean.pdf
```

That address never changes, so the links on my profile, my website, and LinkedIn stay current without any edits. The [releases page](https://github.com/southsidedean/southsidedean/releases) keeps every version I've published.

## How Recent activity stays current

`whats-new.yml` runs four times a day. It reads my public repos (only ones I own, so employer repos can't appear, and no forks or archived repos), lists recent releases and updates, and rewrites the lines between two HTML comment markers in the README.

It doesn't commit to `main`. It opens a pull request, or updates the one already open, and I merge it like any other change. A pull request opened with the workflow's own token doesn't trigger other workflows, so the job starts the content checks on its branch itself.

## Keeping it locked down

- Workflows start with `permissions: {}`, and each job asks only for what it needs. Only the release and Recent activity jobs can write.
- Every Action is pinned to a full commit SHA, with the version in a comment.
- The repo allows only GitHub's own Actions and the few third-party ones listed above.
- Dependabot opens one grouped pull request a week for Action updates, and waits seven days after a release before suggesting it.
- Secret scanning and push protection are on.

## Roll your own

You don't need all of this. A useful version is a profile README, a Markdown resume, the build script, and the release workflow. Add the checks and the activity list once that works.

1. Create a public repo named after your GitHub username. GitHub shows its `README.md` on your profile.
2. Write your resume in Markdown, and copy `scripts/build-resume.sh` and `resume/resume.css`. Change the file names and the page title.
3. Copy `release-resume.yml` and change the paths. Link to `releases/latest/download/<your file>.pdf`.
4. Copy `content-checks.yml` and rewrite `check-content-policy.sh` with your own rules.
5. In Settings, add a ruleset for `main` that requires pull requests and your checks.
6. If you want the activity list, copy `update-whats-new.py` and `whats-new.yml`, change `USER`, and turn on "Allow GitHub Actions to create and approve pull requests" under Settings > Actions.

Two things to know:

- The activity job's pull requests come from `github-actions[bot]`. If your repo asks for approval before running workflows from first-time contributors, the bot counts as one, and its checks wait until you approve the run.
- GitHub turns off scheduled workflows after 60 days without activity in the repo.

### A prompt to get started

If you use Claude Code or another coding agent, start it in your new repo and give it something like this:

```text
Set up this repository as my GitHub profile and resume, modeled on
https://github.com/southsidedean/southsidedean. Read its README, its
HOW-THIS-REPO-WORKS.md, and the files they describe before you start.

1. Ask me for my resume (paste or file) and convert it to Markdown in
   Resume-<Name>.md. Don't invent anything. Ask when something is missing.
2. Add a build script that turns the Markdown into HTML with pandoc and into
   PDF with headless Chrome, plus a stylesheet with a print layout. Keep the
   built files out of git.
3. Add a workflow that builds the resume on every change to main and
   publishes it as a GitHub Release marked latest.
4. Add a checks workflow: build the resume, spell check, Markdown lint,
   secrets scan, and workflow lint. Give each workflow permissions: {} at the
   top and only what each job needs, and pin every Action to a commit SHA.
5. Write a short profile README that links to the latest resume PDF.
6. Do all of this on a branch and open a pull request. Don't merge it, and
   tell me which repo settings I need to change.
```

Read what it produces before you merge, since your name is on it.
