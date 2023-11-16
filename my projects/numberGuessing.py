#! python3
# the computer generates a random number from a range of numbers
# the user has a limited amount of tries to guess what number it is
# after every wrong guess, a hint is given by the computer about the number to be guessed

import random

def main():
    secretNumber = random.randint(1, 10)
    print('A number has been generated between 1 and 10 and including them')
    print('input your guess: ')
    limit = 3
    try:
        while limit > 0:
            userGuess = int(input())
            if userGuess == secretNumber:
                print('Congratulations, you guessed the number.')
                playLoop()
            elif userGuess < secretNumber:
                print('The number is greater than that.')
                limit -= 1
                print('input another number:')
                continue
            else:
                print('The number is less than that.')
                limit -= 1
                print('input another number:')
                continue
        if limit == 0:
            print('nice try, the number was ' + str(secretNumber))
    except ValueError:
        print('That is not a number. you will have to try again')
        main()

def playLoop():
    print('welcome to numberGuesser, do you want to play? y=yes, n=no')
    ans = input()
    if ans.lower() == 'y':
        main()
    elif ans.lower() == 'n':
        print('We hope you can play next time.')
        exit()

playLoop()

