## make shirtificate.pdf
## orientation of the pdf should be portrait
## the format of the pdf should be a4
## the top of the pdf should say CS50 Shirtificate as text centered horizontally
## the shirt image should be centered horizontally
## the user's name should be on top of the shirt, in white text
from fpdf import FPDF
        
def main():
    Shirtify(input('Name: '))

def Shirtify(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', '', 15)

    # text
    page_width = pdf.w
    page_height = pdf.h
    
    text1_width = pdf.get_string_width('CS50 Shirtificate')
    text2_width = pdf.get_string_width(name)
    
    x_position1 = (page_width - text1_width)/2
    x_position2 = (page_width - text2_width)/2

    pdf.set_x(x_position1)
    pdf.cell(40, 10, 'CS50 Shirtificate',new_x='LMARGIN', new_y='NEXT', align='C')

    # image
    image = 'shirtificate.png'

    pdf.image(image, page_height/4, 50, page_width/4)
    
    pdf.set_x(x_position2)
    pdf.set_text_color(255,255,255)
    pdf.cell(18, 85, name, new_x='LMARGIN', new_y='NEXT', align='C')
    
    pdf.output('shirtificate.pdf')
    
if __name__ == '__main__':
    main()
