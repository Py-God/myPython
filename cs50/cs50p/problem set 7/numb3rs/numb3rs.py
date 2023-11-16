import re
import sys

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    regex = re.compile(r'^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$')
    
    if matches := re.search(regex, ip):
        matches_list = [matches.group(i) for i in range(1, 5)]
            
        for match in matches_list:
            if int(match) not in range(256):
                return False
        return True
    return False
            
if __name__ == '__main__':
    main()
