import cv2
import numpy as np

def main():
    raw_image = cv2.imread("D:\Python3\Image_Process\data_hough_demo.jpg")
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
    h,w = gray_image.shape

    smoothed = cv2.GaussianBlur(gray_image,(5,5),0)
    #find out all edges first
    edges = cv2.Canny(smoothed,50,150)
    cv2.imshow("Edges",edges)
    try:
       #cv2.HoughLines(canny_edges_image, resolution, angle(accuracy resolution), threshold (for a straightline))
        detected_lines = cv2.HoughLines(edges,1,np.pi/180,250)[1]
        for (rho, theta) in detected_lines:
            x0 = np.cos(theta)*rho 
            y0 = np.sin(theta)*rho
            pt1 = ( int(x0 + (h+w)*(-np.sin(theta))), int(y0 + (h+w)*np.cos(theta)) )
            pt2 = ( int(x0 - (h+w)*(-np.sin(theta))), int(y0 - (h+w)*np.cos(theta)) )
            cv2.line(raw_image, pt1, pt2, (0, 0, 255), 3) 
            cv2.imshow("HoughLines", raw_image)
            cv2.waitKey(0)
    except TypeError:
        print ("The Houghlines function returns None, try decrease the threshold!")
    cv2.destroyAllWindows()
    
    
if __name__ =='__main__':
    main()
