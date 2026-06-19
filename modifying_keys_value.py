alien_1 = {'color': 'green', 'x-position': 0, 'y-position': 25, 'speed': 'medium'}
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print(f"The first x-position of alien_1 is {alien_1['x-position']}")
alien_1['x-position'] = alien_1['x-position'] + x_increment
print(f"The new x-position of alien_1 is {alien_1['x-position']}")



user = {'name': 'tony starck', 'age': 20, 'days': 100, 'follower': 0  , 'views': 0}
if 0 <= user['days'] <=  10:
    new_views = 110
    new_followers = 25
elif 11 <= user['days'] <= 50:
    new_views = 300
    new_followers = 150
elif 50 < user['days'] <= 80:
    new_views = 750
    new_followers = 500
elif 80  < user['days'] <= 120:
    new_views = 10000
    new_followers = 2000
else:
    new_views = 100000
    new_followers = 10000
user['follower'] = user['follower'] + new_followers
user['views'] = user['views'] + new_views
print(f"Your current follers is {user['follower']}")
print(f"Your current views per video is {user['views']}")

# Removing key-value pair in dictionaries
del user['age']
print(user)

# using get() methode
favorite_language = {
    'my' : 'python',
    'shazia': 'c++',
    'arham': 'html',
    'mehreen': 'css',
    'hassan': 'rust',
  # 'sarfaraz': 'c#',
}
language = favorite_language['shazia'].upper()
print(f"Favorite language of shazia is {language}")
sarfaraz_language = favorite_language.get('sarfaraz', "No sarfaraz value assaigned")
print(sarfaraz_language)

for name, language in favorite_language.items():
    print(f"\nThe favorite language of {name.title()} is {language.title()}")
