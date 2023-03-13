import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
# Writing format , codec , video editor and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# 50 is the speed of your video you can adjust it 
out = cv.VideoWriter("resources/cam_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),50,(frame_width,frame_height))
while(True):
    (ret,frame) = cap.read()
    if ret ==True:
        out.write(frame)
        cv.imshow("Video",frame)
        # To quit by pressing [q]
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
cap.release()
out.release()
cv.destroyAllWindows()