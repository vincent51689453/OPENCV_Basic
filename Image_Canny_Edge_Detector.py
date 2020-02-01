import cv2
import numpy as np

window_name = 'Canny_Edge_Dectector'

def dummy(x):
    pass

def Tunning_pheripherals():
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Threshold',window_name,0,100,dummy)
    cv2.createTrackbar('Ratio',window_name,0,5,dummy)
    cv2.setTrackbarPos('Threshold',window_name,1)
    cv2.setTrackbarPos('Ratio',window_name,1)

def main():
    raw_image = cv2.imread("D:\Python3\Image Process\lena512rgb.png")
    cv2.imshow('Raw',raw_image)
    Tunning_pheripherals()
    while True:
        threshold = cv2.getTrackbarPos('Threshold',window_name)
        ratio = cv2.getTrackbarPos('Ratio',window_name)

        gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
        #GassianBlur is used to smooth image where the kernel size is 5x5
        smoothed = cv2.GaussianBlur(gray_image,(5,5),0)
        edges = cv2.Canny(smoothed,threshold,threshold*ratio)
        print("Canny Threshold:",threshold,"and",threshold*ratio)
        cv2.imshow("Edge Detection",edges)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
        
        
