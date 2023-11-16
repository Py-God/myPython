class Restaurant():
    def __init__(self, name, cuisine, number_served):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 40
    def describe_restaurant(self):
        print('''name: %s
cuisine: %s
number of customers served: %s''' % (self.name, self.cuisine, self.number_served))
    def increment_number_served(self, daysCustomers):
        self.number_served += daysCustomers
    def open_restaurant(self):
        print(self.name+' is officially open')

class IceCreamStand(Restaurant):
    def __init__(self, name, number_served, cuisine='icecream'):
        super().__init__(name, cuisine, number_served)
        self.flavors = ['Vanilla', 'chocolate', 'strawberry', 'mint']
    def display_flavors(self):
        for flav in self.flavors: 
            print(flav)

restaurant = Restaurant("ChinaTwine", 'Chinese', 40)
restaurant1 = Restaurant("DinersDelight", 'Mexican', 4040)
restaurant2 = Restaurant('BurgerManic', 'European', 42)
restaurant3 = Restaurant('Dominos', 'American', 424)

print(restaurant.name)
print(restaurant.cuisine)
print('-------------------')
restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

restaurant3.increment_number_served(40)
restaurant3.describe_restaurant()
print('-------------------')
restaurant.open_restaurant()

ice = IceCreamStand('Middle Creamer', 200)
ice.display_flavors()
