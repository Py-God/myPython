import zipfile, os

os.chdir('C:\\')    # move to the folder with example.zip
deliciousZip = zipfile.ZipFile('bacon_backup\\delicious.zip') # opened zipfile
deliciousZip.namelist() # returns list of files and folders in the opened zipfile
['delicious/', 'delicious/cats/', 'delicious/cats/catnames.txt', 'delicious/cats/zophie.jpg', 'delicious/spam.txt']
spamInfo = deliciousZip.getinfo('delicious/spam.txt') # initialized to get info about the file,
                    # various infos can be gotten after this initialization, remember this is saved to a new variable
spamInfo.file_size
8
spamInfo.compress_size
8
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
'Compressed file is 1.0x smaller!'
deliciousZip.close()
