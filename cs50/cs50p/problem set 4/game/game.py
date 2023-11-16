import random, sys

def main():
    while True:
        level = input('Level: ')
        if level == '':
            main()
        level = int(level)
        if level < 1:
            main()
        elif level >= 1:    
            number = random.randint(1, level)
            game(number)
        
def game(number):
    try:
        guess = int(input('Guess: '))
    except ValueError:
        game(number)
    if guess < 1:
        game(number)
    if guess > number:
        print('Too large!')
        game(number)
    elif guess < number:
        print('Too small!')
        game(number)
    else:
        print('Just right!')
        sys.exit()


main()
    
