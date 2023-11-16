Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'

robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

robocop.search('Al, Why does your programming book talk about robocop so much?').group()
'robocop'
