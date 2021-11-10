# Putting images all together vertically or horizontally with numpy --> vstack & hstack

import numpy
import cv2 
 
img1 = cv2.imread('/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder/1-10-250-360.jpg')
img2 = cv2.imread('/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder/1-1-40-110-rotate.jpg')
 
# comment out either based on the need
verticalAppendedImg = numpy.vstack((img1,img2)) #vertical stack
horizontalAppendedImg = numpy.hstack((img,img,img)) #horizontal stack
 
 
cv2.imshow('Vertical Appended', verticalAppendedImg)
cv2.imshow('Horizontal Appended', horizontalAppendedImg)
 
cv2.waitKey(0)
cv2.imwrite('/Users/Shih-Hsi Chien/Desktop/jupyter/image/combo/14.jpg', verticalAppendedImg)

cv2.destroyAllWindows()