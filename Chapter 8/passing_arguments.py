def discribe_pet(pet_name, pet_type):

    print(f"\nI have a {pet_type.title()}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

discribe_pet('billu', 'dog')



def get_formited_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

user = get_formited_name('jam', 'mubashir')
print(user)

def formiting_name(first_name, midle_name, last_name):
    full_name = f"{first_name} {midle_name} {last_name}"
    return full_name.title()

user_full_name = formiting_name('jam', 'mubashir', 'alone')
print(user_full_name)

def user_name_formiting(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {last_name} {middle_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

username = user_name_formiting('jam', 'mubashir', 'alone')
username_two = user_name_formiting('jam', 'mubashir')
print(f"{username}\n{username_two}")

