import glob 
import os
from PIL import Image

for image in glob.glob("**/*.gif", recursive = True):
    im1 = Image.open(image)
    im1.save(image.replace(".gif", ".png"), "PNG")
    os.remove(image)
