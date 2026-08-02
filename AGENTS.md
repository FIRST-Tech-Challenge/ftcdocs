# AGENTS.md

## What this project is

This repository is the *FIRST* Tech Challenge (FTC) documentation project — the source for
https://ftc-docs.firstinspires.org. There is no application code here. The entire repo builds a
documentation website (HTML), a single combined PDF manual, and a set of smaller topic "booklet"
PDFs, all from [Sphinx](https://www.sphinx-doc.org/)/reStructuredText (`.rst`) source files under
`docs/source/`.

There is no test suite or app to run. "Correctness" here means: the Sphinx build completes with zero
warnings, internal/external links resolve, images meet size rules, and content follows the project's
writing/accessibility style guide (all enforced in CI, see below).

## Repo layout

```
docs/
  Makefile                # all build entry points (see Build commands)
  requirements.txt        # Python deps, including several FIRST-Tech-Challenge/ftcdocs-helper packages
  scripts/                # standalone maintenance scripts, not part of the Sphinx build itself
    imagesizechecker.py   #   run via `make imagecheck`
    convert_md_to_rst.py  #   one-off Markdown -> RST converter (pandoc wrapper)
    convertWebp.py        #   one-off image format converter
  source/
    conf.py                # Sphinx config: theme, extensions, LaTeX/PDF layout, linkcheck rules
    index.rst               # site homepage; also the master toctree that defines the left nav
    redirects.txt           # old-path -> new-path pairs, checked by rediraffe (see Redirects below)
    booklets/                # booklet landing page + per-booklet "chapter list" stub docs (see Booklets below)
    <topic>/                 # one directory per top-level subject area, e.g.:
      programming_resources/
      apriltag/
      manufacturing/
      hardware_and_software_configuration/
      control_hard_compon/
      color_processing/
      contrib/                # the contributor-facing docs you're reading conventions from
      ...
dependencies                 # apt package list installed by CI (LaTeX/xetex/fonts) for PDF builds
.readthedocs.yaml             # Read the Docs build config (Sphinx, Python 3.11, PDF format)
.devcontainer/                 # Codespaces/devcontainer image with the same LaTeX + Python toolchain
.github/workflows/             # CI: PR checks, scheduled link-check, booklet builds, artifact cleanup
```

### The folder-per-topic content pattern

Content is organized as **one directory per document**, not one flat file per document. A typical
leaf topic looks like:

```
docs/source/apriltag/vision_portal/apriltag_intro/
  apriltag-intro.rst          # the document itself
  images/                     # images referenced by this doc only
    020-Sample-Tags.png
    100-Tag-size-42.png
  files/                      # (optional) downloadable non-image assets, e.g. PDFs
    AprilTag_0-20_family36h11.pdf
```

- The `.rst` file's name usually mirrors its parent directory name (`apriltag_intro/apriltag-intro.rst`,
  `3d_printing_intro/3d_printing_intro.rst`). Older content sometimes uses underscores or MixedCase in
  the filename (e.g. `Blocks-Tutorial.rst`, `The-FTC-Control-System.rst`); new documents should follow
  the style guide instead (see Filenames below) — lowercase and hyphens.
- Images live in an `images/` subfolder **local to the document that uses them** — never a shared/global
  image folder. This keeps a topic's assets self-contained when moved or deleted.
  Reference them with a relative path: `.. image:: images/my-image.png`.
- A directory that has children (a "section") has its own `index.rst` (or `<name>.rst` matching the
  directory, e.g. `manufacturing/3d_printing/index.rst`) that both introduces the section in prose and
  contains a `.. toctree::` pulling in the child documents. See `docs/source/programming_resources/index.rst`
  for the pattern: a short bullet list of `:doc:` links in the visible body, followed by a `:hidden:`
  toctree with the same targets (the hidden toctree drives the sidebar/nav; the bullet list is what
  readers actually see on the page).
- `docs/source/index.rst` is the sitewide homepage and defines the *entire* top-level navigation as a
  sequence of captioned `.. toctree::` blocks (`Getting Started`, `Game and Season-Specific Resources`,
  `Control System Resources`, `AprilTag Resources`, etc.). Adding a new top-level section of the site
  means adding an entry there. It also uses `sphinx_design` `.. grid::` / `.. grid-item-card::` /
  `.. button-ref::` / `.. button-link::` directives to build the "quick links" cards — follow that
  pattern rather than inventing new homepage layout.
