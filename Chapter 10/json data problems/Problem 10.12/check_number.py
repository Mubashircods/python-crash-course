from pathlib import Path
import json


root = Path("json data problems/Problem 10.11/favorite_number.json")
if root.exists():
    content = root.read_text()
    number = json.loads(content)

    print(f"Your favorite number is {number}")
else:
    prompt = input("Enter your favorite number: ")
    number = json.dumps(prompt)
    root.write_text(number)


