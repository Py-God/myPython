def main():
    fraction = input('Fraction: ')
    convert(fraction)

def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
    except ValueError:
        main()

    if numerator > denominator:
        main()
    
    try:
        percentage = round((numerator/denominator)*100)
    except ZeroDivisionError:
        main()

    return percentage

def guage(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
        
    return f'{percentage}%'

if __name__ == '__main__':
    main()
