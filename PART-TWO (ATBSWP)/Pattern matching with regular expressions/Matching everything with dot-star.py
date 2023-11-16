Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Boluwatife Last Name: Leke-Oduoye')
mo.group(1)
'Boluwatife'
mo.group(2)
'Leke-Oduoye'

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man> for dinner.>'

# match an opening angle bracket, then anything, then a closing angle bracket.  For python to choose where to stop, use either the greedy or non greedy method