import cv2



def main():
    raw_image = cv2.imread("D:\Python3\Face_Detection\data_human.png")
    cv2.imshow("Test",raw_image)
    gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)

    #Load classifier
    faceCascade = cv2.CascadeClassifier("D:\Python3\Face_Detection\haarcascade_frontalface_default.xml")
    #gray_image -> gray scale pictures
    #scaleFactor (default = 1.1) -> Parameters specifying how much the image size is reduced at each image scale
    #minNeighbors (default = 3) -> how many neighbors each candidate rectangle should have to retain it. (default: at least check 3 times)
    #minSize -> Minimium possible object size
    human = faceCascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    print ("Found {0} faces!".format(len(human)))

    for(x,y,w,h) in human:
        cv2.rectangle(raw_image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Detection",raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
    
