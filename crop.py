# image crop 
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder.jpg")
img = cv2.resize(img, (120, 360), interpolation=cv2.INTER_AREA) #resize (x, y)

crop_img = img[252:360, 0:120] #[y:y+h, x:x+w]

cv2.imshow("cropped", crop_img)
cv2.imshow("reg", img)

cv2.waitKey(0)
cv2.imwrite('/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder/1-10-252-360.jpg', crop_img)


# print(img.size)