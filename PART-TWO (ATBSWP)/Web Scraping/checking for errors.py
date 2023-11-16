Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
'''Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\user\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\models.py", line 1022, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist'''

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

There was a problem: 404 Client Error: Not Found

