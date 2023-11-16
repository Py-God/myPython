Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import bs4
exampleFile = open('C:\\Users\\user\\Desktop\\PYTHON\\PART-TWO (ATBSWP)\\Web Scraping\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
example = exampleSoup.select('head title')
len(example)
1
str(example[0])
'<title>The Website Title</title>'
example[0].getText
<bound method PageElement.get_text of <title>The Website Title</title>>
example = exampleSoup.select('.slogan')
str(example[0])
'<p class="slogan">Learn Python the easy way!</p>'
example[0].getText()
'Learn Python the easy way!'
example[0].get('class')
['slogan']
