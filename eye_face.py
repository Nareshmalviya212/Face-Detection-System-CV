import cv2

cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:/face data.xml")
eye_cascade = cv2.CascadeClassifier("C:/eyeglasses.xml")
while(True):
    ret,frame = cap.read()
    frame=cv2.resize(frame,(700,500))
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame)
    eye = eye_cascade.detectMultiScale(frame)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,0,255),2)
    for (a,b,c,d) in eye:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(255,255,0),2)
        

    
    cv2.imshow("face",frame)
    
    if cv2.waitKey(10)==ord("q"):
        break
    
cap.release()

cv2.destroyAllWindows()
