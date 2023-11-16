Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'bat', 'rat']
size,color,disposition = cat
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    size,color,disposition = cat
NameError: name 'cat' is not defined
size,color,disposition = spam
spam
['cat', 'bat', 'rat']
size
'cat'
color
'bat'
disposition
'rat'
# you are assigning the values of cat to size,color,disposition. cat would remain the same 