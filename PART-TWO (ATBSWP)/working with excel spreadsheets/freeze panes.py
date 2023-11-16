Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import openpyxl
wb = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\PYTHON\\produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'
wb.save('C:\\Users\\user\\Desktop\\PYTHON\\freezeExample.xlsx')
