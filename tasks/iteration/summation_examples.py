"""Compare summation using ``for`` and ``while`` loops."""


def sum_with_for(limit: int) -> int:
    total = 0
    for value in range(limit + 1):
        total += value
    return total


def sum_with_while(limit: int) -> int:
    counter = 0
    total = 0
    while counter < limit:
        counter += 1
        total += counter
    return total


def main() -> None:
    limit_for = int(input("Hvor mange heltall skal summeres (for-løkke): "))
    print(sum_with_for(limit_for))

    print()

    limit_while = int(input("Hvor mange heltall skal summeres (while-løkke): "))
    print(sum_with_while(limit_while))


if __name__ == "__main__":
    main()
