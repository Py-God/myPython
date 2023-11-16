#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd creates a folder in the cwd
# exists_ok: prevents the function from throwing an exception if this folder already exists.

while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
        # A few XKCD pages have special content that isn’t a simple image file.  If your selector doesn’t find any elements
        # then soup.select('#comic img') will return a blank list. When that happens, the program can just print
        # an error message and move on without downloading the image by getting a mew link below
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # file named xkcd[imageLink]
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]  # identifies the <a> element with the rel attribute set to prev
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')