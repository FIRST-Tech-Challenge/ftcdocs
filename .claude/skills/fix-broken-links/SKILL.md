---
name: fix-broken-links
description: Run a full Sphinx linkcheck against FTC Docs, triage every broken link into "genuinely dead" vs "anti-bot/IP blocked", fix the dead ones with verified-live replacement URLs, and add confirmed-blocked domains to linkcheck_ignore. Use when the user wants to "fix broken links", "clean up linkcheck", "reduce link-check false positives", or reduce/resolve the errors the docs site's link checker reports.
user-invocable: true
---

# fix-broken-links — triage and fix FTC Docs' broken links

FTC Docs links out to hundreds of external vendor/reference sites. Some links are
genuinely dead (product delisted, page moved, anchor renamed); others just look
broken because the target site's anti-bot/WAF blocks automated checkers outright.
Treating both the same way is the mistake to avoid: "fixing" a permanently-blocked
domain by retrying/tuning headers wastes CI time forever, and silently ignoring a
domain that's actually just moved its content hides a real dead link from readers.
This skill is the repeatable triage + fix process, plus how to verify a
replacement URL is actually live before writing it into the docs (search engines
and your own memory are not proof — always curl it).

Prerequisite context: see [[docs-linkcheck-pipeline]] if it exists — this repo's
linkcheck has a diff-against-baseline mechanism (`ftcdocs_linkcheckdiff`) where a
broken scheduled workflow can silently make *every* PR's link-check fail against
an empty baseline, which looks identical to "lots of broken links" but has a
totally different fix. Rule that out first (check recent scheduled "Link Check"
workflow runs actually succeed) before assuming the volume of broken links you
see in CI reflects real link rot.

## Workflow

1. **Work in a dedicated worktree/branch**, based on whatever the current linkcheck
   baseline PR/branch is if one is open (so this branch inherits any `conf.py`
   tuning already in flight rather than conflicting with it):
   ```
   git worktree add .claude/worktrees/<name> <base-branch>
   cd .claude/worktrees/<name> && git checkout -b <new-branch-name>
   ```

2. **Run a full linkcheck**, not the PR's `linkcheckdiff` builder — you want every
   currently-broken link, not just ones "new" since some baseline:
   ```
   cd docs
   rm -rf build/linkcheck
   <path-to-venv>/bin/python3.14 -m sphinx -b linkcheck source build/linkcheck -q
   ```
   (Use the repo's `.venv`/`nix develop` environment, not system Python — see the
   repo's `AGENTS.md`/setup docs for which one applies.) This produces
   `build/linkcheck/output.json` (one JSON object per line) and `output.txt`.

3. **Parse and categorize** rather than reading the scrollback:
   ```python
   import json
   from collections import Counter
   lines = [json.loads(l) for l in open('build/linkcheck/output.json') if l.strip()]
   print(Counter(l['status'] for l in lines))  # working/broken/ignored/redirected/timeout/unchecked
   broken = [l for l in lines if l['status'] == 'broken']
   for b in broken:
       print(b['uri'], b.get('info','')[:100], f"({b['filename']}:{b['lineno']})")
   ```

4. **Triage every broken URL with a direct, isolated request** — this is the
   step that actually distinguishes "dead" from "blocked", and search results or
   the error message alone aren't enough evidence:
   ```
   curl -s -o /dev/null -w "%{http_code}\n" -L \
     -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" \
     "<url>"
   ```
   - **Consistent 403/429 on a single plain request** (not a burst, not repeated
     rapid-fire) is IP-reputation/anti-bot blocking (common: SourceForge, W3C,
     GitHub's `/join`, and various e-commerce WAFs like Shopify-fronted vendor
     sites). No header tuning or retry count fixes this — it belongs in
     `linkcheck_ignore` in `conf.py` (with a comment recording the domain, the
     date confirmed, and the evidence, matching the existing entries there).
   - **A real 404, or a 200 at a different URL** is genuine content rot — find
     and apply the actual fix (next step). Don't add these to `linkcheck_ignore`;
     that just hides a real dead link from every future reader.
   - **A same-site (ftc-docs.firstinspires.org) anchor/URL that's broken** means
     something in *this repo* changed (a heading got renamed, a page moved) and
     a hardcoded link elsewhere didn't track it. This is the highest-value fix:
     build the target page locally and check its actual current heading anchor
     IDs (`grep -o 'id="[a-z0-9-]*"' build/html/<path>.html`), then replace the
     hardcoded external-style URL with a proper `:ref:`/`:doc:` — per the style
     guide — so it can't silently rot the same way again.

5. **Find and verify replacements for genuinely dead links.** Use `WebSearch` to
   find where content moved (product page renamed category, page restructured,
   etc.), but never trust a search result's URL or title as proof it's live —
   always `curl` the specific candidate URL yourself before writing it into an
   `.rst` file. When a product is truly discontinued with no confirmed successor
   SKU, prefer linking to the vendor's closest live category/overview page over
   either leaving a dead link or guessing an unconfirmed replacement part number.
   When an existing table already sources the same category from another vendor
   (e.g. a servo comparison table already links ServoCity for one row), prefer
   that vendor for consistency over introducing a new one.

6. **Apply fixes**: for a URL repeated verbatim multiple times in one file, use
   `Edit` with `replace_all: true` after confirming the count with
   `grep -c "<old-url>" <file>`; for the same stale URL appearing in *multiple*
   files, `grep -rn "<old-url>" source/` first — don't assume a single-file fix
   caught every instance.

7. **Re-run the full linkcheck** (step 2-3) until `broken` is 0. Then run a
   normal HTML build with warnings-as-errors to make sure nothing else regressed:
   ```
   <venv>/bin/python3.14 -m sphinx -b html source /tmp/check -q -W
   ```
   For any `:ref:`/`:doc:` link you added or changed, spot-check the actual
   rendered HTML resolves to the right anchor/page rather than assuming:
   ```
   grep -o 'href="[^"]*<target-slug>[^"]*"' /tmp/check/<page>.html
   ```

8. **Commit and PR.** If this branch is based on another open linkcheck-related
   PR (see step 1), note that explicitly in the PR body ("stacked on #NNN") —
   GitHub can't set a cross-fork PR's base to a branch that only exists on the
   fork, so such a stacked PR still targets `main` directly and will show both
   PRs' commits combined until the base one merges (GitHub recalculates the
   diff automatically once it does; this is normal and expected, not a bug to
   fix). Write the PR body as a table of what was actually broken, why (dead vs.
   blocked), and what changed — reviewers should be able to verify each claim
   without re-doing the research themselves.

## What NOT to do

- Don't add a domain to `linkcheck_ignore` just because it showed up broken once
  in a CI run — confirm with a direct, isolated request first. A transient
  outage or a real dead link both look like "broken" in the CI log; only a
  direct check tells you which.
- Don't leave a hardcoded `ftc-docs.firstinspires.org` URL with a patched anchor
  — convert it to `:ref:`/`:doc:` instead, since the whole reason it broke is
  that a hardcoded link doesn't get validated/updated by Sphinx's own
  cross-reference resolution.
- Don't guess a replacement URL from memory or from a search snippet's title —
  verify every single one with a direct request before it goes in the docs.
