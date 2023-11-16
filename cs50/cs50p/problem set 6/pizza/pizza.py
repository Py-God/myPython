import sys, csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit()
    elif len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit()
    if not sys.argv[1].endswith('.csv'):
        print('Not a CSV file')
        sys.exit()

    try:
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)
            reader_list = list(reader)
    except FileNotFoundError:
        print('File does not exist')
        sys.exit()

    print(tabulate(reader_list, headers='keys', tablefmt='grid'))

if __name__ == '__main__':
    main()
