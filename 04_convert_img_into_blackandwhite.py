import cv2 as cv

img = cv.imread("resources/kust.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

(thresh,b_w) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow("original",img)
cv.imshow("gray",gray)
cv.imshow("black and white",b_w)
cv.waitKey(0)
cv.destroyAllWindows()