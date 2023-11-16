import shutil, os

os.chdir('C:\\')
shutil.copy('C:\\Games\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
shutil.copy('Games\\eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'

shutil.copy('C:\\Games\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
shutil.copy('Games\\eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'

shutil.copytree('bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'
