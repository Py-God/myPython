Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
for i in range(3):
    print('tick')
    time.sleep(1)
    print('tock')
    time.sleep(1)

    
tick
tock
tick
tock
tick
tock
time.sleep(5)
