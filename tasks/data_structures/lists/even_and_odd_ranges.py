"""Generate and display even and odd numbers within a given range."""

def build_even_numbers(start: int = 2, stop: int = 100) -> list[int]:
    """Return a list of even numbers from ``start`` to ``stop`` inclusive."""
    return list(range(start, stop + 1, 2))


def build_odd_numbers(start: int = 1, stop: int = 100) -> list[int]:
    """Return a list of odd numbers from ``start`` to ``stop`` inclusive."""
    return list(range(start, stop + 1, 2))


def main() -> None:
    """Print the generated ranges to the terminal."""
    even_numbers = build_even_numbers()
    odd_numbers = build_odd_numbers()

    print()
    print(even_numbers)
    print()
    print(odd_numbers)


if __name__ == "__main__":
    main()
