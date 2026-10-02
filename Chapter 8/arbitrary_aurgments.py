def making_pizza(*toppings):

    print("\nMaking the pizza with following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")


making_pizza('cheese', 'mashroom', 'chicken')


def pet_info( name, *charectristics):
    """This function show the chsrsctristic of of dog.
    It has two positional aurgment and one arbitrary aurgment."""
    print(F"\nMy pet name is {name} and their charectristic is:")
    for charectristic in charectristics:
        print(f"\t{charectristic}")


pet_info('billu', 'Dog', 'brown', 'pista', '2 year')



def user_information(first_name, last_name, **user_info):
    "This store the information of user in dictionary"
    user_info['first name'] = first_name
    user_info['last name'] = last_name

    return user_info

my_profile = user_information('jam', 'mubashir', age=17, color='white brownish')
print(my_profile)





