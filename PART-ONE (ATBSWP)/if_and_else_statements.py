#! python3

name = input()
age = int(input())
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('Youre not Alice kiddo')
else:
    print('Youre neither Alice nor a little kid')               # the elif statement would execute only when her name isnt Alice or else
                                                                #   itll greet her.
                                                                                       
name = input()
age = int(input())
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('Youre not Alice kiddo')
elif age > 2000:
    print('nice try but Alice is not an immortal vampire')
elif age > 100:
    print('Youre not Alice, grannie')
else:
    print('Hello, stranger.')                #*if elif age > 100 was put first the program would run the grannie function*
                                            #instead of the vampire cuz grannie is > 100. THE ORDER MATTERS
