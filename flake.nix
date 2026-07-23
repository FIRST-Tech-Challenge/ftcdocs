{
  description = "Reproducible build environment for FTC Docs (Sphinx + LaTeX/PDF booklets)";

  inputs = {
    # Pinned to nixos-25.05 because it is the newest release branch that still ships
    # Sphinx 8.2.3 for Python 3.11 (nixpkgs-unstable has since moved to Sphinx 9.x,
    # which drops Python 3.11 support). Bump this once the repo moves off Python 3.11.
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
        py = python.pkgs;

        # ----------------------------------------------------------------------
        # FIRST-Tech-Challenge/ftcdocs-helper
        #
        # Several Sphinx extensions used by this site (dark mode theme, the
        # Java API doc builder, the cookie banner, Google Analytics glue, and
        # the linkcheck-diff builder) live in this companion repo and were
        # previously installed with
        #   pip install git+https://github.com/.../ftcdocs-helper@main#subdirectory=<name>
        # i.e. always tracking the tip of `main`. For a reproducible flake we
        # pin to a specific commit instead. Bump `ftcdocsHelperRev` (and the
        # hash, which `nix build` will report on mismatch) when a new helper
        # release is needed.
        # ----------------------------------------------------------------------
        ftcdocsHelperRev = "5fa0c07f1a6670bc4df84d072ba955380d09f280";
        ftcdocsHelperSrc = pkgs.fetchFromGitHub {
          owner = "FIRST-Tech-Challenge";
          repo = "ftcdocs-helper";
          rev = ftcdocsHelperRev;
          hash = "sha256-uZpCb61P1mBt+/CN7uTgQg6Syk9tmKBTxjZP95YtYRI=";
        };

        # ----------------------------------------------------------------------
        # Plain-PyPI packages pinned to the exact versions previously listed in
        # docs/requirements.txt but not (yet) packaged in nixpkgs/25.05.
        # ----------------------------------------------------------------------
        javalang = py.buildPythonPackage {
          pname = "javalang";
          version = "0.13.0";
          format = "setuptools";
          src = pkgs.fetchPypi {
            pname = "javalang";
            version = "0.13.0";
            hash = "sha256-FoGlpIClgRbUKn7t/RMqviXmwP/lUoaNWBrYTmqjQkw=";
          };
          propagatedBuildInputs = [ py.six ];
          doCheck = false;
        };

        pythonGitInfo = py.buildPythonPackage {
          pname = "python-git-info";
          version = "0.8.3";
          format = "setuptools";
          src = pkgs.fetchPypi {
            pname = "python-git-info";
            version = "0.8.3";
            hash = "sha256-wIonZKFtoCnk25CauENq5IT4hGQF+Dsbz9QV/l46sw0=";
          };
          doCheck = false;
        };

        sphinxDesign = py.buildPythonPackage {
          pname = "sphinx_design";
          version = "0.7.0";
          format = "pyproject";
          src = pkgs.fetchPypi {
            pname = "sphinx_design";
            version = "0.7.0";
            hash = "sha256-0qP1sZwkuRattS+XxfAO+rQAnKM3gSABEJCEp0Dsm3o=";
          };
          nativeBuildInputs = [ py.flit-core ];
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        sphinxAutobuild = py.buildPythonPackage {
          pname = "sphinx_autobuild";
          version = "2024.2.4";
          format = "pyproject";
          src = pkgs.fetchPypi {
            pname = "sphinx_autobuild";
            version = "2024.2.4";
            hash = "sha256-y50hIaF21i1FRxYkhyr8X613Va1mJzir5ADs9KeVQwM=";
          };
          nativeBuildInputs = [ py.flit-core ];
          propagatedBuildInputs = [
            py.sphinx
            py.livereload
            py.colorama
          ];
          doCheck = false;
        };

        sphinxSitemap = py.buildPythonPackage {
          pname = "sphinx-sitemap";
          version = "2.3.0";
          format = "setuptools";
          src = pkgs.fetchPypi {
            pname = "sphinx-sitemap";
            version = "2.3.0";
            hash = "sha256-eye12fbr91WX2n1Ixk3LknH6JpklZz2QDuJ9ayxISRU=";
          };
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        sphinxcontribMermaid = py.buildPythonPackage {
          pname = "sphinxcontrib-mermaid";
          version = "0.9.2";
          format = "setuptools";
          src = pkgs.fetchPypi {
            pname = "sphinxcontrib-mermaid";
            version = "0.9.2";
            hash = "sha256-JS7xPdIxZLKPFtiwIFzxhLnY4rcUowInTZ9Z63COd68=";
          };
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        sphinxHoverxref = py.buildPythonPackage {
          pname = "sphinx-hoverxref";
          version = "1.3.0";
          format = "pyproject";
          src = pkgs.fetchPypi {
            pname = "sphinx-hoverxref";
            version = "1.3.0";
            hash = "sha256-5RfatMuBhtpY14xTeBRZ7hEW7JyEE1gMfcQ+EkxfMXc=";
          };
          nativeBuildInputs = [ py.flit-core ];
          propagatedBuildInputs = [
            py.sphinx
            py.sphinxcontrib-jquery
          ];
          doCheck = false;
        };

        sphinxNotfoundPage = py.buildPythonPackage {
          pname = "sphinx-notfound-page";
          version = "1.1.0";
          format = "pyproject";
          src = pkgs.fetchPypi {
            pname = "sphinx_notfound_page";
            version = "1.1.0";
            hash = "sha256-kT4XVDcLs9sgHZMA1FiouLX7IukkaoFmQ6gZqeorgGc=";
          };
          nativeBuildInputs = [ py.flit-core ];
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        # ----------------------------------------------------------------------
        # ftcdocs-helper subpackages (see comment above ftcdocsHelperSrc).
        # ----------------------------------------------------------------------
        javasphinx = py.buildPythonPackage {
          pname = "javasphinx";
          version = "0.9.15";
          format = "setuptools";
          src = "${ftcdocsHelperSrc}/javasphinx";
          propagatedBuildInputs = [
            javalang
            py.lxml
            py.beautifulsoup4
            py.future
            py.docutils
            py.sphinx
          ];
          doCheck = false;
        };

        cookiebanner = py.buildPythonPackage {
          pname = "sphinxcontrib-cookiebanner";
          version = "0.1";
          format = "setuptools";
          src = "${ftcdocsHelperSrc}/cookiebanner";
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        googleanalytics = py.buildPythonPackage {
          pname = "sphinxcontrib-googleanalytics";
          version = "0.2";
          format = "setuptools";
          src = "${ftcdocsHelperSrc}/googleanalytics";
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        sphinxRtdDarkMode = py.buildPythonPackage {
          pname = "sphinx_rtd_dark_mode";
          version = "1.4.0";
          format = "setuptools";
          src = "${ftcdocsHelperSrc}/sphinx_rtd_dark_mode_v2";
          propagatedBuildInputs = [ py.sphinx-rtd-theme ];
          doCheck = false;
        };

        linkcheckdiff = py.buildPythonPackage {
          pname = "ftcdocs-linkcheckdiff";
          version = "0.1.0";
          format = "pyproject";
          src = "${ftcdocsHelperSrc}/linkcheckdiff";
          nativeBuildInputs = [ py.setuptools ];
          propagatedBuildInputs = [ py.sphinx ];
          doCheck = false;
        };

        # ----------------------------------------------------------------------
        # The Python environment Sphinx runs in: Sphinx itself (from nixpkgs,
        # pinned to 8.2.3 via the nixos-25.05 input above) plus every extension
        # docs/source/conf.py loads, matching docs/requirements.txt 1:1. The
        # only requirements.txt entry intentionally dropped is the `make` PyPI
        # package -- that was a Windows-only shim so `make` works without
        # installing GNU Make separately; this flake provides real GNU Make
        # via pkgs.gnumake instead.
        # ----------------------------------------------------------------------
        ftcdocsPython = python.withPackages (
          ps: with ps; [
            sphinx
            sphinxAutobuild
            javasphinx
            sphinxRtdDarkMode
            sphinxDesign
            googleanalytics
            cookiebanner
            sphinxSitemap
            pythonGitInfo
            sphinxcontribMermaid
            sphinxHoverxref
            sphinxext-rediraffe
            sphinxNotfoundPage
            linkcheckdiff
          ]
        );

        # OS-level packages needed for the LaTeX/PDF "booklets" build. This
        # replaces the top-level `dependencies` file (texlive-xetex, latexmk,
        # fonts-roboto). We use the full TeX Live scheme rather than hand-picking
        # individual LaTeX packages: docs/source/conf.py's latex_elements preamble
        # pulls in a fair number of packages (fancyhdr, titlesec, datetime2,
        # eso-pic, ...) and a full scheme is the simplest way to guarantee the
        # xelatex build keeps working as that preamble evolves, at the cost of a
        # larger closure/first download.
        texliveEnv = pkgs.texlive.combine { inherit (pkgs.texlive) scheme-full; };

        docsPackages = [
          ftcdocsPython
          pkgs.gnumake
          pkgs.git
          texliveEnv
          pkgs.roboto
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          packages = docsPackages;
          shellHook = ''
            echo "FTC Docs dev shell ready."
            echo "  make -C docs html       # build the HTML site"
            echo "  make -C docs autobuild  # live-reloading local server"
            echo "  make -C docs booklets   # build the PDF booklets (needs LaTeX)"
          '';
        };

        # `nix build` / `nix profile install` target with the same tool set as
        # the devShell, for use in CI and container images without needing
        # `nix develop`.
        packages.default = pkgs.buildEnv {
          name = "ftcdocs-env";
          paths = docsPackages;
        };
      }
    );
}
