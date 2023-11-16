import PyPDF2

minutesFile = open('C:\\Users\\user\\Desktop\\PYTHON\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWaterMarkReader = PyPDF2.PdfFileReader(open('C:\\Users\\user\\Desktop\\PYTHON\\watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWaterMarkReader.getPage(0)) # page with the watermark is passed to the mergepage method

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('C:\\Users\\user\\Desktop\\PYTHON\\watermarkedcover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
