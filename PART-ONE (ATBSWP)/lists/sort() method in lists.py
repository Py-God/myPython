Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
[-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse = True)
spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
spam = [1,2,3,4, 'Alice', 'Bob']
spam.sort
<built-in method sort of list object at 0x000001544AA78100>
spam.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'

spam = ['Alice', 'ants', 'Bob', 'badgers', 'carol', 'cats']
spam.sort()
spam
['Alice', 'Bob', 'ants', 'badgers', 'carol', 'cats']

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam
['a', 'A', 'z', 'Z']
