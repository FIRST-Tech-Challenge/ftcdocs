import glob 
import os
from tqdm import tqdm

for markdown in (pbar := tqdm(glob.glob("**/*.md", recursive = True))):
    pbar.set_postfix_str(f"Converting {markdown}")
    filename = markdown.replace(".md", ".rst")
    os.system(f'pandoc --to=rst --output=\"{filename}\" \"{markdown}\"')
