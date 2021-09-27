import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while(True):
    #camera ghi hinh
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Detecting face', frame)
    #Doi trong 1 miligiay hoac q de thoat
    
    if(cv2.waitKey(1) & 0xff == ord('q')):
        break;

cap.release()
cv2.destroyAllWindows()
