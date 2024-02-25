# Byron Garcia
# 2/25/24
# Turtle will draw shape based on input of sides, color, and size.

import turtle

toto = turtle.Turtle()

poly_sides = int(input('Enter how many sides for polygon: '))
poly_length = int(input('How long is each side? '))
poly_line = input('What color line? ')
poly_color = input("what color is the polygon? ")

toto.pencolor(poly_line)
toto.fillcolor(poly_color)

toto.begin_fill()

for _ in range(poly_sides):
    toto.forward(poly_length)
    toto.left(360 / poly_sides)

toto.end_fill()

turtle.done()




