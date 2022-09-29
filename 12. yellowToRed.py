#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 21, 2021
#This program prints tear drops in shades of yellow-to-red

import turtle
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

turtle.colormode(255)

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(255,255 - i,0)

tess.penup()
for i in range(250,-5,-10):
    tess.backward(10)
    tess.pensize(i)

tess.color(0,0,0)
tess.right(90)
tess.pendown()

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(255,255 - i,0)
