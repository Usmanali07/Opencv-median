import cv2
import numpy as np
image= cv2.imread('now.jpg')
# prcessed_image=cv2.medianBlur(image,7)
kernel= np.ones((3,3), np.float32)/9
prcessed_image=cv2.filter2D(image ,-1 , kernel)
cv2.imshow('Median Filter  Processing',prcessed_image)
cv2.imwrite('prcessed_image.png',prcessed_image)
cv2.waitKey(0)