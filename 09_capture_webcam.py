# Step 1 : Import libraries
import cv2 as cv
import numpy as np
# Step 2 : Read frame from camera
cap = cv.VideoCapture(0)  # 0 mean webcam no. 1
# For showing Error
if (cap.isOpened()==False):
    print("There is Some Error")
# Read cam until the end
# Step 3 : Display camera frame by frame (cap.isOpened)
while(cap.isOpened()):
    # Capture frame by frame
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
# Release or Close Windows Easily
cap.release()
cv.destroyAllWindows()