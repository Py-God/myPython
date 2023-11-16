Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Zophie a cat'
name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
newName = name[0:7] + 'the' + name[8:12]
name
'Zophie a cat'
newName
'Zophie the cat'
# name didnt change because strings are immutable

eggs = [1,2,3]
eggs = [4,5,6]
# the list value in eggs isnt changed also but the entirely new list is ovewrit- ing the old list value
# if you wanted to modify the list to 4,5,6
eggs = [1,2,3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(3)
del eggs[1]
eggs.append(5)
eggs.append(6)
eggs
[4, 5, 6]
