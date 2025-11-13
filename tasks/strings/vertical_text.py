"""Display the word "Vertical" one character per line using two approaches."""

WORD = "Vertical"


def print_line_by_line(word: str) -> None:
    for letter in word:
        print(letter)


def main() -> None:
    print_line_by_line(WORD)
    print("-------------")
    print("V\ne\nr\nt\ni\nk\na\nl\n")


if __name__ == "__main__":
    main()
