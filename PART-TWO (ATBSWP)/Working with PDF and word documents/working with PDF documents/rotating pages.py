import PyPDF2

minutesFile = open('C:\\Users\\user\\Desktop\\PYTHON\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
'''{'/Contents': [IndirectObject(961, 0, 2233212853488), IndirectObject(962, 0, 2233212853488), IndirectObject(963, 0, 2233212853488), IndirectObject(964, 0, 2233212853488), IndirectObject(965, 0, 2233212853488), IndirectObject(966, 0, 2233212853488), IndirectObject(967, 0, 2233212853488), IndirectObject(968, 0, 2233212853488)], '/CropBox': [0, 0, 612, 792], '/MediaBox': [0, 0, 612, 792], '/Parent': IndirectObject(953, 0, 2233212853488), '/Resources': {'/ColorSpace': {'/CS0': IndirectObject(975, 0, 2233212853488), '/CS1': IndirectObject(976, 0, 2233212853488), '/CS2': IndirectObject(976, 0, 2233212853488)}, '/ExtGState': {'/GS0': IndirectObject(977, 0, 2233212853488)}, '/Font': {'/TT0': IndirectObject(979, 0, 2233212853488), '/TT1': IndirectObject(981, 0, 2233212853488), '/TT2': IndirectObject(983, 0, 2233212853488), '/TT3': IndirectObject(985, 0, 2233212853488), '/TT4': IndirectObject(987, 0, 2233212853488), '/TT5': IndirectObject(989, 0, 2233212853488)}, '/XObject': {'/Im0': IndirectObject(973, 0, 2233212853488)}}, '/Rotate': 90, '/StructParents': 0, '/Type': '/Page'}'''

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('C:\\Users\\user\\Desktop\\PYTHON\\rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
