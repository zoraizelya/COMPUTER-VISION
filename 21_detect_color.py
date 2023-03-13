import cv2 as cv
from cv2 import imshow
import numpy as np

# img = cv.imread("resources/kust.jpg")

# Convert into HSV i.e Hue , Saturatiuon , Value
# hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Sliders
def slider():
    pass
path = "resources/kust.jpg"
cv.namedWindow("Bars")
cv.resizeWindow("Bars",840,500)
cv.createTrackbar("Hue min","Bars",0,179,slider)
cv.createTrackbar("Hue max","Bars",179,179,slider)
cv.createTrackbar("Sat min","Bars",0,255,slider)
cv.createTrackbar("Sat max","Bars",255,255,slider)
cv.createTrackbar("Val min","Bars",0,255,slider)
cv.createTrackbar("Val max","Bars",255,255,slider)

img =cv.imread(path)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos("Hue min","Bars")
# print(hue_min)

while (True):
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue min","Bars")
    hue_max = cv.getTrackbarPos("Hue max","Bars")
    sat_min = cv.getTrackbarPos("Sat min","Bars")
    sat_max = cv.getTrackbarPos("Sat max","Bars")
    val_min = cv.getTrackbarPos("Val min","Bars")
    val_max = cv.getTrackbarPos("Val max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    # To See Changes in Image
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])

    mask_image = cv.inRange(hsv_img,lower,upper)
    ouput_image = cv.bitwise_and(img,img,mask=mask_image)

    # cv.imshow("Original",img)
    # cv.imshow("HSV",hsv_img)
    cv.imshow("Mask",mask_image)
    cv.imshow("Final Output ",ouput_image)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break
cv.destroyAllWindows()