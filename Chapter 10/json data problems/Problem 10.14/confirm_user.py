from pathlib import Path
import json



def get_new_username(root):
    """Prompt for store username"""
    prompt = input("Enter your name: ")
    json_prompt = json.dumps(prompt)
    root.write_text(json_prompt)
    print(f"we'll remember you wen you come back, {prompt}")


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
    username_fun = get_username(root)
    if username_fun:
        prompt = input(f"Is it your correct username '{username_fun}' (yes/no): ")
        if prompt == 'yes':
            print(f"\nWelcome back {username_fun}.")
        else:
            get_new_username(root)
    else:
        name = get_new_username(root)
        print(f"We'll remember your when you come back, {name}!")

root = Path('json data problems/Problem 10.14/username.json')
greet_user(root)



