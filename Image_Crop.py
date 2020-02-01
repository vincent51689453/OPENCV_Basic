import cv2
import numpy as np

image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
cv2.imshow("Original", image)


#image[row, column]
face = image[95:195, 100:180]
cv2.imshow("Face",face)



body = image[20:, 35:210]
cv2.imshow("Body", body)
cv2.waitKey(0)

cv2.destroyAllWindows()
