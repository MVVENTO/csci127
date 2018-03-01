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
img = np.zeros((2,2,3))


# top left
#red
img[0,0,0] = 255
#green
img[0,0,1] = 0
#blue
img[0,0,2] = 0


# top right
#red
img[0,1,0] = 0
#green
img[0,1,1] = 255
#blue
img[0,1,2] = 0


# bottom left
#red
img[1,0,0] = 127
#green
img[1,0,1] = 127
#blue
img[1,0,2] = 127


# bottom right
#red
img[1,1,0] = 0
#green
img[1,1,1] = 0
#blue
img[1,1,2] = 255



print (img.shape)
print(img)
img /= 255.
plt.imshow(img,interpolation = 'nearest')		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

plt.imsave('my_artifical_img.png', img)  #Save the image we created to the file: reds.png
