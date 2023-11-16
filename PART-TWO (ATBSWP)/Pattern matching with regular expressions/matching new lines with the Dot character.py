Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public trust \nProtect the innocent. \nUphold the law.').group()
'Serve the public trust '

newLineRegex = re.compile('.*', re.DOTALL)
newLineRegex.search('Serve the public trust \nProtect the innocent. \nUphold the law.').group()
'Serve the public trust \nProtect the innocent. \nUphold the law.'
