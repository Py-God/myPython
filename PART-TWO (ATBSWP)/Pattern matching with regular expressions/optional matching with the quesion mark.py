Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo1.group()
'Batman'
mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()
'Batwoman'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
'415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
'555-4242'

questionMarkRegex = re.compile(r'(\d\d\d)\?\d\d\d-\d\d\d\d')
mo5 = questionMarkRegex.search('My phone number is 415?333-1212')
mo5.group()
'415?333-1212'
