import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'reply hazy try again'
    elif answerNumber == 5:
        return 'ask again later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# the bottom three codes can be reduced to
# print(getAnswer(random.randint(1, 9)))
