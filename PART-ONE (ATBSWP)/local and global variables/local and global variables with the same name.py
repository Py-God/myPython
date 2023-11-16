def spam():
    eggs = 'spam local'
    print(eggs) # prints spam local
    
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints bacon local
    spam()      # spam function is called to print its eggs variable *it doesnt replace the eggs that is printed in the next line*
    print(eggs) # prints bacon local

eggs = 'global'
bacon()
print(eggs) # prints global
