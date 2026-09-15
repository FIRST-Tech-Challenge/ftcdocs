"""Advisory checker for the "link the first mention of every glossary term on
the page" rule documented in docs/source/contrib/style_guide/style-guide.rst.

This is a HEURISTIC, not a source of truth. Whether a word is being used in
the glossary's sense ("a wireless problem during a match" vs. "check for a
match with the DS app version") is a judgment call this script cannot make
reliably, so it never fails the build -- it only prints candidates for a
human (or a PR reviewer) to check. Treat its output as a checklist, not a
verdict.

What it actually catches well: a glossary term's exact spelling appearing in
a page's plain prose before any `:term:` role for that term shows up. It
strips code spans, existing roles/links, and section-title lines first to
cut down obvious false positives, but plurals, alternate casing, and
sense-ambiguous words will still need a human to confirm.

Usage:
    python -m scripts.glossarychecker source [--file path/to/one.rst ...]
"""

import argparse
import os
import re
import sys

GLOSSARY_PATH = os.path.join("glossary", "glossary.rst")

# Files that intentionally contain example prose demonstrating the linking
# rule itself (including deliberate "leave this unlinked" examples) or that
# define a separate, unrelated glossary. Checking these would just produce
# noise about content that is correct on purpose.
EXCLUDED_FILES = {
    os.path.join("contrib", "style_guide", "style-guide.rst"),
    os.path.join("contrib", "tutorials", "glossary", "glossary.rst"),
}

TERM_LINE_RE = re.compile(r"^   (\S.*)$")
CODE_SPAN_RE = re.compile(r"``.*?``")
# docutils cannot nest an interpreted-text role inside strong emphasis, so a
# **bold** mention of a term is not a linkable spot -- blank it like code
# spans rather than flagging it as an uncompliant "first mention".
BOLD_RE = re.compile(r"\*\*.*?\*\*")
# :doc:/:ref:/:download: are blanked outright (their target text isn't a term
# mention). :term: roles are deliberately NOT blanked here -- we need to see
# them intact to tell "the first occurrence IS a :term: role" apart from
# "the first occurrence is bare text that happens to precede a later role".
OTHER_ROLE_RE = re.compile(r":(?:doc|ref|download):`[^`]*`")
TERM_ROLE_RE = re.compile(r":term:`[^`]*`")
EXTERNAL_LINK_RE = re.compile(r"`[^`]*`(?:_{1,2}|__)")
DIRECTIVE_LINE_RE = re.compile(r"^\s*\.\.\s+\S+::")
UNDERLINE_RE = re.compile(r"^[=\-~^\"'`#*+.:_]{3,}\s*$")


def load_glossary_terms(source_dir):
    """Parse the term names out of the .. glossary:: block. A run of
    consecutive un-indented lines under the directive are alternate names
    for one definition, so each is independently a valid :term: target."""
    path = os.path.join(source_dir, GLOSSARY_PATH)
    terms = []
    in_glossary = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            if ".. glossary::" in line:
                in_glossary = True
                continue
            if not in_glossary:
                continue
            if line.strip().startswith(":"):
                continue  # directive option, e.g. :sorted:
            m = TERM_LINE_RE.match(line.rstrip("\n"))
            if m and not line.startswith("    "):
                candidate = m.group(1).strip()
                if candidate and not candidate.endswith("."):
                    terms.append(candidate)
    return terms


LITERAL_BLOCK_START_RE = re.compile(r"^(\s*)\.\.\s+(code|code-block|literalinclude|math)::")
LITERAL_MARKER_RE = re.compile(r"::\s*$")


def _indent_of(line):
    return len(line) - len(line.lstrip(" "))


