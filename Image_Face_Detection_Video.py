import cv2

video_path = "D:\Python3\Face_Detection\data_human_video.avi"


def main():
    camera = cv2.VideoCapture(video_path)             # 0 = first camera
    #camera.set(cv2.CAP_PROP_FRAME_WIDTH,960) # set frame dimensions
    #camera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    faceCascade = cv2.CascadeClassifier("D:\Python3\Face_Detection\haarcascade_frontalface_default.xml")
    while (camera.isOpened()):
        #Capture frame by frame
        ret,frame = camera.read() 
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        human = faceCascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=8,minSize=(40,40))
        print("{0} faces deteced!".format(len(human)))
        for(x,y,w,h)in human:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, "Human", (x+w+10, y+h+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255))
        cv2.imshow("Detector",frame)
        cv2.waitKey(25)
    camera.release() #When everything is done, release the capture
    cv2.destroyAllWindows()
        
        
if __name__ == '__main__':
    main()
