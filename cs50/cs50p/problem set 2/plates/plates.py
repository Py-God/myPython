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
    elif '.' in s or ' ' in s or '?' in s or '!' in s:
        return False
    
    regex_obj = re.compile(r'^[a-zA-Z]{2,}(([0-9][0-9])$)*')
    if match := re.search(regex_obj, s):
        print(match.group())
        inputs = match.group().split()
        print(inputs)
        size = len(inputs)
        
        for i in range(size):
            if type(inputs[i]) == int:
                if inputs[i] in range(10):
                    return False
        
        if match.group(1):
            print(match.group(1))
            if match.group(1).startswith('0'):
                return False
        return True
    return False

main()
