Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
mo1.group()
'Batman'
mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()
'Batwoman'
mo3 = batRegex.search('The adventures of Batwowowowowoman')
mo3.group()
'Batwowowowowoman'
