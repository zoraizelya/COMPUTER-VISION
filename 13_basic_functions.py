
import cv2 as cv
import numpy as np
# ORIGINAL 
img = cv.imread("resources/kust.jpg")

# Fun 1: Resize Image
resized_img = cv.resize(img , (350,250))

# Fun 2: Gray Image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Fun 3: Blured Image
blur = cv.GaussianBlur(img,(7,7),0)

# Fun 4: Edge detection
edge = cv.Canny(img,53,53)

# Fun 5: thikness of lines
mat_kernal = np.ones((3,3),np.uint8)
dilated = cv.dilate(edge,mat_kernal,iterations=1)

# Fun 6: thiner of lines
erode = cv.erode(dilated,mat_kernal,iterations=1)

# Fun 7: BLACK AND WHITE    


# Fun 8: Crop image.  We will use numpy not openCV
crop = resized_img[0:300,0:250]


cv.imshow("Original",img)
cv.imshow("Resized Image",resized_img)
cv.imshow("Gray Image",gray)
cv.imshow("Blur Image",blur)
cv.imshow("Edge Image",edge)
cv.imshow("Dilated Image",dilated)
cv.imshow("Erode Image",erode)
cv.imshow("Crop Image",crop)
cv.waitKey(0)
cv.destroyAllWindows()
