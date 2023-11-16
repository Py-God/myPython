spam = print('Hello!')
# Hello!
None == spam
# True

x = None
if x:
    print('do you think None is True?')
elif x is False:
    print('Do you think none is False?')
else:
    print('None is not True or False, None is just None...')
