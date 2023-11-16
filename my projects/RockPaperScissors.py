import random, time, sys

def game():
    while True:
        print('''Welcome to rock paper scissors
            
            1 - rock
            2 - paper
            3 - scissors
                please type one of these numbers as your pick.''')
        num = input()
        rps = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        if num not in rps.keys():
            print('That is not an option, please follow the instructions')
            continue
        elif num == '1':
            player = 'rock'
        elif num == '2':
            player = 'paper'
        elif num == '3':
            player = 'scissors'
            
        computer = random.choice(['rock', 'paper', 'scissors'])

        if player == computer:
            time.sleep(1)
            print('You both picked ' + player + ' it is a tie!')
        elif player == 'paper' and computer == 'rock':
            time.sleep(1)
            print('The computer picked ' + computer)
            print('You won! '+ player + ' beats ' + computer)
        elif player == 'rock' and computer == 'scissors':
            time.sleep(1)
            print('The computer picked ' + computer)
            print('You won! '+ player + ' beats ' + computer)
        elif player == 'scissors' and computer == 'paper':
            time.sleep(1)
            print('The computer picked ' + computer)
            print('You won! '+ player + ' beats ' + computer)
        else:
            time.sleep(1)
            print('The computer picked ' + computer)
            print('you lost! ' + computer + ' beats ' + player)
        playAgain()
        
def playAgain():
    print('Do you want to play again?. y = yes, n = no')
    ans = input().lower()
    if ans == 'y' or ans == 'yes':
        game()
    elif ans == 'n' or ans == 'no':
        print('Thank you for playing. We hope to see you again.')
        sys.exit()
    else:
        print('That is not an option.')
        playAgain()
        
game()