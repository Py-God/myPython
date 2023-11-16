from pyfiglet import Figlet
import sys

length = len(sys.argv)

if length == 1:
    text = input('Input: ')
    f = Figlet()
    print('Output: ')
    print(f.renderText(text))
elif length == 3:
    if sys.argv[1] != '-f' or sys.argv[1] != '--font':
        if '_' in sys.argv[2]:
            print('Invalid usage')
            sys.exit()
            
        text = input('Input: ')
        f = Figlet(font=sys.argv[2])
        print('Output: ')
        print(f.renderText(text))
else:
    print('Invalid usage')