def strip_unlinkable_regions(text):
    """Blank out code spans, existing roles/links, directive lines,
    section-title/underline lines, and multi-line literal/code blocks so
    term matches inside them are ignored. Blanking (not deleting) keeps
    line/column positions stable."""
    text = CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)
    text = BOLD_RE.sub(lambda m: " " * len(m.group(0)), text)
    text = OTHER_ROLE_RE.sub(lambda m: " " * len(m.group(0)), text)
    text = EXTERNAL_LINK_RE.sub(lambda m: " " * len(m.group(0)), text)

    lines = text.split("\n")
    out = []
    prev_nonblank = ""
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        starts_literal = LITERAL_BLOCK_START_RE.match(line) or (
            line.strip() and LITERAL_MARKER_RE.search(line) and not line.lstrip().startswith("..")
        )
        if DIRECTIVE_LINE_RE.match(line):
            out.append("")
            base_indent = _indent_of(line)
            i += 1
            # Blank the directive's own option/body lines (e.g. :align:,
            # a caption) up to and including the block's indented content,
            # since none of it is prose a reader sees as a term mention.
            if LITERAL_BLOCK_START_RE.match(line):
                # skip the blank line(s) separating the directive from its body
                while i < n and not lines[i].strip():
                    out.append(lines[i])
                    i += 1
                while i < n and (not lines[i].strip() or _indent_of(lines[i]) > base_indent):
                    out.append("")
                    i += 1
            continue
        if starts_literal and i + 1 < n:
            base_indent = _indent_of(line)
            out.append(line)
            i += 1
            while i < n and not lines[i].strip():
                out.append(lines[i])
                i += 1
            if i < n and _indent_of(lines[i]) > base_indent:
                body_indent = _indent_of(lines[i])
                while i < n and (not lines[i].strip() or _indent_of(lines[i]) >= body_indent):
                    out.append("")
                    i += 1
            continue
        if UNDERLINE_RE.match(line) and prev_nonblank:
            out.append("")  # blank the underline
            out[-2] = ""  # and the title line above it
        else:
            out.append(line)
        if line.strip():
            prev_nonblank = line
        i += 1
    return "\n".join(out)


def find_unlinked_first_mentions(filetext, terms):
    cleaned = strip_unlinkable_regions(filetext)
    findings = []
    for term in terms:
        escaped = re.escape(term)
        # Either a :term: role targeting this exact canonical term (plain
        # form ``:term:`Term``` or display-text form
        # ``:term:`display <Term>```), OR a bare word-boundary mention.
        # Alternation + a single .search() naturally prefers whichever
        # starts earlier in the text; if both could start at the same
        # point the role alternative (listed first) wins, which is correct
        # since the bare mention is entirely inside the role's own span.
        pattern = re.compile(
            r"(?P<role>:term:`(?:[^`<]*<\s*" + escaped + r"\s*>|" + escaped + r")`)"
            r"|(?P<bare>\b" + escaped + r"\b)",
            re.IGNORECASE,
        )
        m = pattern.search(cleaned)
        if m and m.lastgroup == "bare":
            findings.append((m.start(), term, m.group(0)))
    findings.sort(key=lambda t: t[0])
    return findings


def check_file(path, terms):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    findings = find_unlinked_first_mentions(text, terms)
    if findings:
        line_no = text.count("\n", 0, findings[0][0]) + 1
        print(f"{path}")
        for _, term, matched_text in findings:
            print(f"  possibly-unlinked first mention of '{term}': \"{matched_text}\"")
    return len(findings)


def iter_rst_files(source_dir):
    for root, _dirs, files in os.walk(source_dir):
        for name in files:
            if not name.endswith(".rst"):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, source_dir)
            if rel == GLOSSARY_PATH or rel in EXCLUDED_FILES:
                continue
            yield full


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Path to docs/source")
    parser.add_argument(
        "--file",
        action="append",
        dest="files",
        help="Check only this file (repeatable). Path relative to source or absolute.",
    )
    args = parser.parse_args()

    terms = load_glossary_terms(args.source)
    if not terms:
        print("Could not find any glossary terms -- check GLOSSARY_PATH.", file=sys.stderr)
        return 2

    if args.files:
        targets = []
        for f in args.files:
            targets.append(f if os.path.isabs(f) else os.path.join(args.source, f))
    else:
        targets = list(iter_rst_files(args.source))

    total = 0
    for path in sorted(targets):
        total += check_file(path, terms)

    if total:
        print(f"\n{total} possibly-unlinked first mention(s) found across {len(targets)} file(s).")
        print("This is advisory only -- verify each one actually matches the glossary's")
        print("sense of the word before adding a :term: link. Exiting 0 regardless.")
    else:
        print(f"No unlinked glossary terms found across {len(targets)} file(s) checked.")

    return 0  # advisory: never fails the build


if __name__ == "__main__":
    sys.exit(main())
