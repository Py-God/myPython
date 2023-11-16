import sys

def main():
    if len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit()
    elif len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit()
        
    if not sys.argv[1].endswith('.py'):
        print('Not a python file')
        sys.exit()
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File does not exist')
        sys.exit()

    print(line_counter(lines))

def line_counter(lines):
    new_content = [line for line in lines if line.strip() != '\n']
    new_content_list = [line for line in new_content if line.strip().startswith('#') == False]
   
    return len(new_content_list)

if __name__ == '__main__':
    main()
