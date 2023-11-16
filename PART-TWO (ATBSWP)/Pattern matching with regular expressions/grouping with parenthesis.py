Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-5555-4242.')
mo.group(1)
'415'
mo.group(2)
'5555'
mo.group(0)
'415-5555'
mo.group()
'415-5555'

mo.groups()
('415', '5555')
areaCode, mainNumber = mo.groups()
print(areaCode)
415
print(mainNumber)
5555

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
'(415)'
mo.group(2)
'555-4242'
