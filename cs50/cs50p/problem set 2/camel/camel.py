def main():
    camelCase = input('camelCase: ')
    snake_case = snake(camelCase)
    if snake_case == '':
        print('snake_case:', camelCase)
    else:
        print('snake_case:', snake(camelCase))

def snake(camelCase):
    snake_case = ''
    for letter in camelCase:
        if letter.isupper():
            letter = '_' + letter.lower()
        snake_case += letter

    return snake_case

if __name__ == '__main__':
    main()
