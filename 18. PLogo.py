#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 28, 2021
#This program draws a pink P on a 30x30 grid

import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((30,30,3))

img[0:6,:,(0,2)] = 1
img[:,0:6,(0,2)] = 1
img[15:21,:,(0,2)] = 1
img[:21,25:,(0,2)] = 1

plt.imsave('logo.png',img)
