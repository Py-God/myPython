class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You cant roll back odometer reading')
    def increment_odometer(self, miles):
        self.odometer += miles
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def readOdometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            self.battery_size = battery_size
 
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(10)
my_new_car.readOdometer()
my_new_car.increment_odometer(100)
my_new_car.readOdometer()

myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describe_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()
myTesla.battery.get_range()

