import re

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')
matches = regex.findall('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
matches
[('ADJECTIVE', '', ''), ('', 'NOUN', ''), ('', '', 'VERB'), ('', 'NOUN', '')]

for i in matches:
    for j in i:
        print(j)


ADJECTIVE



NOUN



VERB

NOUN


for i in matches:
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            print(reg)


re.compile('ADJECTIVE')
re.compile('NOUN')
re.compile('VERB')
re.compile('NOUN')
