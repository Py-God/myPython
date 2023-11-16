def main():
    reply = input('Greeting: ').strip().lower()
    print(value(reply))

def value(reply):
    if reply.startswith('hello'):
        return '$0'
    elif reply.startswith('h'):
        return '$20'
    return '$100'

if __name__ == '__main__':
    main()
