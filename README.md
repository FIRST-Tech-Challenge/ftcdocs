*FIRST* Tech Challenge Documentation Project
==========================================

![Build](https://readthedocs.com/projects/first-tech-challenge-ftcdocs/badge/?version=latest) ![Link-Check](https://github.com/FIRST-Tech-Challenge/ftcdocs/actions/workflows/link-check.yaml/badge.svg)

This GitHub project is a work-in-progress for FTC documentation.

The website is available at https://ftc-docs.firstinspires.org

# Contributing

We are always looking for help improving FTC Docs. For more information on contributing
consult the [contributing section](https://ftc-docs.firstinspires.org/contrib/index.html) in FTC Docs.

# Building Locally

Python dependencies are managed with [uv](https://docs.astral.sh/uv/). With uv installed, run:

```
uv sync
uv run make -C docs html
```

That covers the HTML site and the link/image/glossary checks. 

Generating the PDF booklets requires an additional LaTeX toolchain, which uv cannot install. The
`dependencies` file lists the exact package list needed for Debian/Ubuntu (`xargs -a dependencies sudo apt-get install -y`).
On other platforms, the simplest route to a PDF build is the dev container in `.devcontainer/`, which has the whole toolchain preinstalled.

See the [environment setup guide](https://ftc-docs.firstinspires.org/contrib/tutorials/setup/setup.html)
for more detail.