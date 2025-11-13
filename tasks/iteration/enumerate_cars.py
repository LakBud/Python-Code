"""Demonstrate ``enumerate`` when iterating over a list of cars."""

CARS = ["BMW", "KIA", "MERCEDES", "LAMBORGHINI"]


def main() -> None:
    print()
    for index, car in enumerate(CARS, start=1):
        print(f"Index: {index} - Car: {car}")


if __name__ == "__main__":
    main()
