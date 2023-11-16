names = []
while True:
    try:
        name = input('Name: ')
        if name != '':
            names.append(name)
    except EOFError:
        break

length = len(names)
message = 'Adieu, adieu, to '

if length == 1:
    message += names[0]
    print(message)
elif length == 2:
    message += ' and '.join(names)
    print(message)
elif length > 2:
    last_name = names.pop()
    message += ', '.join(names)
    message += ', and ' + last_name
    print(message)
        
