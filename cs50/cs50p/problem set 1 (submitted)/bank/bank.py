def main():
    reply = input('Greeting: ').strip().lower()
    print(payer(reply))

def payer(reply):
    if reply.startswith('hello'):
        return '$0'
    elif reply.startswith('h'):
        return '$20'
    return '$100'

main()
