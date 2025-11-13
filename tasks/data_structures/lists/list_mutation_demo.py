"""Showcase appending, inserting, removing, and sorting elements in a list."""


def display_car_mutations() -> None:
    cars = ["Mercedes", "BMW", "Toyota"]
    print(cars)
    print()

    cars.append("Kia")
    print(cars)

    cars.insert(4, "Bugatti")
    print(cars)
    print()

    cars.remove("Bugatti")
    print(cars)

    deleted_car = cars.pop(0)
    print(cars)
    print()

    bmw = "BMW"
    print(f"Det første treff på \"{bmw}\"  er på index: {cars.index(bmw)}")

    sorted_cars = sorted(cars, reverse=True)
    print(sorted_cars)

    print(f"Det fjernede elementet var: {deleted_car}")


def main() -> None:
    print()
    display_car_mutations()


if __name__ == "__main__":
    main()
