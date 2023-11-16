Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
helloFile = open('C:\\Users\\user\\hello.txt', 'r')
helloContent = helloFile.read()
helloContent
'Hello World!'

sonnetFile = open('C:\\Users\\user\\sonnet29.txt')
sonnetFile.readlines()
["when, in disgrace with fortune and men's eyes,\n", 'i all alone beweep my outcast state,\n', 'and trouble deaf heaven with my bootless cries,\n', 'and i look upon myself and curse my fate,']
