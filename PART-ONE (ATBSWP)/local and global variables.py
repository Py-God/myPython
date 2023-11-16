def spam():
    eggs = 31337
spam()
print(eggs)

# this will cause an error
# this error happens because the eggs variable exists only in the local variable created when the spam() function was called
# once the program execution returns spam(), the eggs variable is destroyed
# *a global scope cannot use local variables*
