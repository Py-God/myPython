import docx

doc = docx.Document('C:\\Users\\user\\Desktop\\PYTHON\\twoPage.docx')
doc.add_picture('C:\\Users\\user\\Desktop\\PYTHON\\zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))
'''<docx.shape.InlineShape object at 0x000002472FC9CD60>'''
doc.save('C:\\Users\\user\\Desktop\\PYTHON\\picture.docx')
