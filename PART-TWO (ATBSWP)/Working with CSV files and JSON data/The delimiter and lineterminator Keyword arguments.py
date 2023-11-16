import csv

csvFile = open('C:\\Users\\user\\Desktop\\PYTHON\\example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
23
csvWriter.writerow(['eggs', 'bacon', 'ham'])
16
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
31
csvFile.close()
