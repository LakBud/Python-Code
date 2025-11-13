"""Demonstrate indexing and slicing on a list of electric car brands."""

EL_CAR_BRANDS = ["Tesla", "BYD", "VW", "BMW", "Voyah", "Opel", "XPeng"]


def main() -> None:
    """Print a handful of indexing examples."""
    print()
    print(EL_CAR_BRANDS[3])
    print(EL_CAR_BRANDS[-2])
    print(EL_CAR_BRANDS[::2])
    print(EL_CAR_BRANDS[3:7])
    print(EL_CAR_BRANDS[-2::-4])


if __name__ == "__main__":
    main()
