print()
# Task 1)

cars: list = [
    {"car_logo": "BMW", "KM_status": 320932093, "Price": 250000 },
    {"car_logo": "Mercedes", "KM_status": 2303, "Price": 120120 },
    {"car_logo": "Kia", "KM_status": 320, "Price": 3293 },
            ]

cars[0]["model"] = "M5"

for key in cars[0].keys():
    print(f"{key:^20} | ", end="")
print()

print("-----------------------" * len(cars[0].keys()))


for car in cars:
    for value in car.values():
        print(f"{value:^20} | ", end="")
    print()