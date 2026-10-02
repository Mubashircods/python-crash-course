# Solution 9.1

class Resturent:
    def __init__(self, resturent_name, cuisine_name):
        self.name = resturent_name
        self.cuisine = cuisine_name
    def describe_resturent(self):
        print(f"The {self.name.title()} is one of the famouse one in khanpur.")
        print(f"I don't now who is {self.cuisine.title()}\n")

    def resturent_open(self):
        print(f"Resturent ``{self.name.title()}`` is now open.")


resturent = Resturent('but da hotel', 'but')
print(resturent.name.title())
print(resturent.cuisine.title())

resturent.describe_resturent()
resturent.resturent_open()




# Solution 9.2 Start from 9.1
resturent_1 = Resturent('coll and coll', 'who coll')
resturent_2 = Resturent('adei bhai', 'adie')
resturent_3 = Resturent('apna Dhaba', 'hadi')

resturent_1.describe_resturent()
resturent_2.describe_resturent()
resturent_3.describe_resturent()




# Solution 9.3
class Users:
    def __init__(self, first_name, last_name, age='', location=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def discribe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        if self.location and self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}\nAnd their location is {self.location}")
        elif self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}")
        else:
            print(f"The full name of user is {full_name.title()}")
    def greet_user(self):
        full_name = self.first_name +' '+self.last_name
        print(f"Hello {full_name.title()}! Thank you to come in my site.\n")
        



me = Users('jam', 'mubashir', 17, 'Dera Gabolan')
me.discribe_user()
me.greet_user()

he = Users('chaudhary', 'umar')
he.discribe_user()
he.greet_user()

she = Users('misbah', 'korai', 23, 'manik waki')
she.discribe_user()
she.greet_user()




# Solution 9.4 continued by 9.1 `Copy code.`
class Resturent:
    def __init__(self, resturent_name, cuisine_name):
        self.name = resturent_name
        self.cuisine = cuisine_name
        self.service = 10
    def describe_resturent(self):
        print(f"The {self.name.title()} is one of the famouse one in khanpur.")
        print(f"I don't now who is {self.cuisine.title()}\n")

    def resturent_open(self):
        print(f"Resturent ``{self.name.title()}`` is now open.")

    def number_surved(self, number=10):

        self.service = number
        print(f"This resturent served only {self.service} custmers\n")
    def increase_service(self, service):

        self.service += service
        print(f"{self.service} custmers are server in this buisness day.\n")
    


resturent = Resturent('but da hotle', 'but')

resturent.number_surved(2)
resturent.increase_service(18)





# Solution 9.5 continued from 9.3 ``Copy code``
class Users:
    def __init__(self, first_name, last_name, age='', location=''):
        self.first_name = first_name
        self.last_name = last_name
        self.login_atempt = 0
        self.age = age
        self.location = location

    def discribe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        if self.location and self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}\nAnd their location is {self.location}")
        elif self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}")
        else:
            print(f"The full name of user is {full_name.title()}")

    def greet_user(self):
        full_name = self.first_name +' '+self.last_name
        print(f"Hello {full_name.title()}! Thank you to come in my site.\n")
    
    def increase_login_attempt(self, attempt=1):
        self.login_atempt += attempt

    def reset_login_attempt(self):
        self.login_atempt = 0


user = Users('jam', 'mubashir')
print(user.login_atempt)
user.increase_login_attempt(1)
print(user.login_atempt)
user.reset_login_attempt()
print(user.login_atempt)




# Solution 9.6
class IceCreamStand(Resturent):
    def __init__(self, resturent_name, cuisine_name):
        super().__init__(resturent_name, cuisine_name)
        self.flavors_list = ['wanella', 'pista', 'kulfa', 'chocolate']
    
    def display_flavors(self):

        print(f"The following flawore is available in our services:")
        for flaver in self.flavors_list:
            print("\t",flaver)

IceCream = IceCreamStand('butt', 'hotle')
IceCream.display_flavors()




# Solution 9.7    # This exersice is modyfied due to problem 9.9
# class Admin(Users):
#     def __init__(self, first_name, last_name, age='', location=''):
#         super().__init__(first_name, last_name, age, location)
#         # self.privileges_string = Privileges()
#         # self.privilages = ['can add post', 'can delete post', 'can ban user',
#         #                    'can awarded user', 'can unban user', 'can recover user']


# adminestater = Admin('mubashir', "alone")
# adminestater.show_privileges()





# Solution 9.8
class Privileges:

    def __init__(self, privilages=['can add post', 'can delete post', 'can ban user',]):
        self.privilages = privilages

    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privilages:
            print(f"\t {privilege}.")


class Admin(Users):
    def __init__(self, first_name, last_name, age='', location=''):
        super().__init__(first_name, last_name, age, location)
        self.privileges_string = Privileges()
    

show_privilages = Admin('mubashir', 'jam')
print(f"{show_privilages.first_name.title()}")
show_privilages.privileges_string.show_privileges()




# Solution 9.9
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

    def update_battery(self):
        if self.battery_size <= 1500:
            self.battery_size += 500
        else:
            None
        




class ElectricCar(Car):

    def __init__(self, make, modle, year):
        super().__init__(make, modle, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This car has not gas tank.")



car = ElectricCar('nisane', 'leaf', 2024)
car.battery.get_range()
car.battery.update_battery()
car.battery.get_range()





# Solution 9.10

# This solution path is class module/resturent/
# Problem solved.


# Solution 9.11     # This solution is modify due to solve problem 9.12

# This problem path is class module/privileges
# Problem Solved.


# Solution 9.12

# This problem path is class module/privileges
# Problem solved.




# Solution 9.13
from random import randint
class Die:

    def __init__(self):
        self.sides = 20

    def roll_die(self):
        
        print(randint(1, self.sides))

hello = Die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()
hello.roll_die()




# solution 9.14
from random import *
lottery = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']

ticket_number = choice(lottery)+choice(lottery)+choice(lottery)+choice(lottery)
print(f"Any ticket matching these 4 numbers or letters '{ticket_number}' wins a prize.")




# Solution 9.15
lottery_ticket = ['0','1','2','3','4','5','6','7','8','9','F','G','H','I','J']
my_ticket = '17J3'
attempt = 0
while True:
    ticket_number = choice(lottery_ticket)+choice(lottery_ticket)+ \
    choice(lottery_ticket)+choice(lottery_ticket)
    attempt += 1
    if ticket_number == my_ticket:

        print(f"Congratulation!\nYour ticket number is {my_ticket}\n"
              f"On {attempt} attempts you won the prize.")
        break


# Solution 9.16

# Visit this site ``https://pymotw.com``
