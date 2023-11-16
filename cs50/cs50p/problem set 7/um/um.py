import re
import sys

def main():
    print(count(input('Text: ')))

def count(s):
    if 'um' in s:
        words = s.split(' ')
        count = 0

        regex = re.compile(r'um\W|^um$')
        for word in words:
            if 'um' in word:
                if matches := re.search(regex, word):
                    count += 1
        return count
    return 0

if __name__ == '__main__':
    main()
