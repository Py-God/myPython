#! python3
# Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.
import csv, re

csvFile = open('example.csv')
csvFileReader = csv.reader(csvFile)
dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
for row in csvFileReader:
    if dateRegex.search(''.join(row)) == None:
        print('invalidity found: no date at line ' + str(csvFileReader.line_num))
    elif ' ' in row:
        print('invalidity found: blank input at line ' + str(csvFileReader.line_num))
    else:
        continue
print('Search complete')