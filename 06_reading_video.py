import cv2 as cv

cap = cv.VideoCapture('resources/vid.mp4')
# this [if] condition is telling if we are having using the right path or not and will show us details
if (cap.isOpened() == False):
    print("Error in video")

# Reading and playing
while(cap.isOpened):
    ret,frame = cap.read()
    if ret ==True:
        cv.imshow("Video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):   # By pressing q it will exit video
            break
    else :
        break
cap.release()
cv.destroyAllWindows()