- `:orphan:` at the top of a `.rst` file (see `docs/source/booklets/apriltags.rst`) tells Sphinx the
  document is intentionally not reachable from any toctree — used for the LaTeX-only booklet chapter
  lists.

## Setup

```bash
cd docs
make setup          # pip install -r requirements.txt
```

Requires Python 3.11 (matches CI and `.readthedocs.yaml`). PDF/booklet builds additionally need a
LaTeX toolchain (xetex, latexmk, fonts) — see the root `dependencies` file (apt package list used by
CI) or `.devcontainer/Dockerfile` for the exact set. GitHub Codespaces / the devcontainer already has
everything installed; local PDF builds are only fully supported on Linux (per
`docs/source/contrib/tutorials/setup/setup.rst`).

## Build & preview commands

Run from the `docs/` directory:

- `make autobuild` — live-reloading local preview at `http://localhost:7350` (the default VS Code
  build task, `Ctrl+Shift+B`). Use this while iterating on content.
- `make html` — one-shot HTML build to `docs/build/html`.
- `make latexpdf` — builds the single combined PDF manual via LaTeX/XeTeX to `docs/build/latex`.
- `make booklets` — builds the per-topic PDF booklets to `docs/build/booklets` (see Booklets below).
- `make local-full` — HTML + full PDF, with the PDF copied into the HTML output (mirrors the "official"
  production build; sets `DOCS_BUILD=true`).
- `make imagecheck` — runs `docs/scripts/imagesizechecker.py`: fails if any image exceeds the size limit
  (500KB) or dimension limit, except paths listed in `IMAGE_SIZE_EXCLUSIONS` in `conf.py`.
- `make linkcheckdiff` — runs Sphinx's link checker and diffs against a previous run's output (this is
  what CI runs on every PR and on a schedule).
- `make rediraffecheckdiff` — validates `docs/source/redirects.txt` is complete relative to `origin/main`
  (see Redirects below).
- `make clean` — removes `docs/build`.

### Verifying a change (build test)

After editing content, use `make html` (run from `docs/`) as the standard build/verification check:

```bash
cd docs && make html
```

This is fast (no LaTeX involved) and mirrors the CI `build-html` gate closely enough to catch the
things that matter for a content change — broken `:ref:`/`:doc:` targets, malformed directives,
duplicate labels, and other Sphinx warnings. For a check even closer to CI, add
`SPHINXOPTS="-W --keep-going -n"` so warnings fail the build the same way they do in
`pull-request.yaml`:

```bash
cd docs && make html SPHINXOPTS="-W --keep-going -n"
```

**Avoid running `make latexpdf` or `make booklets` to verify a routine content change** — both invoke
the LaTeX/XeTeX toolchain and are slow (multi-minute) compared to the HTML build. Only run them when
the task is specifically about PDF/LaTeX output (e.g. changes to `latex_elements` in `conf.py`, the
booklet chapter lists under `docs/source/booklets/`, or LaTeX-only content wrapped in
`.. only:: latex`) or when you need to confirm a PDF-specific regression is actually fixed.

## Booklets

Booklets are standalone, smaller PDFs (e.g. "3D Printing Guide", "AprilTag Guide", "Blocks Manual")
assembled from a subset of the same source content used in the main site/manual, meant to be printed
and used as quick references. The mechanism:

1. `docs/source/conf.py` checks the `BOOKLETS_BUILD` environment variable. When set to `"true"`, it
   overrides `latex_documents` (normally just the single combined manual) with a list of
   `(master_doc, output_tex_filename, title, author, "manual")` tuples — one per booklet, e.g.
   `('booklets/apriltags', "april_tags.tex", 'April Tags Guide', author, "manual")`.
2. Each booklet's `master_doc` points either directly at a real content page (e.g.
   `manufacturing/3d_printing/index`) or at a small `:orphan:` stub under `docs/source/booklets/`
   (e.g. `booklets/apriltags.rst`) whose only job is to hold a `.. only:: latex` toctree listing the
   chapters that belong in that specific booklet, since the booklet's chapter set doesn't match any
   single page's normal toctree.
