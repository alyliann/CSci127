#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#D
ate: September 22, 2021
#This program makes a photo yellow

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


og_pic = input("Enter name of the input file: ")
end_pic = input("Enter name of the output file: ")

img = plt.imread(og_pic)            #Read in image from og_pic
img2 = img.copy()                   #make a copy of our image
img2[:,:,2] = 0                     #Set the red channel to 0

plt.imsave(end_pic, img2)        #Save the image we created to the file: reds.png

#not needed:
plt.imshow(img)             #Load image into pyplot
plt.show()                  #Show the image (waits until closed to continue)
