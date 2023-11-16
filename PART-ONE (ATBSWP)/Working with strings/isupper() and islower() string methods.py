Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = 'Hello world!'
spam.islower()
False
spam.isupper()
False
'HELLO'.isupper()
True
'abc1231'.islower()
True
'12345'.islower()
False
'12313'.isupper
<built-in method isupper of str object at 0x000001E1B41C8A30>
'1313123'.isupper()
False

'Hello'.upper()
'HELLO'
'Hello'.upper().lower()
'hello'
'Hello'.upper().lower().upper()
'HELLO'
'HELLO'.lower()
'hello'
'HELLO'.lower().islower()
True
