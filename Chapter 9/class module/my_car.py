from car import Car as c, ElectricCar as ec



car = c('audi', 'n4', 2024)
print(car.get_discriptive_name())
car.fill_gas_tank()



my_leaf = ec('nissan', 'leaf', 2024)
print(my_leaf.get_discriptive_name())
my_leaf.battery.discribe_battery()
my_leaf.battery.get_range()


