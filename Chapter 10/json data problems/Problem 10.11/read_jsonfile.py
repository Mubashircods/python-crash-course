from pathlib import Path
import json


root = Path('json data problems/Problem 10.11/favorite_number.json')
content = root.read_text()
number = json.loads(content)
print(f"I know your favorite number! It is {number}")
