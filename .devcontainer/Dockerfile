FROM python:3.8.18-bullseye
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra latexmk texlive-lang-greek texlive-luatex texlive-xetex texlive-fonts-extra dvipng librsvg2-bin git
RUN pip install -r docs/requirements.txt
