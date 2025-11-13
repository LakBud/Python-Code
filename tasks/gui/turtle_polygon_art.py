"""Render a simple turtle art scene made of filled polygons."""

import turtle as t


def tegn_mangekant(antall_sider: int, sidelengde: int, fargekode: str) -> None:
    t.fillcolor(fargekode)
    for _ in range(antall_sider + 1):
        t.forward(sidelengde)
        t.left(360 / antall_sider)


def main() -> None:
    t.speed(200)
    screen = t.Screen()
    screen.title("Turtle")

    antall_sider = 20
    sidelengde = 20
    fargekode = "yellow"

    t.pendown()
    t.begin_fill()
    tegn_mangekant(antall_sider, sidelengde, fargekode)
    t.end_fill()

    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.begin_fill()
    tegn_mangekant(20, 5, "black")
    t.end_fill()

    t.penup()
    t.goto(-20, 50)
    t.pendown()
    t.begin_fill()
    tegn_mangekant(20, 5, "black")
    t.end_fill()

    t.penup()
    t.goto(50, 35)
    t.pendown()
    t.left(-180)

    for _ in range(10):
        t.right(10)
        t.forward(10)

    t.done()


if __name__ == "__main__":
    main()
