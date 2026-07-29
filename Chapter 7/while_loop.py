count = 1
while count <= 5:
    print(count)
    count += 1


prompt = "\nTell me anything and i'll return write that for you" \
"\nEnter 'quit' to end the program>>> "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message.title())


prompt_0 = "\nEnter any thing and i will write it for you."

active = True
while active:
    num = int(input('Enter a age>>> '))

    if num >= 18:
        active = False
        print("Enjoye this content.")
    else:
        print("You're not old enough.\nPlease enter walid age.")


while True:
    ask = input("What would you like?\n(Enter 'quit' to close the program)>>> ")
    if ask == 'quit':
        break
    else:
        print(f"\nHmm, you like {ask.title()}.\n")


number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


# current_number = 1
# while current_number <= 5:
#     print(1)        (# This is infinity loop.)



