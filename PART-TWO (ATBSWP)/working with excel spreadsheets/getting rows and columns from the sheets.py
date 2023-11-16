import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\PYTHON\\example.xlsx')
sheet = wb['Sheet1']
tuple(sheet['A1':'C3'])
'''((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))'''

for rowOfCellObjects in sheet['A1': 'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('---- END OF ROW ----')

'''
A1 2015-04-05 13:34:02
B1 Apples
C1 73
---- END OF ROW ----
A2 2015-04-05 03:41:23
B2 Cherries
C2 85
---- END OF ROW ----
A3 2015-04-06 12:46:51
B3 Pears
C3 14
---- END OF ROW ----
'''

sheet['A1': 'C1']
'''((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),)'''
sheet['A1': 'C3']
'''((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))'''
# , our slice of the sheet contains all the Cell objects in the area from A1 to C3, starting from the top-left cell and ending with the bottom-right cell.


sheet = wb.active

sheet['A']
'''(<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>, <Cell 'Sheet1'.A3>, <Cell 'Sheet1'.A4>, <Cell 'Sheet1'.A5>, <Cell 'Sheet1'.A6>, <Cell 'Sheet1'.A7>)'''
for cellObj in sheet['A']:
    print(cellObj.value)

'''
2015-04-05 13:34:02
2015-04-05 03:41:23
2015-04-06 12:46:51
2015-04-08 08:59:43
2015-04-10 02:07:00
2015-04-10 18:10:37
2015-04-10 02:40:46
'''
for cellObj in sheet['B']:
    print(cellObj.value)

'''
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
'''