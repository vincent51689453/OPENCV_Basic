import cv2
import numpy as np

number = 1

def main():
    raw_image = cv2.imread("D:\Python3\Image_Process\data_hough_demo.jpg")
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
    smoothed = cv2.GaussianBlur(gray_image,(5,5),0)
    edges = cv2.Canny(smoothed,50,150,3)
    try:
        lines_p = cv2.HoughLinesP(edges,1,np.pi/180,50,None,100,5)[number]
        print ("line[",number,"]:",lines_p)
        for p1 in lines_p:
            cv2.line(raw_image, (p1[0], p1[1]), (p1[2], p1[3]), (255, 0, 0), 3)         
        cv2.imshow("HoughLinesP",raw_image)
        cv2.waitKey(0)
    except TypeError:
        print("The HoughlinesP function returns None, try decrease the threshold!")
    cv2.destroyAllWindows()

    

if __name__ =='__main__':
    main()
