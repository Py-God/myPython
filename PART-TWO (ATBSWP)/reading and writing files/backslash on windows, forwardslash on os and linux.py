import os

path = os.path.join('usr', 'bin', 'spam')
print(path)                                 # there was double slash because windows added its own. in os and linus it'll be a single slash

print('--------------')
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\user\\Desktop', filename))           # notice the doubleslash?