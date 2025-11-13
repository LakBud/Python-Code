"""Create a checkerboard pattern using alternating "X" and "O" characters."""


def build_checkerboard(rows: int, columns: int) -> list[str]:
    """Return a flat list representing a checkerboard pattern."""
    pattern: list[str] = []
    for row in range(rows):
        for col in range(columns):
            pattern.append("X" if (row + col) % 2 == 0 else "O")
    return pattern


def display_checkerboard(pattern: list[str], columns: int) -> None:
    """Print the checkerboard using the provided column width."""
    for index, value in enumerate(pattern):
        if index % columns == 0:
            if index != 0:
                print()
        print(f"{value:^2}", end="")
    print()


def main() -> None:
    rows = int(input("How many rows do you want: "))
    columns = int(input("How many columns do you want: "))
    print()

    pattern = build_checkerboard(rows, columns)
    display_checkerboard(pattern, columns)


if __name__ == "__main__":
    main()
