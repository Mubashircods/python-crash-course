age = int(input("How old are you? "))
print(age)

height = int(input("Tell your height in inches: "))
if height >= 48:
    print("\nYou're tall enough to ride.")
else:
    print(f"You're be able to ride when you are a littlr older.")

number = int(input("Enter a number and I'll tell you if it's even or old: "))
if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")


