"""Utility functions for exploring a collection of people dictionaries."""

from datetime import date

PEOPLE = [
    {"first_name": "Kevin", "last_name": "Tran", "f_date": "2008-10-19"},
    {"first_name": "Nicolai", "last_name": "Haukefær", "f_date": "2008-12-12"},
    {"first_name": "Barbara", "last_name": "Nilsen", "f_date": "2007-04-13"},
    {"first_name": "Karanveer", "last_name": "Singh", "f_date": "2008-09-13"},
]


def parse_date(value: str) -> date:
    year, month, day = map(int, value.split("-"))
    return date(year, month, day)


def print_age_extremes() -> None:
    age_key = lambda person: parse_date(person["f_date"])
    oldest = min(PEOPLE, key=age_key)
    youngest = max(PEOPLE, key=age_key)

    print(
        f"Oldest = Name: {oldest['first_name']}, Last Name: {oldest['last_name']}, Birthday: {oldest['f_date']}"
    )
    print(
        f"Youngest = Name: {youngest['first_name']}, Last Name: {youngest['last_name']}, Birthday: {youngest['f_date']}"
    )
    print()


def print_sorted_people() -> None:
    age_key = lambda person: parse_date(person["f_date"])
    sorted_people = sorted(PEOPLE, key=age_key, reverse=True)

    for person in sorted_people:
        print(
            f"Name: {person['first_name']:^15} | Last Name: {person['last_name']:^10} | Birthday: {person['f_date']:^10}"
        )


def main() -> None:
    print_age_extremes()
    print_sorted_people()


if __name__ == "__main__":
    main()
