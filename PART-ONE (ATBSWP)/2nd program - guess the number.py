import random

secretNumber = random.randint(1, 20)    # find a number btw 1 and 10 and store it in secretNumber
print('I am thinking of a number between 1 and 20')
while True:
    try:
        for guessesTaken in range(1, 7):
            print('Take a guess.')
            guess = int(input())            # telling the player to guess a number in 6 tries

            if guess < secretNumber:
                print('Your guess is too low.')
            elif guess > secretNumber:
                print('Your guess is too high.')
            else:
                break           # they have gotten the number so you need to break out of the for loop
        if guess == secretNumber:   
            print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        else:
            print('Nope. The number i was thinking of was ' + str(secretNumber))
    except ValueError:
        print('that is not a number. try again')
    except NameError:
        print('a guess can only be a whole number not a decimal')
        if guess != secretNumber:
            continue
        else:
            break


# after the for loop, this ast if else statement checks whether the player has guessed
# the number and prints an appropriate message on the screen