3. `make booklets` runs `BOOKLETS_BUILD=true sphinx-build -M latexpdf ...` (building every booklet's
   `.tex`/`.pdf` in one pass) and then copies the resulting PDFs into `docs/build/booklets`.
4. `docs/source/booklets/index.rst` is the *public* landing page on the live site — it's just a manually
   maintained list of links to `https://ftc-docs-cdn.ftclive.org/booklets/en/<name>.pdf`. It is **not**
   auto-generated from the booklet list in `conf.py`; adding a new booklet means updating both places.
5. In CI, `.github/workflows/booklets.yaml` runs `make -C docs/ booklets` on every push to `main` and
   syncs the output to the `ftc-docs-cdn` S3 bucket, which is what the CDN links in `booklets/index.rst`
   ultimately serve.

If you add a new booklet or change what belongs in an existing one, update the `latex_documents`
override block in `conf.py` (search for `BOOKLETS_BUILD`) and the corresponding entry in
`docs/source/booklets/index.rst`.

## Redirects

`docs/source/redirects.txt` is a flat list of `old/path.rst new/path.rst` pairs (space-separated, one
per line), consumed by the `sphinxext-rediraffe` extension (`rediraffe_redirects` /
`rediraffe_branch = "origin/main"` in `conf.py`). Whenever you rename or move an `.rst` file, add a
line here mapping the old path to the new one — otherwise `make rediraffecheckdiff` (and the
`check-redirect` CI job) will fail the PR, and readers/search engines with the old URL will get a
broken link instead of a redirect.

## What CI checks on every PR (`.github/workflows/pull-request.yaml`)

Treat these as the acceptance criteria for any content change — they all run automatically on PRs:

1. **build-html** — `make html` with `-W --keep-going -n` (Sphinx warnings are treated as errors, e.g.
   duplicate labels, broken `:ref:`/`:doc:` targets, malformed directives). This is the check you should
   reproduce locally (see Verifying a change above).
2. **build-pdf** — `make latexpdf` must succeed (LaTeX/XeTeX build of the full manual). Slow; only run
   locally if the change is PDF/LaTeX-specific.
3. **spelling-check** — `reviewdog/action-misspell` (US locale) flags misspellings.
4. **link-check** — `make linkcheckdiff`; validates every link resolves, diffed against the last
   main-branch run so only *newly broken* links fail the PR. Some flaky/hostile domains are
   intentionally excluded via `linkcheck_ignore` in `conf.py` (Solidworks, Autodesk, Dell, etc. — they
   403/redirect-loop bots).
5. **image-check** — `make imagecheck`; enforces image size/dimension limits.
6. **check-redirect** — `make rediraffecheckdiff`; fails if a renamed/moved doc has no entry in
   `redirects.txt`.

There's also a separate scheduled workflow (`link-check.yaml`, every 12h) that re-runs link-check
against `main` independently of PRs, and `booklets.yaml` which rebuilds and republishes booklets on
every push to `main`.

## Content style guide

Full guide: `docs/source/contrib/style_guide/style-guide.rst` (general RST/writing conventions),
`docs/source/contrib/style_guide/image-and-figure-details.rst` (images in depth), and
`docs/source/contrib/style_guide/ftc-docs-accessibility-guidelines.rst` (WCAG-mapped guidance). Key
points to actually apply:

**Filenames** — lowercase alphanumeric + `-` (hyphen) only, e.g. `style-guide.rst`. Append
`-hardware`/`-software` when a hardware and a software doc would otherwise share a name.

**Section heading underlines**, in strict nesting order (don't skip a level, and titles/headings must
be unique within a document):

| Level | Character | Example |
|---|---|---|
| Title | `=` | `======` |
| Section | `-` | `------` |
| SubSection | `^` | `^^^^^^` |
| SubSubSection | `"` | `""""""` |
| SubSubSubSection | `+` | `++++++` |

