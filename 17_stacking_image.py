import cv2 as cv
import numpy as np

img = cv.imread("resources/kust.jpg")

horizontal_img = np.hstack((img,img))
vertical_img = np.vstack((img,img))

cv.imshow("Horizontal",horizontal_img)
cv.imshow("Vertical",vertical_img)
cv.waitKey(0)
cv.destroyAllWindows()