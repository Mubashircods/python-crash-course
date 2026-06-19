#Loop through list.l
colleges =['al barkat', 'alpine', 'grace', 'punjab']
for college in colleges:
    print(f'{college.title()} College is best.')
    print(f"I can't wait to go {college.title()}\n")

print(f"Thankyou! You all are helped me to build my carear.\n")

"""
Indentation Error
indt = ['mubashir','mudasir', 'muhammad','zaffar']
for int in indt:
print(int)

Over Indtation Error
greet = "Hello! how are you?"
    print(greet)
"""


# Problem No 4.1: Solution
favorite_pizza = ['pepperoni pizza', 'cheez pizza', 'chicken pizza']
for pizza in favorite_pizza:
    print(pizza.title())
    print(f"I like {pizza.title()}.\n")
print(f"I dont eat pizza but unfortunily i write about pizza because my sir ask me that i write three lines on pizza.\n"
      f" I dont eat pizza. One day i eat {favorite_pizza[2].title()} only two bite and just in some secondes i feel\n "
      f"womating and feel gilty. I want to eat it but my stomach don't bear pizza. I don't now how i treet it, But i try!\n")

# Problem No 4.2: Solution
animals = ['lion', 'lepard', 'tiger']
for animal in animals:
    ability = "is a brave Animal"
    print(f"{animal.title()} {ability}\n")
print(f"These animals are the greet pets for rich peoples\n")

# Numbers lists.
numbers = list(range(0, 51,2))
for n in numbers:
    n = n * 2
    print(f"{n}")

# Geeting Sequare printing by list loop.
squares = [9]
for value in squares:
    squares = value  ** 2
    print(squares)


# Temporary Square.
square = []
for value in range(1,11):
    square.append(value ** 2)
print(min(square))
print(max(square))
print(sum(square))

squ = [value ** 2 for value in range(1, 11)]
print(squ)


# Problem 4.3: SOlution
problem_number = list(range(1,21))
for num in problem_number:
    print(num)
print(problem_number)

# Problem 4.4: Solution
one_million_number = list(range(1, 1000001))
for M in one_million_number:
    print(M)
   
# Problem No 4.5: Solution
sum_of_1m = list(range(1,1000001))
print(min(sum_of_1m))
print(max(sum_of_1m))
print(sum(sum_of_1m))

# Problem No 4.6: Solution
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)


# Problem No 4.7: Solution
threes = []
for value in range(1,11):
    threes = value * 3
    print(threes)


# Problem No 4.8: SOlution
cub = []
for value in range(1,11):
    cub = value ** 3
    print(cub)

# Problem No 4.9: Solution

ten_cub = [mult ** 3 for mult in range(1,11)]
print(ten_cub)


# Working through slice in list

my_food = ['burger', 'ice cream', 'biryani', 'chicken rost', 'white karahi']
print(my_food[1:4])
print(my_food[3:])
print(my_food[:])


friend_food = my_food[:]

friend_food.append('Chicken samoosas')
del friend_food[3]
print(friend_food)


print(f"My favorite food is\n\t{my_food}")
print(f"My friend favorite food is\n\t{friend_food}")

# Self Test
foods =['chicken', 'lentils', 'cauliflower', 'minced meat']
for food in foods[1:4]:
    print(food)

# Problem No 4.10: Solution
favorite_pizzas = ['pepperoni pizza', 'cheez pizza', 'chicken pizza','normal pizza','cream pizza']
for pizzas in favorite_pizzas:
    print(pizzas.title())
    print(f"I like {pizzas.title()}.\n")
print(f"Print first three item in the list are\n\t{favorite_pizzas[:3]}")
print(f"Three items from the midle of list are\n\t{favorite_pizzas[1:4]}")
print(f"Print last three item in the list are\n\t{favorite_pizzas[2:5]}")


# Problem No 4.11: Solution
favorite_food_pizza = ['pepperoni pizza', 'cheez pizza', 'chicken pizza']
for food_pizzas in favorite_food_pizza:
    print(food_pizzas.title())
    print(f"I like {food_pizzas.title()}.\n")
my_friend_pizza = favorite_food_pizza[:]
favorite_food_pizza.append('creem pizza')
my_friend_pizza.insert(2, 'normal pizza')
print(f'My pizzas are;\n{favorite_food_pizza}')
for f_pizza in favorite_food_pizza:
    print(f_pizza.title())
print(f"My friend favorite pizzas are;\n{my_friend_pizza}")
for my_f_pizza in my_friend_pizza:
    print(my_f_pizza.title())


# Problem No 4.12: SOlution
my_food_p = ['chicken', 'bread', 'burger']

friend_food_p = my_food_p[:]

my_food_p.insert(0, "roti")
friend_food_p.append('yoguart')
print("My favorite foods are;")
for food_p in my_food_p:
    print(f"{food_p.title()}\n")

print("My friend favorite foods are;")
for friend_p in friend_food_p:
    print(f'{friend_p.title()}\n')

# Introduction to tuple.

angles = (90,180,270,360)
for angle in angles[1:3]:
    print(angle)



# Problem No 4.13: Solution

buffet_food = ('roti', 'chicken', 'ciliflower', 'burger', 'meat')
# buffet_food[0] = 'chicken rost'
buffet_food = ('chicken rost', 'pizza', 'coliflower', 'burger', 'meat')
for b_food in buffet_food:
    print(b_food)

# Problem 4.14-15: Solution
"""Visit this web page;

https://python.org/dev/peps/pep-0008
"""

