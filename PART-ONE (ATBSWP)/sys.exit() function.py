import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed '+ response + '.')     # see that when you typed exit, the
                                            # last line wasn't called
                                            # the progam stops ABRUPTLY.
