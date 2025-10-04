
# ? 1)

even_number_list = list(range(2, 101, 2))
odd_number_list = list(range(1, 101, 2)) 

print()
print(even_number_list)
print()
print(odd_number_list)

print("------------------------------------------------")

# ? 2)

elcar_list = ["Tesla", "BYD", "VW", "BMW", "Voyah", "Opel", "XPeng"]

print()
print(elcar_list[3])
print(elcar_list[-2])
print(elcar_list[::2])
print(elcar_list[3:7])
print(elcar_list[-2::-4])

print("------------------------------------------------")


# ? 3)

car_list = ["Mercedes", "BMW", "Toyota"]
print(car_list)

print()

# Add
car_list.append("Kia")
print(car_list)
car_list.insert(4, "Bugatti")
print(car_list)

print()

# Remove 
car_list.remove("Bugatti")
print(car_list)
deleted_car_element = car_list.pop(0)
print(car_list)

print()

bmw = "BMW"

print(f"Det første treff på \"{bmw}\"  er på index: {car_list.index(bmw)}")

sorted_car_list = sorted(car_list)
sorted_car_list.reverse()
print(sorted_car_list)