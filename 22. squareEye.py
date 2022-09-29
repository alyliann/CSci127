#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 5, 2021
#This program draws an eye of squares

import turtle
tom = turtle.Turtle()

turtle.colormode(255)
tom.speed(0)
tom.pensize(5)
turtle.bgcolor('khaki')

for i in range(36):
    tom.pencolor(0,i*7,0)
    tom.forward(10)
    tom.left(10)
    for i in range(4):
        tom.left(90)
        tom.forward(300)
        tom.backward(50)
