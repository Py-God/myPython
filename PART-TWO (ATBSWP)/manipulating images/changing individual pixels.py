Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
(0, 0, 0, 0)
for x in range(100):
    for y in range(50)
    
SyntaxError: expected ':'
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

        
from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

        
im.getpixel((0, 0))
(210, 210, 210, 255)
im.getpixel(0, 50)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    im.getpixel(0, 50)
TypeError: Image.getpixel() takes 2 positional arguments but 3 were given
im.getpixel((0, 50))
(169, 169, 169, 255)
im.save('C:\\Users\\user\\Desktop\\PYTHON\\putPixel.png')
