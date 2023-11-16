import random

messages = ['It is certain',
            'It is decidedly so',
            'yes, definitely',
            'Reply hazy',
            'try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so doubtful',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

print('Four score and seven ' + \
      'years ago...')

print(random.randint(0, 8))
