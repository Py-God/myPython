Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import openpyxl
wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wbFormulas.active
sheet['A3'].value
'=SUM(A1:A2)'

wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = wbDataOnly.active
sheet['A3'].value
500
500
