#Name:  Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 13, 2021
#This program draws a pinwheel

import turtle
tom = turtle.Turtle()
tom.shape("arrow")
tom.color("purple")
tom.pensize(3)

tom.forward(30)

for i in range(3):
    tom.forward(50)
    tom.right(120)

tom.backward(30)
tom.right(90)
tom.forward(30)

for i in range(3):
    tom.forward(50)
    tom.right(120)

tom.backward(30)
tom.right(90)
tom.forward(30)

for i in range(3):
    tom.forward(50)
    tom.right(120)

tom.backward(30)
tom.right(90)
tom.forward(30)

for i in range(3):
    tom.forward(50)
    tom.right(120)

tom.backward(30)
