#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 5, 2021
#This program counts snow

import matplotlib.pyplot as plt
import numpy as np

in1 = input("Enter first image file name: ")
in2 = input("Enter second image file: ")
t = float(input("Enter threshold of white pixels: "))

img1 = plt.imread(in1)
img2 = plt.imread(in2)
countSnow1 = 0
countSnow2 = 0

for row in range(img1.shape[0]):
    for col in range(img1.shape[1]):
        if (img1[row,col,0]>t) and (img1[row,col,1]>t) and (img1[row,col,2]>t):
            countSnow1 = countSnow1 + 1
 
print("Snow count of first image: ", countSnow1)

for row in range(img2.shape[0]):
    for col in range(img2.shape[1]):
        if (img2[row,col,0]>t) and (img2[row,col,1]>t) and (img2[row,col,2]>t):
            countSnow2 = countSnow2 + 1

print("Snow count of second image: ", countSnow2)

print("Difference between first and second image: ", countSnow1 - countSnow2)
