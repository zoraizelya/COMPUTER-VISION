import cv2 as cv
img = cv.imread("resources/kust.jpg")
img = cv.resize(img,(800,600))
cv.imshow("Image: ",img)
cv.waitKey(0)
cv.destroyAllWindows()
