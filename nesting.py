# Making empty list
aliens = []
# making 30 aliens
for alien_number in range (30):
    new_alien = {'color': 'green', 'point': '5', 'speed': 'slow'}
    aliens.append(new_alien)
# changing alien values
for alien in aliens[10:]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'

# changing alien values
for alien in aliens[20:]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'

# Loop through aliens
for alien in aliens:
    print(alien)

    





users = []
for user in range(50):
    new_user = {
        'username': '@freecodecamp',
        'first': 'free',
        'last': 'codecamp',
        'subscriber': '11.2M'
    }
    users.append(new_user)
for User in users[:5]:
    print(User)
print('...')
print(f"Totle user is {len(users)}")




burgers = {
    'burger_1': 'egg burger',
    'toppings_1': ['less catchub', 'more slaad', 'double egg'],
    'price_1': 150,
    'burger_2': 'chicken burger',
    'toppings_2': ['more catchub', 'less slaad', 'more chicken'],
    'price_2': 180
}

print(f"You orderd {burgers['burger_1'].title()} "
      "with the following toppings:")
for tooping in burgers['toppings_1']:
    print(f'\t{tooping.title()}')



favorite_languages = {
    'jhon': ['python', 'rust', 'dart'],
    'saira': ['perl'],
    'donald': ['c', 'java'],
    'starck': ['javaScript']   
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\nThe favorite language of {name.title()} is:")
        for language in languages:
            print(f"\t{language.title()}")
    else: 
        print(f"\nThe favorite language of {name.title()} is {language.title()}.")


custmers = {
    'gourje': {
        'first': 'gourje',
        'last': 'josouf',
        'age': 20
    },
    'william': {
        'first': 'edward',
        'last': 'william',
        'age': 32
    },
    'harword': {
        'first': 'harword',
        'last': 'starck',
        'age': 19
    }
}
print(f"\nMy First custmers are:")
for username, user_info in custmers.items():
    print(f"\t Username:{username.lower()}")
    fullname = f"{user_info['first']} {user_info['last']}"
    age = user_info['age']
    print(f"\t\tfullname:{fullname.title()}\n\t\tage:{age}\n")


