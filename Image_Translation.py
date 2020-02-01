import cv2
import numpy as np

def main():
    raw_image = raw_image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
    cv2.imshow('Raw',raw_image)
    rows, columns = raw_image.shape[:2]
    #image.shape will output (y,x,matrix_layer) => [:2] only output (y,x)
    print("Image Detail (y,x):",rows,",",columns)

    #Translation Matrix M -> Used for adjusting translation
    M = np.float32([ [1,0,130], [0,1,50] ])
    translation = cv2.warpAffine(raw_image, M, (columns, rows))
    cv2.imshow('Translation', translation)
    cv2.waitKey(0)
 
if __name__ == '__main__':
    main()
    
