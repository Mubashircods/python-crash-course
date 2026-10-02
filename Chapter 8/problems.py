# Solution 8.1
def display_message():
    print("I'll learn to defining function in this chapter.")

display_message()




# Solution 8.2
def favorite_book(title):
    print(f"One of my favorite book is {title.title()}.")

favorite_book('python crash course')




# Solution 8.3
def make_shirt(size, message):
    print(f"The size of tshirt is {size}.")
    print(f"The message which print on it is {message}.")

make_shirt(8, 'coder')
make_shirt(size= 7, message= 'Alone')




# Solution 8.4
def large_shirt(size = 8, message = 'I love Python'):
    print(f"The size of large shirt is {size}")
    print(f"The message print on it is {message}")

def medium_shirt(size = 6, message = 'I love Python'):
    print(f"The size of medium tshirt is {size}")
    print(f"The message print on it is {message}")

large_shirt()
medium_shirt()





# Solution 8.5
def discribe_city(city, country = 'america'):
    print(f"{city.title()} is in {country.title()}\n")

discribe_city('new yourk')
discribe_city('california')
discribe_city('karachi', 'pakistan')




# Solution 8.6
def city_country(city, country):
    
    city_country_pair = f"{city}, {country}"
    return city_country_pair.title()

citypair = f"{city_country('karachi', 'pakistan')}"
print(citypair.title())
cali = city_country('california', 'america')
print('\n',cali)
san = city_country('san fransisco', 'america')
print("\n",san)



# Solution 8.7
def make_album(artist, title, gazal_number = None):
    if gazal_number:
        album_dic = {'artist': artist.title(), 'title': title.title(), 'number of gazzals': gazal_number}
    else:
        album_dic = {'artist': artist.title(), 'title': title.title()}
    return album_dic


album = make_album('jaun elia', 'shayad')
print('\n',album)
album_1 = make_album("jaun elia", 'lekin')
print("\n", album_1)
album_2 = make_album('allama iqbl', 'khudi')
print('\n',album_2)
album_3 = make_album('jaun elia', 'firnaud', 200)
print('\n',album_3)




# Solution 8.8
while True:
    print("\nEnter 'q' any time to end the program.")
    artist_n = input("Enter artist name:  ")
    if artist_n == 'q':
        break
    album_t = input("Enter album title:  ")
    if album_t == 'q':
        break
    gazzals_num = input("Enter numbers of gassals:  ")
    if gazzals_num == '':
        None
    if gazzals_num == 'q':
        break

    album_0 = make_album(artist_n, album_t, gazzals_num)
    print(album_0)




# Solution 8.9
def display_message(messages):
    for message in messages:
        print('\t',message)


messages = ["Hello!","How are you?","Good morning","Have a nice day","See you soon",
            "Thank you","Welcome","I miss you","Good luck","Take care"]

display_message(messages)




# Solution 8.10
def send_message(messages, sent):
    while messages:
        message_sending = messages.pop()
        sent.append(message_sending)




messages = ["Hello!","How are you?","Good morning","Have a nice day","See you soon",
            "Thank you","Welcome","I miss you","Good luck","Take care"]
sent = []
send_message(messages, sent)
display_message(sent)
print(messages)
print(sent)




# Solution 8.11
messages_ad = ["Hello!","How are you?","Good morning","Have a nice day","See you soon",
            "Thank you","Welcome","I miss you","Good luck","Take care"]
sent_messages = []
send_message(messages_ad[:], sent_messages)
display_message(sent_messages)
print(messages_ad)
print(sent_messages)




# Solution 8.12
def  pizza(*pizzas):
    """Shown the summery of order"""
    print(F"\nYou order this pizzas:")
    for pizza in pizzas:
        print("\t",pizza)

pizza('Tune pizza', 'chese pizza', 'peppirony pizza')
pizza('Tune pizza', 'Normal pizza')
pizza("Tune pizza")




# Solution 8.13
def build_profile(first_name, last_name, **userinfo):
    """This shown my profile."""
    userinfo['first_name'] = first_name
    userinfo['last_name'] = last_name
    return userinfo
my_selfe = build_profile('mubashir', 'Alone', age=17, hoby='programer', goal='AI agent')
print(my_selfe)




# Solution 8.
def make_car(modle, manufactuare, **otherfeature):
    """Make the dictionary about car."""
    otherfeature['modle'] = modle
    otherfeature['manufacturer'] = manufactuare
    return otherfeature
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)