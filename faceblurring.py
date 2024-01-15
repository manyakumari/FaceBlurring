import cv2 as cv

img = cv.imread("group_pic2.png")
face_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
rect = face_cascade.detectMultiScale(img)
for x,y,w,h in rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(250,0,0))
    roi = img[y:y+h,x:x+w]
    roi = cv.GaussianBlur(roi,(15,15),30)
    img[y:y+roi.shape[0],x:x+roi.shape[1]]= roi
cv.imshow("image window",img)
cv.waitKey(0)
