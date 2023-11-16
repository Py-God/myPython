def main():
    mass = int(input('m: '))
    print('E:', convert(mass))

def convert(mass):
    return mass * (3*10**8)**2

main()
