# If conditions
cars = ['toyota', 'bmw', 'tesla', 'rolse royce']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())       # We also avoide to print other value by None

# Bolean condition
Car = 'bmw'
if Car == 'bmw':
    print(Car.upper())
else:
    None
# Equality and notequality opperators.
print(Car == 'Bmw')
print(Car == 'bmw')

request = 'chicken burger'
if request != 'biryani':
    print('Hold the biryani')

answer = input("Enter th number")
if answer != 42:
    print("Wrong answer! Please try Again")


# and or operatore
my_age = 18
friend_age = 16

if my_age <= 18 and friend_age >= 14:
    print(" You'll go into Maried.")
else:
    print("You'll not go to Maried")

car = 'audi'
print(car.title() == 'Audi')

x = 5
y = 9
print(x <= 4 or y >= 10)

# Check Presentation
cars = ['toyota', 'suzuki', 'honda civic', 'honda city', 'toyota', 'Audi', 'tesla',
        'rolse royse', 'bughati','porsche', 'bmw', 'lamborghini', 'firarry']
print('mazda' in cars)
print('bmw' in cars)

expensive_car = 'rolse royse'
if expensive_car in cars:
    print(f"You can't buy the most expensive car, The {expensive_car.title()}")
else:
    print(f"You can buy the expensive Car")
indian_car = 'marutisazuki'
if indian_car not in cars:
    print(f"You can't buy {indian_car.title()}")

# Problem No 5.1: Solution
car = "subaru"
print("Is car == 'subaru'? I predict true ")
print(car == 'subaru')

moterbike = ['cd', 'honda', 'yahama', 'suzuki', '125cg']
print(moterbike[1] == 'honda')
print(moterbike[0] == 'cd' and moterbike[3] == 'suzuki')
numbers_list = list(range(1,101))
print(numbers_list[99] <= 100)
print(numbers_list[:] == range(1,200)) 

sickle = ['small', 'midle', 'large', 'extra larg']
print('gear scikle' in sickle)
print('small' not in sickle)
print('get sickle' is sickle or 'large' not in sickle)
print(numbers_list[49] <= numbers_list[40])
print(numbers_list[90]  == numbers_list[89 + 1])


# Problem No 5.2: We also solve this problem in previous problem expect 1
string_name = 'Mubashir'
lower_name = 'mudasir'
upper_name = 'AZHAR'

print(string_name.lower() == 'mubashir')
print(lower_name.upper() == 'MUDASIR')
print(upper_name == 'Azhar')


# If-elif-else Conditions
user_age = 25
if user_age >= 18:
    print("You are able to creat this account.")
    print("Will you want to creat the account.")
else:
    print("You aren't enable to creat account.")
    print("Please wait to be able to create the account")

age_for_park = 17
if age_for_park <= 8:
    price = 'free'
elif age_for_park <= 18:
    price = '5 USD'
elif age_for_park <= 30:
    price = '10 USD'
elif age_for_park >30:
    price = '15 USD'
print(f"your cost for rolercoster ride is {price}")

burger_recipie = ['bread', 'mionies', 'egg','slaad']
if 'chicken thakka' in burger_recipie:
    print('Added Chicken Thakka')
if 'mionies' in burger_recipie:
    print('Added Mionies')
if 'slaad' in burger_recipie:
    print('slaad added')
if 'egg' in burger_recipie:
    print('Added egg')
else:
    None

print('\nYour burge is ready.')

# Problem No 5.3: Solution
alien_color = ['green', 'yellow','red']
if 'green' in alien_color:
    print('This player just earn 5 points.')
if 'blue' in alien_color:
    print("Nothing")

# Problem No 5.4 continue to 4.3: Solution

if 'green' not in alien_color:
    print('This player earn just 10 points.')
else:
    print('This player ern just 5 points.')

# Problem No 5.5 continue to 5.4: Solution

if 'green' in alien_color:
    print("This player just earn 5 Points")
if 'yellow' in alien_color:
    print('Thus player just earn 10 points')
if 'red' in alien_color:
    print("This player just earn 15 points")

# Problem No 5.6: Solution 
person_age = 18
if person_age < 2:
    print("You are a Baby.")
elif 2 <= person_age <= 4:
    print("You are a toddler.")
elif 4 <= person_age <= 13:
    print("You are kid.")
elif 13 <= person_age <= 20:
    print("YOu are a teenager.")
elif 20 <= person_age <= 65:
    print("You are an edult.")
elif person_age >= 65:
    print("You are an elder.")

# Problem No 5.7: Solution
no_favorite_fruite  = ['apple', 'orange', 'mango']
if 'apple' in no_favorite_fruite:
    print("I don't like it")
if 'orange' in no_favorite_fruite:
    print("I don't like it")
if 'mango' in no_favorite_fruite:
    print(f"I don't like it.")
if 'bannana' in no_favorite_fruite:
    print("I don't like it.")
if 'grapse' in no_favorite_fruite:
    print("I don't like it.")


requesr_burgers = ['bread', 'egg', 'chicken', 'mionies']
for request_burger in requesr_burgers:
    if request_burger == 'egg':
        print(f"Egg is out of stock")
    else:
        print(f"Added {request_burger}.")
print("You burger is ready")

request_tooping = []
if request_tooping:
    for tooping in request_tooping:
        print(f"Added {tooping}")
    print("Your burger is ready")
else:
    print("Are you sour, you sent a Request Tooping.")

available_services = ['video editing', 'tts', 'ttp', 'ttv', 'tt avater video']
request_services = ['video editing', 'tts', 'tt documentry' ]
for request_service in request_services:
    if request_service in available_services:
        print(f"You can use {request_service}")
    else:
        print(f"Sorry we can't prvide {request_service}")

print("\nSome services is provided sone.")


# Problem No 5.8: Solution
user_list = ['admin','mubashir_4xc1_0','mrbeast','azhar_cc1e','shoaib_jam']
for user in user_list:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report.")
    else:
        print(f"Hello {user}, Thanks for loging back.")


# Problem No 5.9: Solution:
new_users = []
if new_users:
    for users in new_users:
        print(f"Hello {users}")
else:
    print("We need to find some users.")

# Problem No 5.10: Solution
current_users = ['mubashir_alone', 'alone_mubashir', 'mubashir_786',
                 'mubashir112', "mubashir1"]
new_username = ['mubashir2', 'Mubashir1','mubashirjam', 'jammubashir',
                'Alone_mubashir']
for newname in new_username:
    if newname.lower() in current_users:
        print(f"Already taken.")
    else:
        print(f"{newname} is available.")

# Problem No 5.10: Solution
priority_numbers = list(range(1,10))
for priority_number in priority_numbers:
    if priority_number == 1:
        print(f"{priority_number}st")
    elif priority_number == 2:
        print(f"{priority_number}nd")
    elif priority_number == 3:
        print(f"{priority_number}rd")
    else:
        print(f"{priority_number}th")
