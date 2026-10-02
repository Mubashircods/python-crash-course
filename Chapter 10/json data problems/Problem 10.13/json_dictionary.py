from pathlib import Path
import json


root = Path("json data problems/Problem 10.13/user_data.json")
if root.exists():
    content = root.read_text()
    user_info = json.loads(content)
    print("Your information is stored.\nSee your information:")
    for k, v in user_info.items():
        print(f"\t{k} : {v}")
else:
    user_info = {}
    first_name_prompt = input("Enter your first name: ")
    last_name_prompt = input("Enter your last name: ")
    age_prompt = input("Enter your age: ")

    user_info['first_name'] = first_name_prompt
    user_info['last_name'] = last_name_prompt
    user_info['age'] = age_prompt
    user_info = json.dumps(user_info)
    root.write_text(user_info)
    print(f"We'll remember your information when you come back, {first_name_prompt.title()}!")


