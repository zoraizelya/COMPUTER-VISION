import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10,100)# !0 brightness key
cap.set(3,640)
cap.set(4,480)
while (True):
    (ret,frame) = cap.read()
    if ret == True:
        cv.imshow("Frame Video",frame)
        # To quit by pressing [q]
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()