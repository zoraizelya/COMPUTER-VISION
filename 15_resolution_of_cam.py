import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#HD resolution
def hd_reso():
    cap.set(3,1280) # Width
    cap.set(4,720) # Height
hd_reso()

while (True):
    ret,frame = cap.read()
    if ret ==True:
        cv.imshow("Camera",frame)
        # To quit by pressing [q]
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()