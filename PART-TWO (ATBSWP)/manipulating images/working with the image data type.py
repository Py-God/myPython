Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
(816, 1088)
width, height = catIm.size
width
816
height
1088
catIm.filename
'zophie.png'
catIm.format
'PNG'
catIm.format_description
'Portable network graphics'
catIm.save('zophie.jpg')

im = image.new('RGBA', (100, 200), 'purple')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    im = image.new('RGBA', (100, 200), 'purple')
NameError: name 'image' is not defined. Did you mean: 'Image'?
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')
