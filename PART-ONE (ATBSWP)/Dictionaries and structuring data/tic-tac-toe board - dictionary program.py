theBoard = {'top-L': '  ', 'top-M': '  ', 'top-R': '  ',
            'mid-L': '  ', 'mid-M': '  ', 'mid-R': '  ',
            'low-L': '  ', 'low-M': '  ', 'low-R': '  '}
# the value for every key in the board is a single spaced string so this is an empty board

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()          # move is top-L, mid-M,  anyone
    theBoard[move] = type   # sets top-L or so to X or O    
    if turn == 'X':
        turn = 'O'          # changes the turn variable to O
    else:
        turn = 'X'

printBoard(theBoard)
