#! python3
# this program opens all txt files in a particular folder in read mode
# searches for a regex in all of them at once
import re, os

search = input('input your search: ')
regex = re.compile(r'{}'.format(search))

files = os.listdir('C:\\Users\\user\\Desktop\\PYTHON\\regexsearchfolder')
for i in files:
    individualFilePath = os.path.join('C:\\Users\\user\\Desktop\\PYTHON\\regexsearchfolder', i)
    print(individualFilePath)
    for paths in individualFilePath:
        file = open(individualFilePath, 'r')
        matches = regex.findall(file.read())
        for match in matches:
            ''.join(match)
    print(matches)
