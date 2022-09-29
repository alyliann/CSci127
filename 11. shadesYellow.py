#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 21, 2021
#This program prints a heart in shades of yellow

import turtle
tess = turtle.Turtle()
tess.shape("turtle")

turtle.colormode(255)
tess.left(60)

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(i,i,0)

tess.penup()
for i in range(250,-5,-10):
    tess.backward(10)
    tess.pensize(i)

tess.color(0,0,0)
tess.left(60)
tess.pendown()

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(i,i,0)
