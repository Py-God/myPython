Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam
['cat', 'dog', 'bat', 'moose']

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam
['cat', 'chicken', 'dog', 'bat']

eggs = 'Hello'
eggs.append('sasa')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    eggs.append('sasa')
AttributeError: 'str' object has no attribute 'append'
bacon = 42
bacon.insert(1, 121)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bacon.insert(1, 121)
AttributeError: 'int' object has no attribute 'insert'
