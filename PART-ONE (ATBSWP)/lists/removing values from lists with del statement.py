Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
['cat', 'bat', 'elephant']
del spam[2]
spam
['cat', 'bat']
eggs = 12345
dale = 'Ate'
eggs
12345
dale
'Ate'
del eggs
eggs
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    eggs
NameError: name 'eggs' is not defined
