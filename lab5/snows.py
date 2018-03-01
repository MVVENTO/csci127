#Name:  CSci 127 Teaching Staff
#Date:  Fall 2017
#This program loads an image, counts the number of pixels that are
#    nearly white as an estimate for snow pack.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt  
import numpy as np


ca = plt.imread('CaliforniaDrought_02232011_md.png')   #Read in image

print (ca.shape
)
plt.imshow(ca)
plt.show()
plt.close()
countSnow = 0            #Number of pixels that are almost white
t = 0.87                 #Threshold for almost white-- can adjust between 0.0 and 1.0
pure_snow_img = np.zeros(ca.shape)
#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               pure_snow_img[i,j,:] = ca[i,j,:]
               countSnow = countSnow + 1
plt.imshow(pure_snow_img)
plt.show()
print("Snow count is", countSnow)
