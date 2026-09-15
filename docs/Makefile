# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

SIZECHECKER   = uv run -m scripts.imagesizechecker
CONFEXCLUDE   = --exclude-file source/conf.py
SIZEMAX       = 500

GLOSSARYCHECKER = uv run -m scripts.glossarychecker

AUTOBUILD = uv run sphinx-autobuild
HTMLBUILDDIR = build/html
LATEXBUILDDIR = build/latex/
BOOKLETSBUILDDIR = build/booklets

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

setup:
	@echo "Python dependencies are managed by uv, from pyproject.toml/uv.lock:"
	@echo
	@echo "  uv sync        # run from the repository root"
	@echo
	@echo "Every target here already invokes Sphinx through 'uv run', so no"
	@echo "shell activation is needed. PDF targets (booklets, local-full,"
	@echo "latexpdf) additionally need the LaTeX toolchain, which uv cannot"
	@echo "install -- see the root 'dependencies' file, or use the dev"
	@echo "container in .devcontainer/ which has it preinstalled."
	@echo "The 'scripts' group (uv sync --group scripts) is only needed by"
	@echo "convertWebp.py and convert_md_to_rst.py, not by any target here."

autobuild:
	@$(AUTOBUILD) $(SOURCEDIR) $(HTMLBUILDDIR) --port=7350

--move-booklets:
	mkdir -p $(BOOKLETSBUILDDIR)
	cp $(addsuffix .pdf, $(basename $(wildcard $(LATEXBUILDDIR)*.tex))) $(BOOKLETSBUILDDIR)

--generate-booklets:
	BOOKLETS_BUILD="true" $(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)

booklets: --generate-booklets --move-booklets
	
local-full:
	DOCS_BUILD="true" $(SPHINXBUILD) -b html $(SOURCEDIR) $(HTMLBUILDDIR) $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)
	cp $(LATEXBUILDDIR)*.pdf $(HTMLBUILDDIR)

imagecheck:
	@$(SIZECHECKER) $(SOURCEDIR) $(SIZEMAX) $(CONFEXCLUDE) $(O)

glossarycheck:
	@$(GLOSSARYCHECKER) $(SOURCEDIR) $(O)

.PHONY: help autobuild imagecheck glossarycheck Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
