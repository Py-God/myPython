groceries = {}

while True:
    try:
        item = input()

        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break

print()
for grocery in sorted(groceries, key=lambda s: s):
    print(groceries[grocery], grocery.upper())
