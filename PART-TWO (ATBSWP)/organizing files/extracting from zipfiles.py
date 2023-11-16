import zipfile, os

os.chdir('C:\\bacon_backup')
deliciousZip = zipfile.ZipFile('delicious.zip')
deliciousZip.extractall()
deliciousZip.close()
# i have closed it here, i need to open it again
deliciousZip = zipfile.ZipFile('delicious.zip')
deliciousZip.extract('delicious/spam.txt')
'C:\\bacon_backup\\delicious\\spam.txt'
deliciousZip.extract('delicious/spam.txt', 'C:\\some\\new\\folders')    # creating the folders you dont have to extract to
'C:\\some\\new\\folders\\delicious\\spam.txt'
