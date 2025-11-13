"""Calculate the area of a triangle and repeat the sum multiple times."""


def triangle_area(base: int, height: int) -> int:
    return base * height


def main() -> None:
    base_input = input("Skriv et tall for grunnlinjen: ")
    height_input = input("Skriv et tall for høyden: ")

    if base_input.isnumeric() and height_input.isnumeric():
        base = int(base_input)
        height = int(height_input)
        area = triangle_area(base, height)

        repetitions = int(input("Hvor mange ganger skal summen gjentas? "))
        total = 0
        for _ in range(repetitions):
            total += area

        print(total)
    else:
        print("Du skrev ikke inn riktige tall")


if __name__ == "__main__":
    main()
