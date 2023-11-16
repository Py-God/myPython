import random
import time

# The invite and call to play

print('''
        Welcome to Mouse and Cheese game
         ''')
time.sleep(2)
name = input('Please Enter your name: ')
print('')
time.sleep(2)
print('Hello ' + name + ', Thank you for choosing to play.')
time.sleep(1)
print('Best of luck!!!   ;)')
time.sleep(2)
print('')
print('''           Lets play Mouse and Cheese!''')
time.sleep(3)

# Defining my parameters
def main():
    global display
    global word
    global alreadyGuessed
    global length
    global playGame

    wordsToGuess = ['sprite', 'tame', 'dog', 'mouse']
    word = random.choice(wordsToGuess)
    length = len(word)
    display = 'Trap ' + ('-' * len(word)) + ' Mouse ' + ('-' * len(word)) + ' Cheese'
    alreadyGuessed = []
    playGame = ''
    count = 0

# setting a play loop
def playLoop():
    global playGame
    playGame = input('Do you want to play again? y = yes, n = no \n').lower()
    while playGame not in ['y', 'n']:
        playGame = input('Do you want to play again? y = yes, n = no \n').lower()
    if playGame == 'y':
        main()
    elif playGame == 'n':
        print('Thank you for playing my game! I expect you back again!')
        exit()

# Actually coding the game
def mouseAndCheese():
    global count
    global display
    global word
    global alreadyGuessed
    global playGame
    limit = len(word) * 2

    guess = input('This is the M&C word ' + display + ' Enter your guess: \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= '9':
        print('You have to type a letter.\n')
        hangman()
    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index + 1:]
        display = 'Trap ' + ('-' * (len(word)+1)) + ' Mouse ' + ('-' * (len(word)-1)) + ' Cheese'
        time.sleep(1)
        print(display + '\n')
    elif guess in alreadyGuessed:
        print('You have guessed this letter. Try another.\n')
    else:
        count += 1
        if count == 1:
            display = 'Trap ' + ('-' * (len(word)-1)) + ' Mouse ' + ('-' * (len(word)+1)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
        elif count == 2:
            display = 'Trap ' + ('-' * (len(word)-2)) + ' Mouse ' + ('-' * (len(word)+2)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
        elif count == 3:
            display = 'Trap ' + ('-' * (len(word)-3)) + ' Mouse ' + ('-' * (len(word)+3)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
        elif count == 4:
            display = 'Trap ' + ('-' * (len(word)-4)) + ' Mouse ' + ('-' * (len(word)+4)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
        elif count == 5:
            display = 'Trap ' + ('-' * (len(word)-5)) + ' Mouse ' + ('-' * (len(word)+5)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
        elif count == 6:
            display = 'Trap ' + ('-' * (len(word)-6)) + ' Mouse ' + ('-' * (len(word)+6)) + ' Cheese'
            time.sleep(1)
            print(display + '\n')
            
        
    if word == '_' * length:
        print('You win! Good Game')
        playLoop()
    elif '_' in word:
        
        mouseAndCheese()
    else:
        print('You lost! nice try.')
        time.sleep(1)
        print('The word was',alreadyGuessed,word)
        playLoop()

main()
mouseAndCheese()

        
        
                

