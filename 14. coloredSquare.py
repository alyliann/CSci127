#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 22, 2021
#This program draws a colorful square

colore = input("Please enter a 6-digit Hexadecimal number: ")

import turtle
tim = turtle.Turtle()
tim.color('#'+colore)
tim.shape('turtle')

for i in range(4):
    tim.left(90)
    tim.forward(100)
    tim.stamp()
