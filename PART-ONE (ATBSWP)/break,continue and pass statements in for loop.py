for letter in 'python':
    if letter == 'h':
        break
    print(letter)
print('-----------')

var = 10
while var > 0:
    print(var)
    var = var - 1
    if var == 5:
        break
print('-----------')
    
for letter in 'python':
    if letter == 'h':
        continue
    print(letter)
print('-----------')

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print(var)
print('-----------')

for letter in 'python':
    if letter == 'h':
        pass
        print('this is the pass block')
    print(letter)
