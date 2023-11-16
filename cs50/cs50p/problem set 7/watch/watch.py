import re
import sys

def main():
    print(parse(input('HTML: ')))

def parse(s):
    regex = re.compile(r'(http|https)://(www.)*(youtube.com){1}/embed/(\w+)')
    if matches := re.search(regex, s):
        print(matches.group())
        return f'https://youtu.be/{matches.group(4)}'
    return None


if __name__ == '__main__':
    main()
