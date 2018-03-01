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
img = np.zeros((10,20,3))

colors =[[228,26,28],
[55,126,184],
[77,175,74],
[152,78,163],
[255,127,0]]

# top left
#red
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j] = colors[i%5]



print (img.shape)
print(img)
img /= 255.
plt.imshow(img,interpolation = 'nearest')		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

plt.imsave('my_artifical_img.png', img)  #Save the image we created to the file: reds.png
