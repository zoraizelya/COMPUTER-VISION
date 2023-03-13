import cv2 as cv
cap = cv.VideoCapture('resources/vid.mp4')

while(True):
    (ret,frame) = cap.read()
    # For Gray 
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # For Black and white
    (thresh,b_w) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    # To Show the video
    if ret ==True:
        cv.imshow("Video",grayframe)
        cv.imshow("Video",b_w)
        # To quit by pressing [q]
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
cap.release()
cv.destroyAllWindows()