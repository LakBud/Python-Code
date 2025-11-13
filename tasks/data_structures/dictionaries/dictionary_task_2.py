"""Practice accessing nested data inside a dictionary."""

PERSON = {
    "first_name": "Johnny",
    "last_name": "Bang",
    "phone": [
        {"type": "Personal", "number": "47+ 123 456 789"},
        {"type": "Job", "number": "47+ 987 654 321"},
    ],
}


def print_personal_and_job_phone() -> None:
    print(
        f"First name: {PERSON['first_name']} | {PERSON['phone'][1]['type']} Phone Number: {PERSON['phone'][1]['number']}"
    )


def print_all_phone_numbers() -> None:
    print(f"First name: {PERSON['first_name']}")
    print()
    for phone in PERSON["phone"]:
        print(f"Type: {phone['type']:^10} | Number: {phone['number']:^5}")


def main() -> None:
    print()
    print_personal_and_job_phone()
    print()
    print_all_phone_numbers()


if __name__ == "__main__":
    main()
