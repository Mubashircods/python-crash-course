from pathlib import Path
import json


# numbers = [0,1,2,3,4,5,6,7,8,9]

# path = Path('number.json')
# content = json.dumps(numbers)
# path.write_text(content)

# content_read = path.read_text()
# json_formate_read = json.loads(content_read)
# print(json_formate_read)



# # Write json formate data in file by prompt meathod.
# prompt = input("Enter your name: ")
# username = (prompt)

# name_path = Path('username.json')
# name_json_formate = json.dumps(username)
# name_path.write_text(name_json_formate.title())
# print(f"Name store compleate.\nConfirm your name.\nYour name is {username.title()}.")


# # Read json formate data meathod
# read_file = name_path.read_text()
# convert_formate = json.loads(read_file)
# print(f"\nWelcome back {convert_formate}.")


# # Checking if the file is exist or not.
# patH = Path('username.json')
# if patH.exists():
#     read_content = patH.read_text()
#     json_read = json.loads(read_content)
#     print(f"\nWelcome {json_read}.")
# else:
#     prompt_users = input("Enter your name: ")
#     name = prompt_users
#     json_formate = json.dumps(name)
#     patH.write_text(json_formate)
#     print(f"We'll remember your when you come back, {name}!")


# Creat the function
def get_new_username(root):
    """Prompt for store username"""
    prompt = input("Enter your name: ")
    json_prompt = json.dumps(prompt)
    root.write_text(json_prompt)


def get_username(path):
    """Get stored username If available."""
    if path.exists():
        content = path.read_text()
        json_content = json.loads(content)
        return json_content
    else:
        return None


def greet_user(root):
    """Great 'if exist' or store the user name in your liked path."""
    PATh = root
    username_fun = get_username(PATh)
    if username_fun:
        print(f"\nWelcome back {username_fun}.")
    else:
        name = get_new_username(root)
        print(f"We'll remember your when you come back, {name}!")

root = Path('name.json')
greet_user(root)








