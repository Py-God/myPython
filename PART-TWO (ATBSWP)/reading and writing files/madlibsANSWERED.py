#! python3
import re

file = open('madlibs.txt', 'w')
file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
file.close()

file = open('madlibs.txt')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')    # either way the regex is, you can still get the same results

for i in regex.findall(text):   # this is the output of regex.findall(text): [('ADJECTIVE', '', ''), ('', 'NOUN', ''), ('', '', 'VERB'), ('', 'NOUN', '')]
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))   # this will return the regex for each and every occurrence of the grammatical function
            # this is the result of print(reg):
            # re.compile('ADJECTIVE')
            # re.compile('NOUN')
            # re.compile('VERB')
            # re.compile('NOUN')

            inp_text = input('Enter the substitute for %s: ' %j)
            text = reg.sub(inp_text, text, 1)   # substituting the grammartical function with the input or 1 if not in the text

print(text)

file = open('madlibs_ans', 'w')
file.write(text)
file.close()