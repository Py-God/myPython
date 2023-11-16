import bs4

exampleFile = open('C:\\Users\\user\\Desktop\\PYTHON\\PART-TWO (ATBSWP)\\Web Scraping\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
<class 'bs4.element.ResultSet'>
len(elems)
1
type(elems[0])
<class 'bs4.element.Tag'>
elems[0].getText()
'Al Sweigart'
str(elems[0])
'<span id="author">Al Sweigart</span>'
elems[0].attrs
{'id': 'author'}

pElems = exampleSoup.select('p')
str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
pElems[0].getText()
'Download my Python book from my website.'
str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
'Learn Python the easy way!'
str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()
'By Al Sweigart'
