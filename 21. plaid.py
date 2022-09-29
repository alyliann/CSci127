#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 5, 2021
#This program draws a plaid grid

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter the size: "))
outputfile = input("Enter output file: ")

img = np.ones((num,num,3))

img[1::2,:] = [240/256, 230/256, 0.5490196347236633]
img[:,1::2] = [0.729411780834198, 143/256, 143/256]

#plt.imshow(img)
#plt.show()

plt.imsave(outputfile, img)
