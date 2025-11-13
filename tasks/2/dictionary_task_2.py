print()
person = {
        "first_name": "Johnny",
        "last_name": "Bang",
        
        "phone": [
            {"type": "Personal", "number": "47+ 123 456 789"},
            {"type": "Job", "number": "47+ 987 654 321"},
                ]
        }

# 1)
print(f"First name: {person["first_name"]} | {person["phone"][1]["type"]} Phone Number: {person["phone"][1]["number"]}")
print()


# 2)
print(f"First name: {person["first_name"]}")
print()

for phone in person["phone"]:
    print(f"Type: {phone["type"]:^10} | Number: {phone["number"]:^5}")