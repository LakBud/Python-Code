"""Load nested dictionary data from JSON and display it."""

import json
from pathlib import Path

FILE_NAME = Path("learning/2/dictionarys/example.json")


def main() -> None:
    with FILE_NAME.open(encoding="utf-8") as file:
        data: dict = json.load(file)

    print("People in the register:\n")

    for person in data["people"]:
        print(f"First Name: {person['first_name']} | Last Name: {person['last_name']}")
        for phone in person["phone"]:
            print(f"Type: {phone['type']} | Number: {phone['number']}")
        print()  # blank line between people


if __name__ == "__main__":
    main()
