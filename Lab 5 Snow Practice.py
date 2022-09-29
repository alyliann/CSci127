import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread('feb2011.png')
countSnow = 0
t = 0.75

for row in range(ca.shape[0]):
    for col in range(ca.shape[1]):
        if (ca[row,col,0]>t) and (ca[row,col,1]>t) and (ca[row,col,2]>t):
            countSnow = countSnow + 1
 
print("Snow count is", countSnow)
