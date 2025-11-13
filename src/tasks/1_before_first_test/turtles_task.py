import turtle as t
t.speed(200)

screen = t.Screen()
screen.title("Turtle")

antall_sider = 20
sidelengde = 20
fargekode = "yellow"

def tegn_mangekant(antall_sider, sidelengde, fargekode):
    
    t.fillcolor(fargekode)
    
    for i in range(0, antall_sider + 1):
        t.forward(sidelengde)
        t.left(360/antall_sider)

    
        
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

for i in range(0, 10):
    t.right(10)
    t.forward(10)

t.pendown()
t.done()