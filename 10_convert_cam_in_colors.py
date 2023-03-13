import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while (True):
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,b_w) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    cv.imshow("Original Cam",frame)
    cv.imshow("Gray Cam",gray)
    cv.imshow("Black And White Cam",b_w)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()