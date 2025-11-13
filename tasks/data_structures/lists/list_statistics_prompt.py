"""Collect integers from the user and display basic statistics."""


def collect_numbers() -> list[int]:
    numbers: list[int] = []
    while True:
        raw_value = input("Skriv inn et heltall (avslutt med q): ")
        if raw_value == "q":
            break
        if raw_value.isnumeric():
            numbers.append(int(raw_value))
        else:
            print("ERROR! Du må enten skrive et heltall eller avslutte med q.")
    return numbers


def show_statistics(numbers: list[int]) -> None:
    if not numbers:
        print("Ingen tall ble lagt til")
        return

    total = sum(numbers)
    largest = max(numbers)
    smallest = min(numbers)

    print()
    print(f"Listen: {numbers}")
    print(f"Summen av alle elementene til sammen: {total}")
    print(f"Det største elementet til listen: {largest}")
    print(f"Det minste elementet til listen: {smallest}")
    print(f"Det er totalt {len(numbers)} elementer i lista")


def main() -> None:
    numbers = collect_numbers()
    show_statistics(numbers)


if __name__ == "__main__":
    main()
