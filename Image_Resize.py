import cv2
import numpy as np

def main():
    raw_image = raw_image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
    cv2.imshow('Raw',raw_image)
    rows, columns = raw_image.shape[:2]
    #image.shape will output (y,x,matrix_layer) => [:2] only output (y,x)
    print("Image Detail (y,x):",rows,",",columns)

    resize_image = cv2.resize(raw_image,(2*rows,2*columns), interpolation = cv2.INTER_CUBIC)
    print("New Image Detai (y,x):",2*rows,",",2*columns)
    cv2.imshow('Resize',resize_image)
    cv2.waitKey(0)
 
if __name__ == '__main__':
    main()
    
