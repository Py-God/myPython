class User():
    def __init__(self, firstName, lastName, age, email, height, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.height = height
        self.gender = gender
        self.loginAttempts = 1

    def describeUser(self):
        print('''first name: %s
last name: %s
age: %s yrs old
email: %s
height: %s
gender: %s
LOGIN ATTEMPT(S): %s''' % (self.firstName, self.lastName, str(self.age), self.email, self.height, self.gender, self.loginAttempts))
        self.loginAttempts += 1
        print('----------------------------')
    def resetAttempts(self):
        self.loginAttempts = 0
    def greetings(self):
        print('Welcome %s' % (self.firstName + ' ' + self.lastName))

class Priviledges():
    def __init__(self, priviledges = ["can add post", "can delete post", "can ban user"]):
         self.priviledges = priviledges
    def display_priviledges(self):
        for priviledge in self.priviledges:
            print(priviledge)

class Admin(User):
    def __init__(self, firstName, lastName, age, email, height, gender):
        super().__init__(firstName, lastName, age, email, height, gender)
        self.priviledges = Priviledges()

user1 = User('Bolu', 'Promise', 18, 'boluwatifelekeoduoye@gmail.com', '6ft', 'male')
user2 = Admin('Boluwatife', 'Promise', 18, 'boluwatifelekeoduoye@gmail.com', '6ft', 'male')

user1.describeUser()
user1.describeUser()
user1.greetings()

user1.resetAttempts()
user1.describeUser()

print('----------')
user2.priviledges.display_priviledges()
