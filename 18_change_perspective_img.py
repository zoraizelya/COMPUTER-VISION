import cv2 as cv
from cv2 import imread
import numpy as np

img = imread("resources/kust.jpg")


# Definig points
point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])
width = 800
height = 900
point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2)

output_img = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("Original",img) 
cv.imshow("Transform",output_img) 
cv.waitKey(0)
cv.destroyAllWindows()