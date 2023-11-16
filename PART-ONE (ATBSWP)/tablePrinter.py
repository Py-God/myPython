tableData = [['apples', 'orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def tablePrinter():
    firstColumn = tableData[0][0].ljust(7) + tableData[1][0].center(7) + tableData[2][0].rjust(5)
    secondColumn = tableData[0][1].ljust(7) + tableData[1][1].center(7) + tableData[2][1].rjust(5)
    thirdColumn = tableData[0][2].ljust(7) + tableData[1][2].center(7) + tableData[2][2].rjust(5)

    print(firstColumn)
    print(secondColumn)
    print(thirdColumn)

tablePrinter()
