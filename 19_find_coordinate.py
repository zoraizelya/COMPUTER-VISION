import cv2 as cv
import numpy as np


# Define a function
def find_cord(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        # Left mouse click
        print(x,'',y)
        font= cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x)+ ','+str(y),(x,y),font,1,(255,0,0),thickness=2)
        #Show text on image
        cv.imshow("image",img)
    # For color finding
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        font = cv.FONT_HERSHEY_PLAIN
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img,str(b)+','+str(g)+','+str(r),(x,y),font,1,(255,0,2),thickness=2)
        cv.imshow("image",img)


# Final funcytion to read and display
if __name__=="__main__":
    # Reading an image
    img = cv.imread("resources/kust.jpg",1)
    cv.imshow("image",img)
    cv.setMouseCallback("image",find_cord)
    cv.waitKey(0)
    cv.destroyAllWindows()

