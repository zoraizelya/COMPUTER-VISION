import cv2 as cv
cap = cv.VideoCapture('resources/vid.mp4')
# Writing format , codec , video editor and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/Out_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)
while(True):
    (ret,frame) = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    if ret ==True:
        out.write(grayframe)
        cv.imshow("Video",grayframe)
        # To quit by pressing [q]
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
cap.release()
out.release()
cv.destroyAllWindows()