import csv

exampleFile = open('C:\\Users\\user\\Desktop\\PYTHON\\example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
[['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], ['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', 'Strawberries', '98']]
exampleData[0][0]
'4/5/2014 13:34'
exampleData[0][1]
'Apples'
exampleData[0][2]
'73'
exampleData[1][1]
'Cherries'
exampleData[6][1]
'Strawberries'
