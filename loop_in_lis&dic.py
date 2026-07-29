unconfirmed_user = ['alice', 'jhon', 'sara','richer']
confirmed_users = []
while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    confirmed_users.append(current_user)
print("The following user sre confirmed.")
for confirm_users in confirmed_users:
    print(confirm_users)


animals = ['cat', 'dog', 'cat', 'dog', 'hamster', 'lion',
           'dear','chithah']
print(animals)
while 'cat' in animals:
    animals.remove('cat')
print(animals)


responces = {}
polling_active = True
while polling_active:
    name = input(f"\nWhat is your name?>>> ")
    responce = input(f"\nWould you like to write python program?>>> ")
    responces[name] = responce
    repeate = input('Would you like to let another person response.(yes/No)>>> ')
    if repeate == 'no' or repeate == 'No':
        polling_active = False
print(responces)

users ={}
user_active = True
while user_active:
    username = input('\nEnter username>>> ')
    first = input('\nEnter first name>>> ')
    last = input('\nEnter last name>>> ')
    age = int(input("What is your age?>>> "))
    users['username'] = username
    users['first'] = first
    users['last'] = last
    users['fullname'] = f"{first.title()} {last.title()}"
    users['age'] = age
    break

for key, value in users.items():
    print(f"{key} is {value}")
print(users)