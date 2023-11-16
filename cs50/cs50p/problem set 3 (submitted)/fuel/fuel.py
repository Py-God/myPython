def main():
    fraction = input('Fraction: ')
    print(percentage_calculator(fraction))

def percentage_calculator(fraction):
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
        
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
        
    return f'{percentage}%'

main()
