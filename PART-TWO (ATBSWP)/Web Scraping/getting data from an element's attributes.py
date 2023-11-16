import bs4

soup = bs4.BeautifulSoup(open('C:\\Users\\user\\Desktop\\PYTHON\\PART-TWO (ATBSWP)\\Web Scraping\\example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
'<span id="author">Al Sweigart</span>'
spanElem.get('id')
'author'
spanElem.get('some_nonexistent_addr') == None
True
spanElem.attrs
{'id': 'author'}
