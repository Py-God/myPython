Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str(45)
'45'
>>> print('i am '+ str(29) + ' years old.')
i am 29 years old.
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> int('42')
42
>>> int('-99')
-99
>>> int(1.25)
1
>>> int(1.99)
1
>>> float('3.14')
3.14
>>> float('2')
2.0
>>> float(10)
10.0
>>> spam = input()
101
>>> spam
'101'
>>> spam = int(spam)
>>> spam
101
>>> spam * 10/5
202.0
>>> int('22.22')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int('22.22')
ValueError: invalid literal for int() with base 10: '22.22'
>>> int('twelve')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int('twelve')
ValueError: invalid literal for int() with base 10: 'twelve'
>>> int(7.7)
7
>>> int(7.7)+1
8
>>> 42 == '42'
False
>>> 42 == 42.00
True
>>> 42 == 0042.00
True
>>> 