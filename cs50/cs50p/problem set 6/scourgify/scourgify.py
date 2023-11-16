import sys, csv

def main():
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit()
    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit()
    if not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
        print('Invalid file format')
        sys.exit()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            reader_dict = list(reader)
    except FileNotFoundError:
        print('Could not read', sys.argv[1])
        sys.exit()

    cleaner(reader_dict)

def cleaner(reader_dict):
    for dicts in reader_dict:
        lastname, firstname = dicts['name'].split(', ')
        dicts.pop('name')
        dicts['first'] = firstname
        dicts['last'] = lastname
        
    new_file(reader_dict)

def new_file(reader_dict):
    with open(sys.argv[2], 'w') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        
        for dicts in reader_dict:
            writer.writerow(dicts)
    

if __name__ == '__main__':
    main()
