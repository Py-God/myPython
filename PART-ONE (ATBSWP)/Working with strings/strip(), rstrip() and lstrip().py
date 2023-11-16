Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = '    Hello world!    '
spam.strip()
'Hello world!'
spam.lstrip()
'Hello world!    '
spam.rstrip()
'    Hello world!'

spam = 'SpamSpamBconSpamEggsSpamSpam'
spam.strip('ampS')
'BconSpamEggs'
