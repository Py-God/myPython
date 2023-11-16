Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam
['A', 'B', 'C', 'D']
cheese
['A', 42, 'C', 'D']
# spam and cheese variables now refer to seperate lists because they carry sepe-rate indexes
