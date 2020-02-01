import cv2
import numpy as np

def main():
    raw_image = cv2.imread("D:\Python3\Image_Process\moment.jpg")
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
    res,thres_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

    temp_image,contours,hierarchy = cv2.findContours(thres_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    #chose which contour to draw
    #different number will lead to draw different contour and calculate relative circle
    cnt=contours[3]

    
    #Finding a minimum circle that can surrond the object
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    #A matrix M (dictionary) is returned for calculating the centroid
    M = cv2.moments(cnt)
    #Center calculation
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    #cv2.circle(image,center coordinates, radius, color, thickness)
    cv2.circle(raw_image,(int(x),int(y)),int(radius),(0,255,255),2)  #Draw Minimum enclosing circle
    cv2.circle(raw_image,center,5,(0,0,255),-1)
    cv2.imshow("Enclosing",raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

if __name__ == '__main__':
    main()
