import cv2
import numpy as np

Hue_Max = 179
Sat_Max = 255
Bri_Max = 255
default_H,default_S,default_V = 160,200,200
Window_Name = "HSV Tunning Software"



def dummy(x):
    pass


def tunning_pheripherals():
    cv2.namedWindow(Window_Name)
    cv2.resizeWindow(Window_Name,400,300)
    cv2.createTrackbar('H_Min',Window_Name,0,Hue_Max,dummy)
    cv2.createTrackbar('H_Max',Window_Name,0,Hue_Max,dummy)
    cv2.createTrackbar('S_Min',Window_Name,0,Sat_Max,dummy)
    cv2.createTrackbar('S_Max',Window_Name,0,Sat_Max,dummy)   
    cv2.createTrackbar('V_Min',Window_Name,0,Bri_Max,dummy)
    cv2.createTrackbar('V_Max',Window_Name,0,Bri_Max,dummy)
    cv2.setTrackbarPos('H_Min',Window_Name,0)
    cv2.setTrackbarPos('H_Max',Window_Name,default_H)
    cv2.setTrackbarPos('S_Min',Window_Name,0)
    cv2.setTrackbarPos('S_Max',Window_Name,default_S)
    cv2.setTrackbarPos('V_Min',Window_Name,0)
    cv2.setTrackbarPos('V_Max',Window_Name,default_V)
    
    
def main():
    #Raw Image Input
    raw_image = cv2.imread("D:\Python3\Color_Space\lena256rgb.jpg")
    hsv_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV:',hsv_image)
    tunning_pheripherals()
    while True:
        h_lower_limit = cv2.getTrackbarPos('H_Min',Window_Name)
        h_upper_limit = cv2.getTrackbarPos('H_Max',Window_Name)
        s_lower_limit = cv2.getTrackbarPos('S_Min',Window_Name)
        s_upper_limit = cv2.getTrackbarPos('S_Max',Window_Name)
        v_lower_limit = cv2.getTrackbarPos('V_Min',Window_Name)
        v_upper_limit = cv2.getTrackbarPos('V_Max',Window_Name)
        
        if((h_lower_limit <= h_upper_limit)and(s_lower_limit <= s_upper_limit)and(v_lower_limit <= v_upper_limit)):
            lower_matrix = np.array([h_lower_limit,s_lower_limit,v_lower_limit])
            upper_matrix = np.array([h_upper_limit,s_upper_limit,v_upper_limit])
            mask_image = cv2.inRange(hsv_image,lower_matrix,upper_matrix)
            cv2.imshow('Mask',mask_image)

            result = cv2.bitwise_and(raw_image,raw_image,mask=mask_image)
            cv2.imshow('Final Result',result)
        else:
            print('Parameter Error!')

        cv2.waitKey(1)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
        
    
