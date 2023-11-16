import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('C:\\bacon_backup\\delicious\\spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.

newZip.close()
