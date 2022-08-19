import glob 
import os
from tqdm import tqdm
from PIL import Image

for image in (pbar := tqdm(glob.glob("**/*.png", recursive = True))):
    im1 = Image.open(image)
    im1.save(image.replace(".webp", ".png"), "PNG")
