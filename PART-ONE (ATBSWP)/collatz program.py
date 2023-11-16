def collatz(number):
    while True:
        if number % 2 == 0:
            newEvenNumber = number // 2
            print(newEvenNumber)
            break
        continue

        elif number % 2 == 1:
            oddNumber = 3 * number + 1
            print(oddNumber)
            break
        continue
        
        

print('Enter a number')
number = int(input())
collatz(number)
