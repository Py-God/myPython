print('Hello')
print('world')
# two strings appear on seperate lines because the print() function
# automatically adds a new line character to the end of the string its passed

print('--------------')

print('Hello ', end = '')
print('World')
# this is useful if you need to disable the new line that gets added to the end
# of every print() function call

print('---------------')

print('cats', 'dogs', 'mice')
# python automatically puts an empty space in between keywords, you can change this

print('---------------')

print('cats', 'dogs', 'mice', sep = ',')