**Text formatting** — ASCII for English text (use character entity sets for special characters);
`*text*` = italics, `**text**` = bold, `` ``text`` `` = literal (use literals for filenames,
functions, variable names). One space between sentences. One blank line between text blocks/section
titles/content directives. Indentation of directive content is 3 spaces and should match the
surrounding indentation level unless starting a new content block.

**Tables** — use `list-table` or `csv-table` directives. Avoid ASCII-art grid tables.

**Admonitions** — `attention`, `caution`, `danger`, `error`, `hint`, `important`, `note`, `tip`,
`warning`. FTC Docs leans heavily on `note` and `warning`. Keep them short.

**Links**:
- Never use "click here"/"learn more" as link text; link text should describe the destination and be
  unique if multiple links look similar.
- Internal section reference: add a label above a heading (`` .. _my label: ``) then reference with
  `` :ref:`my label` `` or `` :ref:`Custom Text <my label>` ``.
- Internal document reference: `` :doc:`relative/path` `` or `` :doc:`/absolute/path/from/source` ``;
  rendered link text defaults to the target's title unless overridden with `` :doc:`Text <path>` ``.
- External links open in a new tab automatically (via JS in `conf.py`'s `setup()`), so no special
  markup is needed for that, but still write descriptive text: `` `Game and Season Materials <url>`_ ``.
- Links to downloadable files (PDF, etc.) should say the file type/size in the link text, and ideally
  point to a "gateway page" describing the file rather than linking the file directly (accessibility —
  avoids surprise context switches). Use `.. button-link::` for a file-download call to action.

**Images** (see full detail in `image-and-figure-details.rst`):
- Store in a local `images/` subfolder next to the referencing `.rst` file.
- PNG or JPEG only — GIF and SVG are not supported in the PDF build.
- Under 500KB and ≤1000px wide, unless explicitly exempted via `IMAGE_SIZE_EXCLUSIONS` in `conf.py`
  (reserved for cases like the RC/DS wiring diagrams where extra resolution is genuinely needed).
- Filenames: short description, under ~24 characters.
- Always set `:alt:`. If you omit it, Sphinx falls back to the image filename/path as the alt text,
  which a screen reader will read aloud verbatim — treat a missing `:alt:` on any image you touch as a
  bug to fix, even if unrelated to your change.
- Alt text guidelines: ≤~150 characters, don't start with "image of"/"photo of", end with a period,
  front-load the important words, avoid jargon.
- FTC Docs does **not** use purely decorative images (images added "because they look nice"). If one is
  ever unavoidable, use `.. image::` with an explicitly blank `:alt:` so screen readers skip it.
- Use `.. image::` when no caption is needed; use `.. figure::` only when a *visible* caption or a long
  description ("legend") is required (e.g. photo credits, or connecting the image to surrounding
  editorial text). Alt text and caption must say different things — alt text is functional
  (what's literally in the image), caption is editorial/illustrative.
- Avoid the `align`, `width`, `height`, `scale` options where possible — they create accessibility
  problems (image floats out of context in PDF; Sphinx auto-links the image to a full-size version with
  no link title). If you must constrain width, add `:class: no-scaled-link` to suppress that
  auto-generated link.
- Prefer local, project-hosted images over externally-hosted ones (availability/copyright risk).

**Accessibility** is treated as a first-class, ongoing concern (not just images) — see
`ftc-docs-accessibility-guidelines.rst` for the WCAG-mapped rationale before making structural changes,
especially anything involving Sphinx "grid"/card/button directives (flagged there as a known screen
reader problem: they render as fake buttons).

## Contribution process expectations

- Issues before PRs: bug reports and feature requests are expected to start as GitHub issues
  (`docs/source/contrib/guidelines/guidelines.rst`). Check for duplicates first.
- PR titles should concisely describe the change's purpose.
- This is a *FIRST* community project — content and interactions should reflect "Gracious
  Professionalism" (`docs/source/gracious_professionalism/gp.rst`).
- `docs/source/contrib/workflow/workflow.rst` documents the maintainer-level view of how a merged PR
  flows through GitHub Actions to the live site (RTD for HTML, S3/CDN for booklets) and how translation
  (Transifex, via a separate `ftcdocs-translation` repo) fits in — useful background if a change you're
  making affects the build pipeline itself rather than just content.
