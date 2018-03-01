#me:  CSci 127 Teaching Staff
#Date:  Fall 2017
#This program is used to generate an artifical img

#Import the packages for images and arrays:
import matplotlib.pyplot as plt  
import numpy as np

"""
file_name = "csBridge.png"
file_name = "hunter.jpg"
img = plt.imread(file_name)   #Read in image from csBridge.png
"""
img = np.random.rand(1000,2000,3)

print (img.shape)
print(img[0])
plt.imshow(img,interpolation = 'nearest')		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

plt.imsave('random_img.png', img)  #Save the image we created to the file: reds.png
