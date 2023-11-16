def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# someParameter = spam = [1,2,3]
# even though spam and someParameter contain seperate references, they both refer to the same list
