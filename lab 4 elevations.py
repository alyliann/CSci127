#This program takes elevation data of NYC and displays using the default color map

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)          #takes map shape and adds
                                            #   3rd dimension for colors
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):              # [0] means the first dimension?
    for col in range(mapShape[1]):          # [1] means the second?
        if elevations[row,col] <= 0:        #below sea level
           floodMap[row,col,2] = 1.0
        elif elevations[row,col] <= 6:      #flooding likely 6 ft and below
            floodMap[row,col,0] = 1.0
        else:                               #flooding not likely here
            floodMap[row,col,1] = 1.0

plt.imshow(floodMap)
plt.show()
