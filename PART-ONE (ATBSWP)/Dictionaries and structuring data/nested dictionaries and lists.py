allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBought(guests, item):
    numBought = 0
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return numBought

print('Number of things being bought:')
print(' - Apples ' + str(totalBought(allGuests, 'apples')))
print(' - Cups ' + str(totalBought(allGuests, 'Cups')))
print(' - Cakes ' + str(totalBought(allGuests, 'Cakes')))
print(' - Ham sandwiches ' + str(totalBought(allGuests, 'Ham sandwiches')))
print(' - Apple pies ' + str(totalBought(allGuests, 'apple pies')))
