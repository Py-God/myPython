Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam,
(['cat', 'rat', 'elephant'],)
spam
['cat', 'rat', 'elephant']

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
['bat', 'rat', 'cat', 'hat', 'cat']

del spam[1]
spam
['bat', 'cat', 'hat', 'cat']
