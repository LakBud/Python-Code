import json

file_name: str = "learning/2/dictionarys/example.json"

with open(file_name, encoding="utf-8") as file:
    data: dict = json.load(file)

print("People in the register:\n")

people: list = data["people"]

for person in people:
    print(f"First Name: {person['first_name']} | Last Name: {person['last_name']}")
    for phone in person["phone"]:
        print(f"Type: {phone['type']} | Number: {phone['number']}")
    print()  # blank line between people
