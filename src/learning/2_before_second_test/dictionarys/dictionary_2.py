from operator import itemgetter
print()
# ? You can create lists of dictionarys within a variable
car_list = [{"Logo":"VW", "Model":"ID.4", "Km_state":5000},
            {"Logo":"BMW", "Model":"ID.1", "Km_state":100000},
            {"Logo":"Porche", "Model":"ID.14", "Km_state":2500}] 



# for key in car_list[0].keys():
#     print(f"{key:^11} |", end="")
# print()

# print("-------------" * 3)

# for car in car_list:
#     for value in car.values():
#         print(f"{value:^11} |", end="")
#     print()

# ---------------------------------------------------------------------------------------------------------

# ? Methods for Sorting Dictionarys

# * 1) Bubble-Sort / Manual-sorting

# for i in range(len(car_list)):
#     for j in range(i+1, len(car_list)):
#         if car_list[i]["Km_state"] > car_list[j]["Km_state"]:
#             a,b = car_list[i]["Km_state"], car_list[j]["Km_state"] #Tuples are recommended to use here
#             car_list[i]["Km_state"], car_list[j]["Km_state"] = b, a #Changes the variable values with eachother

# print(car_list)

# ---

# * 2) Lamba Function with Sorted

# car_km_state = lambda car: car["Km_state"]

# sorted_car_list = sorted(car_list, key=car_km_state)
# print(*sorted_car_list, sep="\n")

# ---

# # * 3) Itemgetter()
# sorted_car_list = sorted(car_list, key=itemgetter("Km_state"))
# print(*sorted_car_list, sep="\n")

# ---------------------------------------------------------------------------------------------------------

# ? Finding the biggest and smallest element in a dictionary

# * 1) Bubble-Sort / Manual-sorting

# # Start by assuming the first car is both smallest and biggest
# smallest = car_list[0]
# biggest = car_list[0]

# # Loop through all cars to find the true smallest and biggest
# for car in car_list:
#     if car["Km_state"] < smallest["Km_state"]:
#         smallest = car
#     if car["Km_state"] > biggest["Km_state"]:
#         biggest = car

# print("Car with smallest Km_state:", smallest)
# print("Car with biggest Km_state:", biggest)


# ---

# * 2) Lambda function

# car_km_state = lambda car: car["Km_state"]

# car_droven_most = max(car_list, key=car_km_state)
# car_droven_less = min(car_list, key=car_km_state)

# print(f"{car_droven_most = }") # The = sign makes it print out the variable = value
# print(f"{car_droven_less = }")

# ---

# * 3) Itemgetter()

# car_droven_most = max(car_list, key=itemgetter("Km_state"))
# car_droven_less = min(car_list, key=itemgetter("Km_state"))

# print(f"{car_droven_most = }") # The = sign makes it print out the variable = value
# print(f"{car_droven_less = }")

