import cv2 as cv


cap =cv.VideoCapture("resources/vid.mp4")

frameNr = 0

while(True):
    success,frame = cap.read()
    if success:
        # here [f] is used to take frames and put it in the string
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg",frame)
    else:
        break
    frameNr = frameNr + 1
cap.release()

