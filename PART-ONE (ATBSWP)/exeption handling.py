def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: invalid arguement.')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

print('----------------')

def eggs(divideby):
    return 43 / divideby

try:                        # exception statements can also be put in function calls
    print(eggs(21))
    print(eggs(0))
    print(eggs(23))
except ZeroDivisionError:
    print('Error: invalid arguement')
    
    # the eggs(23) didnt print because once the execution jumps to the except
    # clause in the function calls, it doesnt go back to the try clause
