Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size
(230, 215)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('C:\\Users\\user\\Desktop\\PYTHON\\pasted.png')

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImwidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

        
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for left in range(0, catImwidth, faceImWidth):
NameError: name 'catImwidth' is not defined. Did you mean: 'catImWidth'?
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

        
0 0
0 215
0 430
0 645
0 860
0 1075
230 0
230 215
230 430
230 645
230 860
230 1075
460 0
460 215
460 430
460 645
460 860
460 1075
690 0
690 215
690 430
690 645
690 860
690 1075
catCopyTwo.save('C:\\Users\\user\\Desktop\\PYTHON\\tiled.png')
