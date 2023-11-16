def main():
    time = input('What time is it? ')
    food_time = convert(time)
    if food_time != None:
        print(food_time)

def convert(time):
    hour, minute = map(int, time.split(':'))
    if hour in range(7, 9):
        if minute in range(0, 60):
            return 'breakfast time'
    elif hour in range(12, 14):
        if minute in range(0, 60):
            return 'lunch time'
    elif hour in range(18, 20):
        if minute in range(0, 60):
            return 'dinner time'
    return

if __name__ == '__main__':
    main()
