Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'Aardvark'
spam
['cat', 'Aardvark', 'rat', 'elephant']
spam[2] = spam[1]
spam
['cat', 'Aardvark', 'Aardvark', 'elephant']
spam[-1] = 12345
spam
['cat', 'Aardvark', 'Aardvark', 12345]
