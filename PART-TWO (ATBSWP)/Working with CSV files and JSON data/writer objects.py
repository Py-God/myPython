import csv

outputFile = open('C:\\Users\\user\\Desktop\\PYTHON\\output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
21
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
32
outputWriter.writerow([1, 2, 3.141592, 4])
16
outputFile.close()
