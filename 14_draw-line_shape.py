import cv2 as cv
import numpy as np

# Draw a canvas
img = np.zeros((600,600))

# Adding Colors channels
colored_img = np.zeros((600,600,3),np.uint8)
# Coloring complete image
colored_img[:]= 255,0,255
# Coloring part of image
colored_img[150:230,100:207]= 255,0,0
# adding lines
# complete line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)
# part of a line
cv.line(colored_img,(100,100),(300,300),(255,255,50),3) 
# Adding  rectangle
cv.rectangle(colored_img,(50,100),(300,350),(255,238,78),3)
# Filling Rectanle
cv.rectangle(colored_img,(50,100),(300,350),(255,238,78),cv.FILLED)
# Adding Circle
cv.circle(colored_img,(400,300),50,(255,238,78),3)
cv.circle(colored_img,(400,300),50,(255,238,78),cv.FILLED)
# Adding Text
cv.putText(colored_img,"Python ka chilla",(200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),2)

cv.imshow("Black",img)
cv.imshow("Colored Image",colored_img)
cv.waitKey()
cv.destroyAllWindows()