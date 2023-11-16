Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
catIm = Image.open('zophie.png')
catIm.rotate(90).save('C:\\Users\\user\\Desktop\\PYTHON\\rotated90.png')
catIm.rotate(180).save('C:\\Users\\user\\Desktop\\PYTHON\\rotated180.png')
catIm.rotate(270).save('C:\\Users\\user\\Desktop\\PYTHON\\rotated270.png')
catIm.rotate(6).save('C:\\Users\\user\\Desktop\\PYTHON\\rotated6.png')
catIm.rotate(6, expand=True).save('C:\\Users\\user\\Desktop\\PYTHON\\rotated270_expanded.png')
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('C:\\Users\\user\\Desktop\\PYTHON\\horizontal_flip.png')

Warning (from warnings module):
  File "<pyshell#7>", line 1
DeprecationWarning: FLIP_LEFT_RIGHT is deprecated and will be removed in Pillow 10 (2023-07-01). Use Transpose.FLIP_LEFT_RIGHT instead.
catIm.transpose.FLIP_LEFT_RIGHT.save('C:\\Users\\user\\Desktop\\PYTHON\\horizontal_flip.png')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    catIm.transpose.FLIP_LEFT_RIGHT.save('C:\\Users\\user\\Desktop\\PYTHON\\horizontal_flip.png')
AttributeError: 'function' object has no attribute 'FLIP_LEFT_RIGHT'
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('C:\\Users\\user\\Desktop\\PYTHON\\horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('C:\\Users\\user\\Desktop\\PYTHON\\vertical_flip.png')

Warning (from warnings module):
  File "<pyshell#10>", line 1
DeprecationWarning: FLIP_TOP_BOTTOM is deprecated and will be removed in Pillow 10 (2023-07-01). Use Transpose.FLIP_TOP_BOTTOM instead.
