import cv2
import numpy as np

image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
cv2.imshow("Original", image)

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower = np.array([141, 0, 0])
upper = np.array([164, 145, 197])

# Threshold the HSV image to get only purple colors
binary = cv2.inRange(hsv_image, lower, upper)
cv2.imshow("Binary", binary)
print("HSV Binary image...")
cv2.waitKey(0)

cv2.destroyAllWindows()

