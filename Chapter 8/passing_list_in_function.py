def greet_user(username):

    for name in username:
        print(f"Hello, {name}")

username = ['jam', 'ch', 'nonserious']
greet_user(username)



unverifyed_users = ['tom', 'zandaya', 'feury', 'starck', 'tony']
verifyed_users = []
while unverifyed_users:
    current_users = unverifyed_users.pop()
    print(f"Verifying user: {current_users}.")

    verifyed_users.append(current_users)

print("This users are verifyed:")
for verifyed_user in verifyed_users:
    print(f"\t{verifyed_user.title()}.")



def user_verification(unverifyed_users, verifyed_users):
    while unverifyed_users:
        current_users = unverifyed_users.pop()
        print(f"Verifying user: {current_users}.")

        verifyed_users.append(current_users)


def confirm_verification(verifyed_users):
    print("This user are verifyed:")
    for verifyed_user in verifyed_users:
        print(f"\t{verifyed_user.title()}")
    


users = ['my', 'name', 'is', 'mubashir', 'and', 'my', 'father', 'name', 'is', 'zaffar']
verify = []
user_verification(users, verify)
confirm_verification(verify)