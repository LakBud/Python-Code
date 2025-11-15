print()

peoples: list = [
                {"first_name": "Kevy", "last_name": "Tran", "f_date": "2008-10-19"}, 
                {"first_name": "Nico", "last_name": "Haukefær", "f_date": "2008-12-12"}, 
                {"first_name": "Barbie", "last_name": "Nilsen", "f_date": "2007-04-13"}, 
                {"first_name": "Jackson", "last_name": "Singh", "f_date": "2008-09-13"},
                ]



peoples_age: str = lambda peoples: peoples["f_date"]

oldest: str = min(peoples, key=peoples_age)
youngest: str = max(peoples, key=peoples_age)

print(f"Oldest = Name: {oldest["first_name"]}, Last Name: {oldest["last_name"]}, Birthday: {oldest["f_date"]}")
print(f"Youngest = Name: {youngest["first_name"]}, Last Name: {youngest["last_name"]}, Birthday: {youngest["f_date"]} ")
print()


sorted_peoples_list: list = sorted(peoples, key=peoples_age, reverse=True)


# Method 1
# for i in range(len(sorted_peoples_list)):
#     print(f"Name: {sorted_peoples_list[i]["first_name"]:^15} | Last Name: {sorted_peoples_list[i]["last_name"]:^10} | Birthday: {sorted_peoples_list[i]["f_date"]:^10}")
    
# Method 2 (recommended)
for people in sorted_peoples_list:
    print(f"{people["first_name"]:>10} | Last Name: {people["last_name"]:^10} | Birthday: {people["f_date"]:^10}")


