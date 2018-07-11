import os
from PIL import Image

imagesNames = os.listdir()
for imagename in imagesNames:
    sizeImage = os.path.getsize(imagename)
    if(sizeImage > 700000):
        image = Image.open(imagename)
        image.save(imagename, quality=20, optimize=True)
