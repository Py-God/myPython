Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

    
red
42

for k in spam.keys():
    print(k)

    
color
age

for i in spam.items():
    print(i)

    
('color', 'red')
('age', 42)

spam.keys()
dict_keys(['color', 'age'])
list(spam.keys())
['color', 'age']

# you can use the multiple assignment trick in a for loop to assign the key and values to seperate variables
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('key: ' + k + ' Value: ' + str(v))

    
key: color Value: red
key: age Value: 42

spam.items()
dict_items([('color', 'red'), ('age', 42)])
spam.value()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    spam.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
spam.values()
dict_values(['red', 42])
