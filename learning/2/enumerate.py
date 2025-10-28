print()
# ? Enumerate is a built in function/method we can use to add a index into en iterable (list, tuples, strings, etc)

car_list = ["Opel", "VW", "BMW", "Fiat"]

enumerator = enumerate(car_list, start=1) # You can choose which index to set the with start=1. This: 0-1-2-3 becomes: -2-3-4


# Counting all of the elements in a list with for loop
# First alternative (RECOMMENDED)
for index, car in enumerate(car_list, start=1): # The first variable in for decides the index, and the second variable decides the element
    print(f"Index: {index} - Bil: {car}")

print()

# Second alternative
# for i in range(len(car_list)):
#     print(f"Index: {i} - Bil: {car_list[i]}")

print("-----------------" * 3)

