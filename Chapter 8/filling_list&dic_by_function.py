def user_data(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
user_info = user_data('jam', 'mubashir', 17)
print(user_info)


# Getting input for functions
def name_formatted(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    f_name = input("First name: ")
    l_name = input("Last name: ")
    break
formatted_name = name_formatted(f_name, l_name)
print("\nHello, ",formatted_name)




