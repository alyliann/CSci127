#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 9, 2021
#This program takes user RGB input to create a color

import matplotlib.pyplot as plt
import numpy as np

print("------------------------------------------\n\
Welcome to the Color Maker!\n\
------------------------------------------\n\
Please enter for each rbg color the value in which to increase/decrease them.\n\
If all 3 values given are 0, the program will end and save the resulting image.")

outF = input("Enter outfile name: ") #yourColor.png
img = np.zeros((10,10,3))

R = 0
G = 0
B = 0
condition = True

while condition:
    inR = float(input("How much do you want to change the red value by? "))
    inG = float(input("How much do you want to change the green value by? "))
    inB = float(input("How much do you want to change the blue value by? "))
    if inR == 0 and inG == 0 and inB == 0:
        print("You're done! Congrats on the color, it looks beautiful!")
        plt.imsave(outF, img)
        condition = False
    else:
        R += (inR/255)
        G += (inG/255)
        B += (inB/255)
        if R > 1:
            R = 1
        if G > 1:
            G = 1
        if B > 1:
            B = 1
        if R < 0:
            R = 0
        if G < 0:
            G = 0
        if B < 0:
            B = 0
        img[:,:,0] = R
        img[:,:,1] = G
        img[:,:,2] = B
        print("The current rgb values are: [", R, ",", G, ",", B, "]")
