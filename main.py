#Casses and f-string function
first_name = "alone"
second_name = "mubashir"
full_name = f'{first_name} {second_name}!'
greet = f"Hello, {full_name.title()}"
print(greet)

#Exersise No 2.1: Solution
message = "Hi my name is Muhammad Mubashir"
print(message)
#Exersise No 2.2: Solution
new_message = "It is The solution of Problem 2.2"
print(new_message)

#Changing Cases
name = 'muhammad mubashir'
father_name = 'muhammad zafar'
full_name = f"{name.title()} son of {father_name.title()}."
print(name.title())
print(name.upper())
print(name.lower())
print(father_name.title())
print(father_name.upper())
print(full_name)

# Tabes, new line and strips.
message = f"My name is {name.title()}.\nand my hobby is to be a\tHacker "
print(message.strip())

string_for_strip ="         This string show the removing of ident or overspace from both side of this string.     "
print(string_for_strip.strip())

#Uses of tabe and new line.
print("Favorite language:\n\tPython\n\tC\n\tJava")


# Remove prefix
nostarch_url = 'https://www.nostarch.com'
normal_url = f"{nostarch_url.removeprefix('https://')}"
print(normal_url)

# Exersise No 2.3: Solution
name = '"Hello Mubashir,'
message = 'Would you like to learn some Python code today?"'
print(f"{name} {message}")

# Exersise No 2.4: Solution
person_name = "Tony starck"
print(f"{person_name.lower()}. {person_name.upper()}. {person_name.title()}.")

# Exersise 2.5: Solution
famous_quote = 'Albert Einstein once said, "the person who never make a mistake never\ntried anything new."'
print(famous_quote)

# Exersise 2.6: Solution
famous_person = "albert einstein"
message = 'once said, "The person who never make a mistake never\ntried anything new."'
print(f"{famous_person.title()} {message}")

# Exersise 2.7: Solution
person_name = f"   \tjam azhar\n   "
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

# Exersise 2.8: Solution
file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))

# Mathematics in Python
x = 2
y = 3
z = 4
a = 5
b = 0.1
c = 0.2
d = 0.3
print(x + y)
print(y - a)
print(a * x)
print(z / x)
print(a ** x) # Double astrisk is used for power
print(y ** y)
print(b * c)
print(d * a)
print(c / x)
print(b + c)
print(a % x)

# Undercost in number.
universe_age = 1_000_000_000  # undercost is automatically avoided by python.
print(universe_age)

# constants
CONSTANT_NUMBER = 100  #The variable which declared by uppercase called constant.
print(CONSTANT_NUMBER)

# Exersise No 2.9: Solution
print(4+4)
print(10-2)
print(4*2)
print(64/8)

# Exersise No 2.10; solution
favorite_number = 7
message =f"My favorite number is {favorite_number}"
print(message)

import this

