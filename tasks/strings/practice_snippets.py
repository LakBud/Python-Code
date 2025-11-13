"""Miscellaneous string formatting and list exercises."""


def display_shopping_message() -> None:
    money = 1.5
    store = "H&M"
    print(f"Jeg liker {store} men jeg har bare {money} kr")


def show_quote_excerpt() -> None:
    quote = "Jeg kjøpte Dogecoin også gikk den ned hard, big F"
    print(quote[44:49])


def display_language() -> None:
    message = "Språket mitt er HTML/PHP/Python"
    print(message)


def multiply_floats() -> None:
    first = 5.4309309309
    second = 4.354905590
    print(f"sum = {(first * second):^.3f}")


def costume_check() -> None:
    costume = input("Har du en kostyme, svar enten ja eller nei: ")
    if costume == "ja":
        print("Du kan komme inn bygget")
    elif costume == "nei":
        print("Du kan ikke komme inn bygget")
    else:
        print("Du må svare enten ja eller nei")


def playlist_demo() -> None:
    songs = ["F.R.I.E.N.D.S", "All Alone", "Bad", "Believer", "Fight Back", "Dior", "TFW"]
    print(songs)
    print(songs[3])
    songs.remove("TFW")
    songs.insert(1, "Pride is the Devil")
    print(songs)


def main() -> None:
    print()
    display_shopping_message()

    print()
    show_quote_excerpt()

    print()
    display_language()

    print()
    multiply_floats()

    print()
    costume_check()

    print()
    playlist_demo()


if __name__ == "__main__":
    main()
