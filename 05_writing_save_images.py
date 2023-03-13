import cv2 as cv

img = cv.imread("resources/kust.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imwrite("resources/kust_gray.jpg",gray) # Saving image into a resourcew folder
(thresh,b_w) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imwrite("resources/bw.jpg",b_w)# Black and white
# cv.waitKey(0)
# cv.destroyAllWindows()