Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
<class 'requests.models.Response'>
res.status_code == requests.codes.ok
True
len(res.text)
178978
print(res.text[:250])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Projec
romeoAndJuliet = file.open('Romeo_and_juliet.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    romeoAndJuliet = file.open('Romeo_and_juliet.txt', 'w')
NameError: name 'file' is not defined. Did you mean: 'filter'?
romeoAndJuliet = open('Romeo_and_juliet.txt', 'w')
romeoAndJuliet.write(res.text[:])
178978
romeoAndJuliet.close()
