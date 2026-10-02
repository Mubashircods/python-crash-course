class Car:
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 6

    def get_discriptive_name(self):

        long_name = f"{self.year} {self.make} {self.modle}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You don't roll back an odometer.")

    def Increasment_odometer(self, miles):
            
        self.odometer_reading += miles
    def fill_gas_tank(self):

        print(f"The gass tank if filled.")




class Battery:

    def __init__(self, battery_size=1500):
        self.battery_size = battery_size

    def discribe_battery(self):
        print(f"This car has {self.battery_size}-kwh battery size.")

    def get_range(self):
        if self.battery_size <= 1000:
            range = 500
        elif self.battery_size <= 1500:
            range = 750
        elif self.battery_size <= 2000:
            range = 1000
        print(f"This car has about {range}km range if it is fully charge.")



my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_discriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_new_car.Increasment_odometer(3)
my_new_car.read_odometer()





class ElectricCar(Car):

    def __init__(self, make, modle, year):
        super().__init__(make, modle, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This car has not gas tank.")


my_nisan = ElectricCar('nisan', 'leaf', 2024)
print(my_nisan.get_discriptive_name())
my_new_car.fill_gas_tank()
my_nisan.fill_gas_tank()
my_nisan.battery.discribe_battery()
my_nisan.battery.get_range()










