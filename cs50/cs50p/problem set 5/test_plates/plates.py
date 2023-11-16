import re

def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    regex_obj = re.compile(r'(^([a-zA-Z]{2,})(([1-9][0-9]+)*)$)')
    if match := re.search(regex_obj, s):
        return True
    return False

if __name__ == '__main__':
    main()
