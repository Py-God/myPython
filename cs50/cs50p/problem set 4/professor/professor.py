import random

def main():
    score = 0

    for _ in range(10):
        question, ans  = generate_question()
        for _ in range(3):
            try:
                user_ans = int(input(question))
            except ValueError:
                print('EEE')
                continue
            if user_ans == ans:
                score += 1
                break
            else:
                print('EEE')
    print(score)
            

def generate_question():
    no1, no2 = generate_numbers(level)
    ans = no1 + no2
    return (str(no1) + ' + ' + str(no2) + ' = ', ans)

def get_level():
    try:
        level = int(input('Level: '))
    except ValueError:
        get_level()
    if level in [1, 2, 3]:
        return level

def generate_numbers(level):
    if level == 1:
        no1 = random.randint(0, 9)
        no2 = random.randint(0, 9)
    elif level == 2:
        no1 = random.randint(10, 99)
        no2 = random.randint(10, 99)
    elif level == 3:
        no1 = random.randint(100, 999)
        no2 = random.randint(100, 999)
    return (no1, no2)

level = get_level()
main()
    
