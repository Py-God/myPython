amount_due = 50
allowed_denominations = [5, 10, 25]


while amount_due > 0:
    print('Amount Due:', amount_due)
    deposit = int(input('Insert Coin: '))
    if deposit in allowed_denominations:
        amount_due -= deposit

print('Change Owed:', amount_due*-1)



    
    
