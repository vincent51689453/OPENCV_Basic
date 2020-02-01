import cv2
import numpy as np




def main():
    raw_image = cv2.imread("D:\Python3\Image_Process\lena512rgb.png")
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
    res,thres_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
    cv2.imshow("Binary",thres_image)

    #create a 3x3 matrix with all 1
    kernel = np.ones((3,3),np.uint8)

    #Corrosion => Image convolute with kernel and reduce the area
    erode_image = cv2.erode(thres_image,kernel,iterations = 1)
    # Default iterations = 1, number of execution of corrosion
    cv2.imshow("Erode",erode_image)

    #Dilate => Image convolute with kernel and increase the area
    dilate_image = cv2.dilate(thres_image,kernel,iterations = 1)
    cv2.imshow("Dilate",dilate_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


if __name__ == '__main__':
    main()
