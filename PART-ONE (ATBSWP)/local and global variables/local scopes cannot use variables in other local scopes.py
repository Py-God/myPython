def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
spam()

# when bacon() is called its local scope is destroyed so the function bacon at
# the bottom is destroyed and cant print eggs as 0 as in the bacon function
# spam() still exists so it returns 99
# -local variables in one function are completely different from local variables in another-

