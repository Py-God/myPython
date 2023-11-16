import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\PYTHON\\example.xlsx')
sheet = wb['Sheet1']
#get a particular column
sheet[1]
'''(<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>)'''
for columnElements in sheet[1]:
    print(columnElements.value)

'''
2015-04-05 13:34:02
Apples
73
'''
# get all the column values

sheet['A1':'C7']
'''((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>), (<Cell 'Sheet1'.A4>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.C4>), (<Cell 'Sheet1'.A5>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.C5>), (<Cell 'Sheet1'.A6>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.C6>), (<Cell 'Sheet1'.A7>, <Cell 'Sheet1'.B7>, <Cell 'Sheet1'.C7>))'''
for elements in sheet['A1':'C7']:
    for element in elements:
        print(element.coordinate, element.value)
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
A4 2015-04-08 08:59:43
B4 Oranges
C4 52
---- END OF ROW ----
A5 2015-04-10 02:07:00
B5 Apples
C5 152
---- END OF ROW ----
A6 2015-04-10 18:10:37
B6 Bananas
C6 23
---- END OF ROW ----
A7 2015-04-10 02:40:46
B7 Strawberries
C7 98
---- END OF ROW ----
'''