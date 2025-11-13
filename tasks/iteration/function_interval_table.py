"""Evaluate a function for a user-provided interval."""


def f(x: int) -> int:
    return x**3 - 2**x + x - 2


def main() -> None:
    print()

    start = int(input("Start x: "))
    end = int(input("Slutt x: "))

    print()
    print()
    for x_value in range(start, end + 1):
        print(f"x: -- {x_value:^8.2f} -- | y: -- {f(x_value):^20.2f} -- ")


if __name__ == "__main__":
    main()
