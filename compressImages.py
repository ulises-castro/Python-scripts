import os
from PIL import Image

validExtensions = ['jpeg','jpg','gif','png']
imagesNames = os.listdir(os.path.dirname(os.path.realpath(__file__)))
for imageName in imagesNames:
    extension = imageName.split('.')
    extension = extension[len(extension) - 1]
    sizeImage = os.path.getsize(imageName)
    if(sizeImage > 500000 and extension in validExtensions):
        image = Image.open(imageName)
        image.save(imageName, quality=15)
