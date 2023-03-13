import cv2 as cv
img = cv.imread("resources/kust.jpg")
img = cv.resize(img,(400,200))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image: ",img)
cv.imshow("Gray Image: ",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
