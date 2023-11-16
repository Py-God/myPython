import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\PYTHON\\example.xlsx')

wb.sheetnames
['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb.get_sheet_by_name('Sheet3')
sheet
<Worksheet "Sheet3">
type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
sheet.title
'Sheet3'
anotherSheet = wb.active
anotherSheet
<Worksheet "Sheet1">
