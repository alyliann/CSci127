#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 28, 2021
#This program draws a colorful spiral

import turtle
tom = turtle.Turtle()

stampInput = input("Enter number of stamps the turtle will print: ")
numStamps = int(stampInput)

turtle.colormode(255)
tom.shape('circle')

steps = 10
red = 186
green = 164
blue = 145

tom.color(red, green, blue)
tom.penup()

for i in range (numStamps):
    tom.stamp()
    if (red+3,green+3,blue+3) < (255,255,255):
        red += 3
        blue += 3
        green += 3
    tom.color(red, green, blue)
    steps = steps + 2
    tom.forward(steps)
    tom.right(24)
