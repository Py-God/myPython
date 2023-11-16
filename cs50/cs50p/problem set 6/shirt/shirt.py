import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit()
    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit()

    acceptable_formats = ['jpeg', 'jpg', 'png']
    
    file, extension = sys.argv[1].split('.')
    file2, extension2 = sys.argv[2].split('.')
    if extension not in acceptable_formats or extension2 not in acceptable_formats:
        print('Invalid input')
        sys.exit()
        
    if not sys.argv[2].endswith(extension):
        print('Input and output have different extensions')
        sys.exit()
    
    merger()

def merger():
    try:
        image = Image.open(sys.argv[1])
    except PIL.UnidentifiedImageError:
        print(sys.argv[1], 'does not exist')
        sys.exit()

    muppet_image = image.copy()
    shirt_image = Image.open('shirt.png')
    
    resized_image = ImageOps.fit(muppet_image, shirt_image.size)
    
    resized_image.paste(shirt_image, (0,0), shirt_image)
    resized_image.save(sys.argv[2])
    
if __name__ == '__main__':
    main()
