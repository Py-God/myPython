class Dog():
    def __init__(self, name, age):
        # initialise name and age attributes
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + ' is now sitting')
    def rollover(self):
        print(self.name.title() +" rolled over")

myDog = Dog('Queen', 2)

print('My dogs name is '+ myDog.name + '. She is '+ str(myDog.age))
myDog.sit()
myDog.rollover()
