


from pathlib import Path
import json

prompt = input("Enter your favorite number: ")
number = []

path = Path('json data problems/Problem 10.11/favorite_number.json')
write = json.dumps(prompt)
path.write_text(write)