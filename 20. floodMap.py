#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 28, 2021
#This program modifies the program from lab 4

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,(0,1)] = 1.0
        elif elevations[row,col] <= 5:      
            floodMap[row,col,0] = 1.0
        elif 20>= elevations[row,col] > 5:
            floodMap[row,col,0:3] = 0.5
        else:
            floodMap[row,col,1] = 1.0
        
plt.imsave('floodMap.png', floodMap)
