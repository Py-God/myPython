Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = 42
cheese = spam
spam = 100
spam
100
cheese
42
# spam and cheese are different variables that store different values
# lists dont work this way
#   when you assign a list to a variable you are assigning a list reference to the variable
# a reference is a value that points to some bit of data. a list reference points to a list

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
spam
[0, 'Hello!', 2, 3, 4, 5]
# cheese = spam copies the list reference in spam to cheese, not the list value itself; Values stored in spam and cheese now both refer to the same list. the list itself was never actually copied.