import cv2 as cv
face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv.imread("resources/zoraiz.jpg")
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,1.1,4)
# Draw a Rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
img = cv.resize(img,(500,680))
cv.imshow("Original",img)
cv.waitKey(0)
cv.destroyAllWindows()

