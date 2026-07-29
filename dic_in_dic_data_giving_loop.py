users = {}
user_activit = True
while user_activit:
    while True:
        username = input("Enter your username>>> ")
        if username.lower() in users:
            print("Already taken")
        else:
            break
    user_info = {}
    first = input("Enter your first name>>> ")
    last = input("Enter your last name>>> ")
    age = int(input("Enter your age>>> "))
    user_info['first'] = first
    user_info['last'] = last
    user_info['age'] = age
    users[username.lower()] = user_info
    new_user = input("Are you add another user?(yes/no) ")
    if new_user == 'no' or new_user == 'No':
        user_activit = False
print(users)