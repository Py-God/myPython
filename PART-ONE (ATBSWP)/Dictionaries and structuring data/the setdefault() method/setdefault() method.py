Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
spam.setdefault('color', 'white')
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
# the value of the key is not changed to white because spam already has a key named color