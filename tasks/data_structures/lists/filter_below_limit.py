"""Filter numbers that fall below a configurable threshold."""

from collections.abc import Iterable


def filter_below_limit(values: Iterable[int], *, limit: int = 10) -> list[int]:
    """Return the numbers from *values* that are less than *limit*."""
    filtered_values: list[int] = []
    for element in values:
        if element < limit:
            filtered_values.append(element)
    return filtered_values


def main() -> None:
    numbers = [4, 12, 8, 23, 3, 5, 11, 9]
    new_numbers = filter_below_limit(numbers)

    print()
    print(f"Original list: {numbers}")
    print(f"Filtered list: {new_numbers}")


if __name__ == "__main__":
    main()
