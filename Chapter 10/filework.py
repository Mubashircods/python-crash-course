from pathlib import Path


path = Path("pi_million.txt")
content = path.read_text()


pi_string = ''
for line in content.splitlines():
    pi_string += line.lstrip()
print(f"{pi_string[:50]}...")
print(len(pi_string))

birthday_date = input("Enter your birthday date in the formate (ddmmyyyy):   ")
if birthday_date in pi_string:
    print("Your birthdy is appear in the first million digit of pi digits.")
else:
    print("Your birthy isn't appear in the first million pi digits.")


"""This meathod is learned in solution 10.2"""
message = "I don't love dogs"
print(message)
print(message.replace('dogs', 'cats'))
"""Not a part of file and exception programing but of strings
and string is also a major part of file and exceptions programing."""




