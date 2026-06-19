# LIST
friends = ['waleed','umar', 'mubashir', 'hamza']
print(friends[0].upper())

message = "My best friend is"
second_message = 'And my another friends is'
print(f"{message} {friends[0].title()}. {second_message} {friends[1].lower()} & {friends[3].title()}")

# Problem No 3.1: Solution
names = ['waleed', 'hammad', 'mujahid', 'shoaib']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

names_prints = f"{names[0]}\n{names[1]}\n{names[2]}\n{names[3]}" #2nd method.
print(names_prints)

# Problem No 3.2: Solution
message = "I want to meat you my friend"
print(f"{message} {names[0]}\n{message} {names[1]}\n{message} {names[2]}\n{message} {names[3]}")

# Problem No 3.3: Solution
transportation =['ev bike', '110 CC', 'honda civic', 'rolse royce']

m_for_ev = "I wanna buy 125"
m_for_cc = "if money is come to me i get"
m_for_honda = "if i'm a rich person, so i want to by"
m_for_rolse = "if i become a bolloinear i buy many"

print(f"{m_for_ev} {transportation[0].title()}.\n{m_for_cc} {transportation[1]}.")
print(f"{m_for_honda} {transportation[2].title()}.\n{m_for_rolse} {transportation[3].title()}s.")

# Modification of list
motersicle =['honda', 'yahama', '125 honda']
motersicle.append('suzuki')
print(motersicle)

motersicle_2 = ['honda','yahama','125 honda']
motersicle_2.insert(2, 'suzuki')
print(motersicle_2)

del motersicle_2[2]
print(motersicle_2)


cares = ['honda civic', 'honda city', 'porche', 'bughati shirone', 'tesla modle s plade', 'rolse royce la rose noire']
cares.remove('porche')
print(cares)

poped_cares = cares.pop(4)
print(cares)
print(poped_cares)


# Problem No 3.4: solution
guest = ['mubshir', 'umar', 'hamza']

guest_greet = "Hello Friend"
guest_message = "I want that tonight you come to me for dinner."
invitation = f"{guest_greet} {guest[0].title()},{guest_message}\n{guest_greet} {guest[1].title()},{guest_message}\n{guest_greet} {guest[2].title()},{guest_message}"
print(invitation)

# Problem 3.5 Continue to 3.4
print(f"{guest[1].title()} not make the dinner.")

guest[1] = 'mudasir'
invitation = f"{guest_greet} {guest[0].title()},{guest_message}\n{guest_greet} {guest[1].title()},{guest_message}\n{guest_greet} {guest[2].title()},{guest_message}"
print(invitation)

# Problem 3.6 conrinue by previous exersize.
guest.insert(0, 'azhar')
guest.insert(2, 'hammad')
guest.append('mujahid')

invitation_insert_list = f"{guest_greet} {guest[0].title()},{guest_message}\n{guest_greet} {guest[1].title()},{guest_message}\n{guest_greet} {guest[2].title()},{guest_message}"
invitation_insert_list_2 = f"{guest_greet} {guest[3].title()},{guest_message}\n{guest_greet} {guest[4].title()},{guest_message}\n{guest_greet} {guest[5].title()},{guest_message}"
print(invitation_insert_list)
print(invitation_insert_list_2)

# Problem No 3.7 continued to 3.6: Solution

print(f"Sorry friends {guest}! I can invite only two people to dinner.")
azhar_pop = guest.pop(0)
print(f"I'm Very sorry {azhar_pop}! I can't invite you for dinner.")
mubashir_pop = guest.pop(0)
print(f"I'm Very sorry {mubashir_pop}! I can't invite you for dinner.")
hammad_pop = guest.pop(0)
print(f"I'm Very sorry {hammad_pop}! I can't invite you for dinner.")
mujahid_pop = guest.pop()
print(f"I'm Very sorry {mujahid_pop}! I can't invite you for dinner.")

remain_invitation = "you're still invited."
print(f"{guest[0].title()}! {remain_invitation}\n{guest[1].title()}! {remain_invitation}")

del guest[0]
del guest[0]
print(guest)

# Sort the list.
hobies = ['bmw', 'toyota', 'porsch', 'audi', 'ferrary']
hobies.sort()
print(hobies)

hoby = ['bmw', 'toyota', 'porsch', 'audi', 'ferrary']
print(sorted(hoby))

print(f'\nHear is a original list')
print(hoby)
print(f'\nHear is a sorted list')
print(sorted(hoby))
print(f'\nhear is again original list')
print(hoby)

hoby.reverse()
print(hoby)

# Finding length
length = len(hoby)
print(length)

# Problem No 3.8: Solution
favorite_location = ['Austrelia', 'Chaina', 'British', 'Newzeeland', 'Koria']
print(favorite_location)

print(sorted(favorite_location))

print(favorite_location)

favorite_location.reverse()
print(favorite_location)


favorite_location.reverse()
print(favorite_location)

favorite_location.sort()
print(favorite_location)

favorite_location.sort(reverse = True)
print(favorite_location)

# Problem No 3.9: Solution
print(len(guest))

# Problem No 3.10: Solution
problem_list = ['friends', 'relatives', 'lifepartner', 'guest', 'enimies']
problem_list.insert(-1, 'love')
problem_list.sort()
poped_enimies = problem_list.pop(0)
problem_list.remove('guest')
problem_message = f'The first priority of list is {problem_list[0].title()}'
problem_m_n =f'Then next Priority'
problem_local_loop = f'{problem_m_n} {problem_list[1]}\n{problem_m_n} {problem_list[2].title()}\n{problem_m_n} {problem_list[3].title()}'

print(f'{problem_message}\n{problem_local_loop}')
