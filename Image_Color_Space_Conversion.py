import cv2
import numpy as np

image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
cv2.imshow("Original", image)  #will be in BGR format

# Convert BGR -> Gray
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray_image)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
