# Image for local development (dev container / Codespaces).
# Includes everything required to build the docs and run the tests,
# except for what is installed by uv (Python and the Python packages)
FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

COPY dependencies /tmp/dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        make \
        nodejs \
        npm \
    && xargs -a /tmp/dependencies apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* /tmp/dependencies

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Pre-install the interpreter uv.lock pins (requires-python == 3.11.*) so the
# first `uv sync` in a fresh container does not pay for the download.
RUN uv python install 3.11

RUN npm install -g cspell@8

ENV UV_LINK_MODE=copy

# Keep the project environment off the bind-mounted workspace.
ENV UV_PROJECT_ENVIRONMENT=/opt/ftcdocs-venv

RUN git config --system --add safe.directory '*'

WORKDIR /workspace
