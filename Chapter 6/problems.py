# Solution 6.1
college_friend_1 = {
    'first': 'hamza',
    'last': 'Rajpoot',
    'age': 16,
  # 'city': 'jetha bhutta'          Commented due to problem 6.7
}

full_name = f"{college_friend_1['first']} {college_friend_1['last']}"
print(full_name.title())
print(college_friend_1['age'])
# print(college_friend_1['city'].title())          Commented due to problem 6.7


# Solution 6.2
favorite_numbers = {         # This dictionary is edit due to problem 6.10
    'my': [1, 7,],           # Changes (convert single integer into integer list.)
    'mudasir': [5, 9],
    'hamza': [3, 6],
    'mehreen': [4, 8],
    'mujahid': [2, 5],
    'muqaddas': [4, 8],
    'hassnain': [2, 7],
    'tehseen': [9, 3], 
}
print(favorite_numbers)
numbers = f"My: {favorite_numbers['my']}\nMudasir: {favorite_numbers['mudasir']}"
second_n = f"\nHamza: {favorite_numbers['hamza']}\nMehreen: {favorite_numbers['mehreen']}"
third_n = f"\nMujahid: {favorite_numbers['mujahid']}\nMuqaddas: {favorite_numbers['muqaddas']}"
fourth_n = f"\nHassnani: {favorite_numbers['hassnain']}\nTehseen: {favorite_numbers['tehseen']}"
print(numbers + second_n + third_n + fourth_n)


# Solution 6.3 | 6.4
python_basics = {
    'print': 'print: It is a function which is used to call variabels and other functions.',
    'variabels': 'variables: It is like a box in which data is stored.',
    'list': 'list: It is also a variable in which large data is stored',
    'if statement': 'if statement: It is used to make the condition in program.',
    'dictionaries': 'dictionaries: It is also a like a box in which many sets of data stored.',
    'sorted()': 'sorted(): It is uset to temporary sort the list and dictionaries.',
    'insert()': 'insert(): It is used to add item in list.',
    'removeprefix()': 'removeprefix(): It is used to remove prefix like https://',
    'set()': 'set(): It is used to remove the equal words in dictionaries.',
    'elif:': 'elif: It is used to implify many conditions.',
}
for k, v in python_basics.items():
    print(f"\n{k.title()}:")
    print(f"\t{v}")

# Solution 6.5

rivers = {
    'neil': 'egypt',
    'indus': 'pakistan',
    'ganga': 'india',
    'jahlim': 'kpk',
}
for river, location in rivers.items():
    print(f"\n{river.title()} run through {location.title()}")

for River in rivers.keys():
    print(River.title())
print("\n")
for country in rivers.values():
    print(country.title())

# Solution 6.6
favorite_language = {
    'ayesha': 'python',
    'arham': 'c',
    'huzaifa': 'rust',
    'maryam': 'pyhton',
}
polltake_persons = ['ayesha', 'maryam', 'sara', 'hasnain', 'huzaifa', 'khalid']
for polltake_person in polltake_persons:
    if polltake_person in favorite_language:
        print(f"{polltake_person.title()}! Thank you for taking the poll.")
    else:
        print(f"{polltake_person.title()}! I'm very thankful to you if you take the poll.")
    
# Solurion 6.7
college_friend_0 = {
    'first': 'chaudhary',
    'last': 'umar',
    'age': 15
    }
college_friend_2 = {
    'first': 'mubashir',
    'last': 'pathan',
    'age': 17
}
college_friends = [college_friend_0, college_friend_1, college_friend_2]
for college_friend in college_friends:
    print(f'\n{college_friend}')


# Solution 6.8
pet_0 = {
    'pet_type': 'dog',
    'owner': 'peter',
    'color': 'light brown'
}
pet_1 = {
    'pet_type': 'cat',
    'owner': 'tom',
    'color': 'white',
}
pet_2 = {
    'pet_type': 'humster',
    'owner': 'harry',
    'color': 'black and white'
}
pets = [pet_0, pet_1, pet_2]
for pet in pets[:]:
    for about, info in pet.items():
        print(f"{about}: {info}\n")


# Solution 6.9
favorite_place = {
    'harry': 'kelash',
    'tom': 'iceland',
    'zandaya': 'norway'
}
for name, place in favorite_place.items():
    print(f"Hello {name}! are you tell me your favorite place?")
    print(f"The favorite place of {name.title()} is:\n\t\t\t{place.title()}\n")


# Solution 6.10
for person, numbers in favorite_numbers.items():
    print(f"The favorite number of {person.title()}:")
    for number in numbers:
        print(f"\t\t {number}")


# Solution 6.11
cities = {
    'new yourk': {
        'country': 'america',
        'population': '~70M',
        'fact': 'city of rich people'
    },
    'honk kong': {
        'country': 'chaina',
        'population': '~90M',
        'fact': 'Whitesh persons'
    },
    'lahore': {
        'country': 'pakistan',
        'population': '~25M',
        'fact': 'Discipline'
    }
}

for city, information in cities.items():
    print(f"\nCity name:\n\t{city.title()}\nInformation:")
    for key, value in information.items():
        print(f"\t{key.title()}: \n\t\t{value.title()}")

# Solution 6.12

"""This Problem Alredy Solved."""

