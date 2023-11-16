def spam():
    global eggs
    eggs = 'spam'   # eggs here isnt a local variable since youve set it to global
                    # when the execution calls spam() it retrieves the global variable
eggs = 'global'     # 'spam' in the spam function instead of 'global' because it 
spam()              # is called last and overides it
print(eggs)
