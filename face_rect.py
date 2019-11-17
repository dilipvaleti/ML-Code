import cv2
face_cascade=cv2.CascadeClassifier ("C:\\Users\\ss\\Desktop\\Data science material\\openCV\\haarcascade_frontalface_default.xml")
img1=cv2.imread("E:\\dilip photo 50kb.jpg")
gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img1=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3)
resized=cv2.resize(img1,(int(img1.shape[1]*2),int(img1.shape[0]*2)))
cv2.imshow("gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
