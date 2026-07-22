FROM python:3.9.18-bullseye
WORKDIR /app
COPY . .

# Dependencies for building the docs (Python, Sphinx, and the LaTeX/PDF
# toolchain) are now provided by the Nix flake at the repository root
# instead of apt-get/pip here -- see flake.nix. Install Nix (single-user,
# no daemon, which is the supported mode inside a container) and enable
# flakes so `nix develop` works out of the box.
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl xz-utils ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && curl -L https://nixos.org/nix/install | sh -s -- --no-daemon \
    && mkdir -p /etc/nix \
    && echo "experimental-features = nix-command flakes" >> /etc/nix/nix.conf

ENV PATH="/root/.nix-profile/bin:${PATH}"
