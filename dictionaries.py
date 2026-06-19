founder = {'name': 'mubshir', 'age': 18, 'hight': '6ft',
           'degree': 'matric', 'location': 'dera gabolan'}

print(founder['name'].title())
print(founder['location'].title())

alien_0 = {'color': 'green', 'point': '5'}
earn_point = alien_0['point']
print(f"You can earn {earn_point} points!")
print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)


founder['skin color'] = 'light brownesh wightesh'
print(founder)
print(founder['skin color'])


for found in founder:
    print(found)


user_data = {}

user_data['name'] = 'jhon'
user_data['age'] = 25
user_data['email'] = 'jhon@gmail.com'
print(f'The user name is {user_data["name"].title()}')

user_data['name'] = 'tony starck'
print(f"The updated user name is {user_data['name'].title()}")


