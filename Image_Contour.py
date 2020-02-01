import cv2


def main():
    raw_image = cv2.imread("D:\Python3\Image Process\lena512rgb.png")
    cv2.imshow('Raw',raw_image)
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
    # res -> classifying threshold
    # thres_image -> resultant image
    # 127 = threshold value
    # 255 = indicating color
    # cv2.THRESH_BINARY -> one of the thresholding effect
    res,thres_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
    cv2.imshow("Threshold",thres_image)
    # find contours
    # @mode: CV_RETR_EXTERNAL / CV_RETR_LIST / CV_RETR_CCOMP / CV_RETR_TREE
    # @method: CV_CHAIN_APPROX_NONE / CV_CHAIN_APPROX_SIMPLE
    # hierarchy = can be used to draw independent contour, -1 to draw all contour
    # contours = contours of pictures
    # image = raw image
    image,contours,hierarchy = cv2.findContours(thres_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # -1 -> Which contour to draw. If -1, then draw all contours
    # (0,255,0) color
    # 3 thickness
    cv2.drawContours(raw_image, contours,-1,(0,255,0),3)
    cv2.imshow("Contours",raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    



if __name__ == '__main__':
    main()
