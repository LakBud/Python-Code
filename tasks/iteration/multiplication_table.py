"""Print a 10x10 multiplication table."""


def main() -> None:
    print()
    for row in range(1, 11):
        for column in range(1, 11):
            print(f"{row * column:4}", end="")
        print()


if __name__ == "__main__":
    main()
