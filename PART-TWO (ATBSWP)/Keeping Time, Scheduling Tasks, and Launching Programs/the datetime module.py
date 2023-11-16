Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import datetime
datetime.datetime.now()
datetime.datetime(2022, 7, 20, 23, 19, 30, 920570)
dt = datetime.datetime(2022, 7, 20, 23, 19, 30, 0)
dt.year, dt.month, dt.day
(2022, 7, 20)
dt.hour, dt.minute, dt.second
(23, 19, 30)

datetime.datetime.fromtimestamp(1000000)
datetime.datetime(1970, 1, 13, 2, 46, 40)
datetime.datetime.fromtimestamp(time.time())
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    datetime.datetime.fromtimestamp(time.time())
NameError: name 'time' is not defined
import time
datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2022, 7, 20, 23, 24, 49, 262058)

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
halloween2015 == oct31_2015
True
halloween2015 > newyears2016
False
newyears2016 > halloween2015
True
newyears2016 != oct31_2015
True
