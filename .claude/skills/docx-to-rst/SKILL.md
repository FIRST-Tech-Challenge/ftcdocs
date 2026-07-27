---
name: docx-to-rst
description: Convert a Word (.docx) guide into an FTC Docs reStructuredText page, correctly placed in the docs/source tree, with images extracted and captions/alt-text rewritten to the FTC Docs style guide, then wire it into a toctree and (optionally) a booklet. Use when the user hands you a .docx (or similar externally-authored doc) and wants it "pulled into ftcdocs" / "converted to rst" / "added to the docs site".
user-invocable: true
---

# docx-to-rst — ingest a Word doc into FTC Docs

This repo (FIRST-Tech-Challenge/ftcdocs) periodically receives finished guides as
`.docx` files (written outside the repo, e.g. by FIRST staff) that need to become a
real page in `docs/source/`. This skill is the repeatable version of that conversion:
read the docx's structure and images, decide where the content belongs relative to
what already exists, write clean RST per the style guide, and verify the build.

This is a content-authoring task, not a mechanical format conversion — pandoc-style
docx→rst tools produce garbage for this repo's needs (wrong heading levels, no alt
text, duplicate content ignored, images dumped flat). Do the extraction
programmatically, but write the RST by hand section by section.

## Workflow

1. **Locate and install tooling.** Find the `.docx` (usually dropped at the repo
   root or a path the user names). Make sure `python-docx` is available.
   Check for Nix first (`command -v nix`) — if present, prefer an ephemeral
   `nix-shell -p python3Packages.python-docx --run '<command>'` (or
   `nix-shell -p python3Packages.python-docx` for an interactive shell) to try
   the package out without installing anything permanently into the system or
   the repo's `.venv`. This repo may also gain a `flake.nix` devShell — if one
   exists at the repo root, `nix develop` is the more correct entry point than
   ad hoc `nix-shell -p`, since it's the pinned, reproducible environment the
   repo itself declares.
   Fall back to `pip install python-docx` (using the repo's `.venv` if one
   exists — `source .venv/bin/activate` before any `pip`/`make` command, check
   for `<repo>/.venv` first, it's the project's own environment, not the
   system Python) only when Nix isn't available.

2. **Read the docx structure**, don't just get plain text — paragraph *styles* carry
   the heading hierarchy and callout types you need to map to RST:

   ```python
   import docx
   d = docx.Document('path/to/file.docx')
   for p in d.paragraphs:
       print(repr(p.style.name), '|', p.text)
   ```

   Note which styles appear (`Heading 1/2/3`, `Caption`, `List Paragraph`, an
   "Alert Box" or similar callout style, table cell text) — these map to RST
   constructs in step 6. Also dump `d.tables` (`row.cells` text) — docx tables
   often hold real content (a parts/tools list) as well as image grids that
   `d.paragraphs` alone won't reveal (see next step).

3. **Extract images and their order/captions**, including images inside table
   cells (python-docx's `Document.paragraphs`/`.tables` only walks top-level
   body content, so a naive script misses images nested in tables). Walk the
   document part relationships and match blips to paragraphs/cells in body
   order:

   ```python
   from docx.oxml.ns import qn
   rels = d.part.rels
   def imgs_in(el):
       return [rels[b.get(qn('r:embed'))].target_ref
               for b in el.iter(qn('a:blip')) if b.get(qn('r:embed')) in rels]
   # imgs_in(paragraph._p) or imgs_in(cell._tc)
   ```

   Build a mapping of `image file -> caption / surrounding bullet list -> where
   it sits in reading order`, by iterating `d.element.body` in document order
   (paragraphs and tables together) rather than `d.paragraphs` alone. Skip
   Word-chrome images that aren't real content: cover/title-page photos,
   header/footer banner graphics, and any `.wdp` alternate-format duplicates.
   Unzip the raw docx (`unzip file.docx -d extract/`) only if you need to
   double check `word/media/` or `word/document.xml` directly.

4. **View the images** (the Read tool renders images) to write real alt text —
   don't guess from the caption alone. Do this in batches of parallel Read
   calls. For each image decide: does it need a visible caption (`.. figure::`)
   or is `.. image::` with just alt text enough (per the style guide, captions
   are for editorial/illustrative text or photo credits — not required for
   every image).

5. **Figure out where the content belongs before writing anything.** This is
   the judgment call that matters most:
   - Search `docs/source/index.rst` for an existing toctree `:caption:` that's
     empty or thin and matches the new content's topic — an unused caption is
     a strong signal of where new content is *supposed* to go.
   - Grep the existing docs tree for pages that already link out to an
     *external* version of this same content (a PDF on
     `ftc-resources.firstinspires.org`, a Google Doc, etc.) — those links
     should be repointed at the new internal page once it exists.
   - Grep for existing pages covering the same subject matter in more depth
     (e.g. this repo has a detailed `managing-esd.rst` — a docx section
     covering the same ground should be condensed to a summary + `:doc:` link
     rather than duplicated). Ask the user when it's ambiguous whether to
     condense, merge, or keep both; don't just silently duplicate.
   - Check `docs/source/contrib/style_guide/style-guide.rst` for filename
     conventions (lowercase-hyphenated, `-hardware`/`-software` suffix rule)
     and `image-and-figure-details.rst` for image/figure/alt-text rules before
     writing RST.
   - If genuinely unsure between 2-3 placement options, ask the user
     (`AskUserQuestion`) rather than picking silently — this decision is hard
     to walk back once cross-links exist.

