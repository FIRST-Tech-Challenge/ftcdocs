*FIRST* Tech Challenge Documentation Project
==========================================

![Build](https://readthedocs.com/projects/first-tech-challenge-ftcdocs/badge/?version=latest) ![Link-Check](https://github.com/FIRST-Tech-Challenge/ftcdocs/actions/workflows/link-check.yaml/badge.svg)

This GitHub project is a work-in-progress for FTC documentation.

The website is available at https://ftc-docs.firstinspires.org

# Contributing

We are always looking for help improving FTC Docs. For more infomration on contributing 
consult the [contributing section](https://ftc-docs.firstinspires.org/contrib/index.html) in FTC Docs.

# Building Locally

This repository provides a [Nix](https://nixos.org) flake with everything needed to build the site
(Python, Sphinx, and the LaTeX toolchain used for PDF booklets). With Nix installed, run:

```
nix develop
make -C docs html
```

See the [environment setup guide](https://ftc-docs.firstinspires.org/contrib/tutorials/setup/setup.html)
for more detail.