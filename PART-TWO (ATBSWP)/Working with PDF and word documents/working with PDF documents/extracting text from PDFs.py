import PyPDF2

pdfFileObj = open('C:\\Users\\user\\Desktop\\PYTHON\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
19
pageObj = pdfReader.getPage(0)
pageObj.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS  \n \nMeeting of March 7, 2014 \n\n \n\n \n\n \n\n  \n \n \n \n \n \n  \n \n\n\nThe Board of Elementary and Secondary Education shall provide leadership and \n\n\ncreate policies for education that expand opportunities for children, empower \n\n\nfamilies and communities, and advance Louisiana in an increasingly \n\n\ncompetitive global market. \n\n BOARD \n \n\nof \nELEMENTARY \nand  \nSECONDARY \n\n\nEDUCATION\n\n \n\n\n '
