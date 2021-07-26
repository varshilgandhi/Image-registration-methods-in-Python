# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:41:51 2021

@author: abc
"""

"""

Image registration methods in Python

Would you like to install package : pip install image_registration

"""

from skimage import io
from image_registration import chi2_shift

#Read our images
image = io.imread("BSE.jpg")
offset_image = io.imread("BSE_transl.jpg")

#Offset image translated by (-17, 45, 18, 75) in y and x

#Method : 1  - chi squared shift
#find the offsets between image 1 and image 2 using the DFT upsampling 
#Apply chi2_shift method image registration
noise = 0.1
xoff, yoff, exoff, eyoff = chi2_shift(image, offset_image, noise, 
                                      return_error = True, upsample_factor='auto')

#Let's print pixel value of both image
print("Offset image was translated by : 18.75, -17.45")
print("Pixels shifted by: ", xoff, yoff)

#Define our corrected image
from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(xoff, yoff), mode='constant')

#Let's plot our images
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image,cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap='gray')
ax3.title.set_text('Corrected')
plt.show()



######################################################################

#Method 2 : Image Registration using cross correlation shift

from skimage import io
from image_registration import cross_correlation_shifts

#Read our images
image = io.imread("BSE.jpg")
offset_image = io.imread("BSE_transl.jpg")

#offset image translated by (-17.45, 18.75) in y and x

#Apply Cross Correlation shift method for image registration
xoff, yoff = cross_correlation_shifts(image, offset_image)

#Let's print pixel value of both image
print("Offset image was translated by : 18.75 , -17.45")
print("Pixels shifted by : ", xoff, yoff)

#Define our corrected image
from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(xoff, yoff), mode='constant')

#Let's plot all the images
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap='gray')
ax3.title.set_text('Corrected')
plt.show()



#############################################################################

#Method : 3 - Image Registration using Optical flow based shift 

from skimage import io
from image_registration import cross_correlation_shifts

#Read our images
image = io.imread("BSE.jpg")
offset_image = io.imread("BSE_transl.jpg")  
#Offset image translated by (-17.45, 18.75) in y and x

#Apply Optical flow based shift method which is used for image registration 
from skimage import registration
flow = registration.optical_flow_tvl1(image, offset_image)

#Display dense optical flow
flow_x = flow[1, :, :]
flow_y = flow[0, :, :]

#Let us find the mean of all pixels in x and y and shift image by that amount
#ideally, we need to move each pixel by the amount from flow
#Find mean of all pixel in x and y
import numpy as np
xoff = np.mean(flow_x)
yoff = np.mean(flow_y)

#print the pixels of offset and shifted image
print("Offset image translated by : 18.75, -17.45")
print("Pixels shifted by :", xoff, yoff)

#Define our corrected image
from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(xoff, yoff), mode='constant')

#Let's plot all the images 
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap='gray')
ax3.title.set_text('Corrected')
plt.show()

















 











