import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
<class 'bs4.BeautifulSoup'>

# This code uses requests.get() to download the main page from the No Starch Press website
# and then passes the text attribute of the response to bs4.BeautifulSoup().
# The BeautifulSoup object that it returns is stored in a variable named noStarchSoup.

exampleFile = open('C:\\Users\\user\\Desktop\\PYTHON\\PART-TWO (ATBSWP)\\Web Scraping\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
<class 'bs4.BeautifulSoup'>
