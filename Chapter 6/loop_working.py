user_0 = {
    'username': 'jripper',
    'first': 'jhon',
    'last': 'ripper',
}
for k, v in user_0.items():
    print(f"\n{k}:")
    print(v)


favorite_language = {
    'sara': 'python',
    'arham': 'perl',
    'mehreen': 'C',
    'sahil': 'python',
    'samreen': 'java'
}
friends = {'sara', 'sahil'}

for name in favorite_language.keys():
    print(f"Hi {name}!")
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}! I see you love {language.title()}.")
    elif 'waleed' not in favorite_language.keys():
        print(f"waleed! Please pik a poll.\n")

    for n in sorted(favorite_language.keys()):
        print(f"{n.title()}, thaank you for taking poll.")
sorted(favorite_language.items())
print("\nFavorite languages of some persons")
for key, value in favorite_language.items():
    print(f"\n{key.title()}:")
    print(f"\t{value.title()}")

print(f"The following languages hase been mentioned.")
for languages in set(favorite_language.values()):
    print(languages.title())


