from PIL import Image

catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width/2), int(height/2)))
quartersizedIm.save('C:\\Users\\user\\Desktop\\PYTHON\\quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('C:\\Users\\user\\Desktop\\PYTHON\\svelte.png')
