Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['Hello', 'Hi', 'Howdy', 'Heyas']
spam.index('Hello')
0
spam.index('Heyas')
3
spam.index('Howdy Howdy Howdy')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    spam.index('Howdy Howdy Howdy')
ValueError: 'Howdy Howdy Howdy' is not in list

spam = ['Zophie', 'Pooka', 'Fat-Tail', 'Pooka']
spam.index('Pooka')
1
