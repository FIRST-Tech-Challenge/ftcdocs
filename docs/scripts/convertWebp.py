import glob 
import os
from PIL import Image

for image in glob.glob("**/*.webp", recursive = True):
    im1 = Image.open(image)
    im1.save(image.replace(".jpeg", ".png"), "PNG")
    os.remove(image)
