from PIL import Image, ImageDraw, ImageFont
import os

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 50), 'Howdy', fill='gray', font=arialFont)
im.save('C:\\Users\\user\\Desktop\\PYTHON\\text.png')
