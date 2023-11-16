Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
catIm = Image.open('zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('C:\\Users\\user\\Desktop\\PYTHON\\cropped.png')
