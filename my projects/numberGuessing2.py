#! python3
# this code is the opposite of numberGuessing.py
# the user will input a number then the computer will try to guess the number in a certain number of tries
import random, sys

def playGame():
    print('''
instructions: You have to type in your guessed number into the terminal
i will guess a number three times in hopes of getting your guessed number 
you have to tell me "higher" or "lower" every guess for me to append my guesses    
    ''')
    print('''I am ready to play your game.
Are you ready?
            y or yes = yes
            n or no = no''')
    ans = input().lower()
    if ans in ['y', 'yes', 'n', 'no']:
        if ans in ['y', 'yes']:
            numberGuesser()
        else:
            print('I\'m always ready. Hope you\'ll be ready next time')
    else:
        print('I don\'t understand that command. Choose one of the options given.')
        playGame()

def numberGuesser():

    print('''type in your secret number from 1 to 10.
            or type 11 to exit
            i promise i wont cheat.
            ;)''')
    limit = 3
    inp = int(input())
    if inp > 0 and inp < 11:
        g = random.randint(1, 10)
        print('i guess '+ str(g))
        while limit > 0:
            limit -= 1
            clue = input().lower()
            if clue == 'higher':
                guess = random.randint(g+1, 10)
                answers = ['Is it ' + str(guess) + '?', 'I think ' + str(guess), str(guess) + '?', 'Im guessing... ' + str(guess)]
                answer = random.choice(answers)
                print(answer)
                limit -= 1
                continue
            elif clue == 'lower':
                guess = random.randint(1, g-1)
                answers = ['Is it ' + str(guess) + '?', 'I think ' + str(guess), str(guess) + '?', 'Im guessing... ' + str(guess)]
                answer = random.choice(answers)
                print(answer)
                limit -=1
                continue
            elif clue == 'yes':
                print('yay! I knew i could guess it.')
                sys.exit()
    elif inp == 11:
        print('byee.')
        sys.exit()
    else:
        print('i said from 1 to 10')
        numberGuesser()

    anotherAns = input()
    print('whats the number?')
    lastAns = input()
    print('jeez, i tried tho.')


playGame()