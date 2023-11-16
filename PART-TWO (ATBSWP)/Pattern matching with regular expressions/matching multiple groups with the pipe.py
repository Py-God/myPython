Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
heroRegex = re.compile(r'Batman|Tina fey')
mo1 = heroRegex.search('Batman and Tina fey')
mo1.group()
'Batman'
mo2 = heroRegex.search('Tina fey and Batman')
mo2.group()
'Tina fey'

mo3 = heroRegex.findall('Batman and Tina fey')
mo3.group()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mo3.group()
AttributeError: 'list' object has no attribute 'group'
mo3
['Batman', 'Tina fey']
' '.join(mo3)
'Batman Tina fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
'Batmobile'
mo.group(1)
'mobile'

pipeCharacterMatch = re.compile(r'bat\|man')
mo4 = pipeCharacterMatch.search('i love calling Batman \'bat|man\'')
mo4.group()
'bat|man'
