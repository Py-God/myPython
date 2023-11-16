def main():
    expression = input('Expression: ').strip().split()
    print(calculator(expression))

def calculator(expression):
    no1, operator, no2 = expression
    if operator == '+':
        return float(no1) + float(no2)
    elif operator == '-':
        return float(no1) - float(no2)
    elif operator == '*':
        return float(no1) * float(no2)
    elif operator == '/':
        return float(no1) / float(no2)

main()
