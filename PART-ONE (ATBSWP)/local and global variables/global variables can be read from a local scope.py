def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

# since there is no parameter assigning eggs to spam, when eggs is told to print
# python considers it a reference to the global variable 'eggs'.

#------------------------------------------------------------------------------#

# i want to write a code that assigns eggs as a funtion parameter just for
# PrAcTiCe ;)

def name(eggs):
    print(eggs)         # return didnt work when i used it here for some reason
name('i have 4 eggs')   # cause after return value the program terminates and cant search for the 'i have four eggs' i assigned at the end of the code.


    
