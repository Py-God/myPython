Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
'cat'
spam[2]
'rat'
spam[3]
'elephant'

'Hello ' + spam[0]
'Hello cat'
'The ' + spam[1] ' ate the ' + spam[0]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
'The ' + spam[1] + ' ate the ' + spam[0]
'The bat ate the cat'
['football', 3.121, None, True, 42]
['football', 3.121, None, True, 42]
spam[1000]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    spam[1000]
IndexError: list index out of range
spam[1.0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers or slices, not float
spam[int(1.0)]
'bat'
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
['cat', 'bat']
spam[0, 1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    spam[0, 1]
TypeError: list indices must be integers or slices, not tuple
spam[0][1]
'bat'
spam[1][4]
50
spam[-1]
[10, 20, 30, 40, 50]
spam[-2]
['cat', 'bat']
spam = [10, 20, 30, 40, 50]
spam[-1]
50
spam[-3]
30
spam[-5] + ' + ' + spam[-3] + '=' + '40'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    spam[-5] + ' + ' + spam[-3] + '=' + '40'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
str(spam[-5]) + ' + ' + str(spam[-3]) + ' = ' + '40'
'10 + 30 = 40'
