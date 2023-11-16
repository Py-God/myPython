Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
', '.join(['cats', 'bats', 'rats'])
'cats, bats, rats'
' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
print('My name is Simon', sep=', ')
My name is Simon
print('My', 'name' 'is' 'Simon', sep = ', ')
My, nameisSimon
print('My', 'name', 'is', 'Simon' sep = ', ')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('My', 'name', 'is', 'Simon', sep = ', ')
My, name, is, Simon

'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
spam = '''Dear Alice'''
spam = '''Dear Alice,
Hpw have you been? I am fine.
There is a container in the fridge
that is labeled mil experiment

please do not drink it
sincerely,
Bob.'''
spam.split('\n')
['Dear Alice,', 'Hpw have you been? I am fine.', 'There is a container in the fridge', 'that is labeled mil experiment', '', 'please do not drink it', 'sincerely,', 'Bob.']
