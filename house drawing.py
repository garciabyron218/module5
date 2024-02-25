# Byron Garcia
# 2/25/24
# program that uses a turtle to draw a house

import turtle

screen = turtle.Screen()

toto = turtle.Turtle()
toto.fillcolor("yellow")
toto.begin_fill()
for _ in range(4):
    toto.forward(100)
    toto.left(90)
toto.end_fill()

toto.penup()
toto.goto(-50, 100)
toto.pendown()

toto.setheading(0)
toto.fillcolor("grey")
toto.begin_fill()
toto.forward(200)
toto.left(135)
toto.forward(140)
toto.left(90)
toto.forward(140)
toto.end_fill()


screen.mainloop()
