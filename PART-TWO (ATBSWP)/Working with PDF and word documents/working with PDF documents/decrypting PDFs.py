import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('C:\\Users\\user\\Desktop\\PYTHON\\encrypted.pdf', 'rb'))

pdfReader.isEncrypted
True
pdfReader.getPage(0)
'''PyPDF2.errors.PdfReadError: File has not been decrypted'''
pdfReader.decrypt('rosebud')
'<PasswordType.OWNER_PASSWORD: 2>'
pageObj = pdfReader.getPage(0)
