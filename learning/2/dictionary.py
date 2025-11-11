print()

# * Dictionary is a data type used to store data values in key-value pairs
# ? variable = {key:information, key:information}

# person = {"forname":"Buddy", "lastname":"Boy"}


# print(person)
# # To get info from a dictionary, you have to get the key first
# print(f"The information to the key (forname) is: {person['forname']}")

# ---------------------------------------------------------------------------------------------------------

# # ? Change the key
# person["lastname"] = "The Great"
# print(person)

# ---------------------------------------------------------------------------------------------------------

# # ? Add keys into the dictionary
# person["birth-year"] = 1995
# print(person)

# ---------------------------------------------------------------------------------------------------------


# # ? Delete keys in the dictionary (del)
# del person["birth-year"]
# print(person)

# ---------------------------------------------------------------------------------------------------------


# 2) With built-in loops (keys(), value(), )

# car = {"Logo":"VW", "Model":"ID.4", "Km_stand":5000}


# # ? Write out the keys with the use of keys()
# print(car.keys())
# for key in car.keys():
#     print(f"{key:^2}")

# ---------------------------------------------------------------------------------------------------------

# print()
# # ? Write out values with the use of values()
# print(car.values())
# for value in car.values():
#     print(value)

# ---------------------------------------------------------------------------------------------------------

# print()
# # ? Write out the elements with the use of items()
# print(car.items())
# for items in car.items():
#     print(items)

# ---------------------------------------------------------------------------------------------------------

# print()
# # ? Write out list of info in the dictionary

# # 1 method. Use key()
# for key in car.keys():
#     print(f"{key:<10}:{car[key]:>8}")
# print()

# ---------------------------------------------------------------------------------------------------------

# # 2 method. use items()
# for key, value in car.items():
#     print(f"{key:<10}:{value:>8}")

# ---------------------------------------------------------------------------------------------------------







