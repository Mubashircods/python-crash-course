# Sloution 7.1
rental_car = input("What kind of rental car you would like?>>> ")
print(f"Let me see if i find you a {rental_car.title()}.")


# Solution 7.2
peoples = int(input("How many people are in your dinner gorup?>>> "))
if peoples > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")


# Solution 7.3
number = int(input("Tell me a number To determine it's multiple>>> "))
if number % 10 == 0:
    print("This number is the multiple of 10")
else:
    print("This isn't a multiple of 10")


# Solution 7.4          / This exercise is modify due to compieate exersice 7.6  
active = True 
while active:
    toppings = input("Enter toppings for your pizza\n"
    "(Enter 'quit' to complete your toppings)>>> ")
    if toppings == 'quit':
        active = False
    else:
        print(f"{toppings.title()} is add.")
    

# Solution 7.5          / This exercise is modify due to compieate exersice 7.6

prompt = f"Tell me your age and i'll tell your ticket cost.>>> "
while True:
    age = int(input(prompt))

    if age <= 3:
        print("You are free.")
        break
    elif 3 < age <= 12:
        print('Your cost is 10$')
        break
    elif age > 12:
        print("Your cost is 15$")
        break
    
    


# Solution 7.6
# Ok problem 7.6 is solved.


# Solution 7.7

"""

count = 1
while count <= 5:      # This is infinity loop that is way it is commented.
    print(count)
"""


# Solution 7.8
sandwich_orders = ['club sandwich', 'grilled cheese sandwich', 'BLT Sandwich',
                  'chicken sandwich', 'tuna sandwich']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print(f"\tI make your {finished_sandwiche.title()}.")
    print(f"\nNext sandwich is {finished_sandwiche.title()}:")
    finished_sandwiches.append(finished_sandwiche)
print(f"\nConfirmed sandwich:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} is prepeard.")


# Solution 7.9
sandwich_orders = ['club sandwich', 'pastrami sandwich', 'grilled cheese sandwich',
                   'BLT Sandwich', 'pastrami sandwich', 'chicken sandwich',
                    'pastrami sandwich', 'tuna sandwich']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()

    if 'pastrami sandwich' in sandwich_orders:
        print("The deil is run out of pastrami sandwich.")

    while 'pastrami sandwich' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')

    print(f"I make your {finished_sandwiche.title()}.")
    finished_sandwiches.append(finished_sandwiche)

print(f"\nConfirmed sandwich:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} is prepeard.")


# Solution 7.10      """I add more code in this problem to compleatly
polling = {}          # understand the nesting of loop and to learn how 
polling_active = True # give data from users and add it to list or dictionaries.
while polling_active:
# Giving input as name.
    while True:
        name = input("Enter your name>>> ")
        
        if name.lower() in polling:
            print("Already taken.")
        else:
            break
# Ask for place as input which lentgth less then 2.
    place = []
    while True:
        prompt = input("If you could visit one or two place in the world,"
                       " where would you go?\n(if you want to go only one place enter place " \
                       "name and then enter okay)>>> ")
        place.append(prompt)
        if len(place) == 2 and prompt == 'okay':
            place.remove('okay')
            break
        elif len(place) > 1:
            break
    # Removing okay from list.
    if 'okay' in place:
        place.remove('okay')
    polling[name] = place 
    repeate = input("want to take another poll (yes/no)>>> ")
    if repeate == 'no' or repeate == 'No':
        polling_active = False
print(polling)



