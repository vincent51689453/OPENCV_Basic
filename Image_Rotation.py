import cv2
import numpy as np

def main():
    raw_image = raw_image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
    cv2.imshow('Raw',raw_image)
    rows, columns = raw_image.shape[:2]
    #image.shape will output (y,x,matrix_layer) => [:2] only output (y,x)
    print("Image Detail (y,x):",rows,",",columns)
    
    #cv2.getRotationMatrix2D( rotation center y, rotation center x, rotational angle [counterclockwise], resize ration)
    #Center = row/2 and column/2
    rotated_image = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 1)
    #cv2.warpAffine(original image, transformed image, dimensions of new picture)
    result = cv2.warpAffine(raw_image,rotated_image,(columns,rows))
    cv2.imshow('Rotation',result)
    cv2.waitKey(0)

 
if __name__ == '__main__':
    main()
    