6. **Set up the folder and copy images**, following the style guide:
   `docs/source/<section>/<page_slug>/<page-slug>.rst` with an `images/`
   subfolder next to it. Rename each image to a short descriptive
   `lowercase-hyphenated.png`/`.jpg` name (not `image17.png`) — this is also
   where you decide which images to drop (duplicates, decorative Word
   chrome, content folded into a condensed section that no longer needs a
   figure).

7. **Write the RST**, mapping docx conventions to this repo's conventions:
   - Heading 1 → section (`-` underline), Heading 2 → subsection (`^`),
     Heading 3 → sub-subsection (`"`). Title uses `=`.
   - A docx "Alert Box" / callout style → the RST admonition matching its
     *content*, not a blanket choice: safety-critical → `.. warning::` or
     `.. caution::`, a nice-to-know aside → `.. note::`, something the reader
     must not skip → `.. important::`.
   - A caption + bullet list describing photo callouts → a `.. figure::` with
     the bullets as the figure's long-description/legend (blank line after
     the caption, then the list, still indented under the figure).
   - Side-by-side images in the source → a `list-table::` with a
     `.. figure::`/`.. image::` per cell (see style guide examples) rather
     than floating/aligned images.
   - Real tabular content (parts lists, cost tables) → `list-table::`, never
     ASCII-art tables.
   - Drop revision-history/changelog tables and any other document-authoring
     housekeeping that doesn't belong in a public docs page, unless the user
     says to keep it.
   - Internal cross-references use `:doc:`/`:ref:` with absolute paths
     (leading `/`), never a bare relative hyperlink target — a plain
     `` `text <path>`_ `` to an internal path silently produces a broken or
     external-style link instead of resolving through Sphinx.
   - External links use the `` `Text <url>`_ `` form with descriptive text,
     never a bare URL; file/PDF links get a note of file type per the style
     guide.

8. **Wire it into a toctree.** Add the new page to its section's `index.rst`
   (or create one), and add that section to `docs/source/index.rst` if it's a
   new top-level caption. Fix any existing pages found in step 5 that linked
   to the old external version.

9. **Build and verify** — don't just trust that the RST parsed:
   ```
   nix develop -c make -C docs html   # if the repo has a flake.nix
   # otherwise:
   source .venv/bin/activate          # if the repo has one
   make -C docs html
   ```
   If the build fails on a missing Python or system package (e.g. a Sphinx
   extension, or a LaTeX package if you also touch a booklet/`latexpdf`
   build) and Nix is available, use a throwaway `nix-shell -p <pkg>` to check
   whether that specific package resolves the error before reaching for a
   permanent `pip install` or system package manager — it's a cheap way to
   confirm the root cause without changing anything persistent, and if it
   works, that's a signal the *repo's* declared dependencies (flake, apt
   `dependencies` file, or `requirements.txt` — whichever this repo is using)
   need that package added, not just your local environment.
   Check the tail *and* grep the full output for warnings/errors scoped to
   the new files' paths (warnings can appear mid-log, not just at the end).
   Then sanity-check the rendered HTML directly: figure/image counts match
   what you expect, every `<img src>` resolves to a file that exists, no
   literal `.. figure::`/`:doc:`/`:ref:` text leaked through unparsed, and
   internal links resolved to real `.html` targets (not 404s). A working
   Chrome/browser tool, if available in the environment, is a good final
   check for layout (image grids, admonition styling) — text-based checks
   above are sufficient when one isn't available.

10. **(Optional) Add a booklet.** If the user wants a standalone printable PDF
    (this repo builds "booklets" — curated PDF subsets — via
    `docs/source/booklets/*.rst`):
    - Create `docs/source/booklets/<slug>.rst` as an orphan page:
      ```rst
      :orphan:

      .. meta::
         :robots: noindex, nofollow

      .. only:: latex

          <Title>
          ========

          .. toctree::

             /<section>/<page_slug>/<page-slug>
      ```
    - Add an entry to the `latex_documents` list inside the
      `if os.environ.get("BOOKLETS_BUILD") == "true":` block in
      `docs/source/conf.py`.
    - Add a link under the matching heading in `docs/source/booklets/index.rst`
      (create a heading if this is a new content category), following the
      `https://ftc-docs-cdn.ftclive.org/booklets/en/<slug>.pdf` URL pattern —
      booklets are built and uploaded to that CDN by CI
      (`.github/workflows/booklets.yaml`), not built locally into that URL.

## Committing / PRing the result

- Do not commit the source `.docx` itself — only the generated `.rst` and
  `images/`, plus the small edits to existing files (toctrees, fixed links,
  `conf.py`). `git add` the specific paths rather than `git add -A` so the
  docx and any scratch files stay untracked.
- This repo's fork workflow: `origin` is the user's fork, `upstream` is
  `FIRST-Tech-Challenge/ftcdocs`. A PR for this kind of change targets
  `upstream:main` from a feature branch pushed to `origin`:
  `gh pr create --repo FIRST-Tech-Challenge/ftcdocs --base main --head <fork-owner>:<branch>`.
