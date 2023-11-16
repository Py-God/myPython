#! python3
import sys

actualWord = 'Skye'
wordsGuessed = []
def hangman():
    print('Guess the word: ')
    word1 = input()
    wordsGuessed.append(word1)
    if wordsGuessed[0] != actualWord:
        print('Progress: -')
    else:
        print('Congratulations, you have won')
        sys.exit()
        
    print('Guess the word: ')
    word2 = input()
    wordsGuessed.append(word2)
    if wordsGuessed[1] != actualWord:
        print('Progress: --')
    else:
        print('Congratulations, you have won')
        sys.exit()

    print('Guess the word: ')
    word3 = input()
    wordsGuessed.append(word3)
    if wordsGuessed[2] != actualWord:
        print('Progress: ---')
    else:
        print('Congratulations, you have won')
        sys.exit()

    print('Guess the word: ')
    word4 = input()
    wordsGuessed.append(word4)
    if wordsGuessed[3] != actualWord:
        print('Progress: ----')
    else:
        print('Congratulations, you have won')
        sys.exit()

    print('Guess the word: ')
    word5 = input()
    wordsGuessed.append(word5)
    if wordsGuessed[4] != actualWord:
        print('Progress: -----')
        print('You have exhausted your chances. The word is ' + actualWord)
    else:
        print('Congratulations, you have won')
        
    
        
            
hangman()
