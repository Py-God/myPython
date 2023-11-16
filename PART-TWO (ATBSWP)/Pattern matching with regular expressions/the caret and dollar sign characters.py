Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
<re.Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello') == None
True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
<re.Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two') == None
True

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
<re.Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
True
wholeStringIsNum.search('12 34567890') == None
True
