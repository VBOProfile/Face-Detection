import cv2
import numpy as np
import sqlite3
import os
import pickle
from PIL import Image

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cap=cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainningData.yml')
#Lay du lieu tu SQLite theo ID
def getProfile(id):
    conn = sqlite3.connect('/Users/vubao/OneDrive/Máy tính/SQLiteStudio/Data.db')
    query = "SELECT * FROM People WHERE ID=" +str(id)
    cusror = conn.execute(query)
    profile = None
    for row in cusror:
        profile = row
    conn.close()
    return profile
cap = cv2.VideoCapture(0)
#Tao kieu chu
fontface = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    #camera ghi hinh
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        id, confidence = recognizer.predict(roi_gray)
        if confidence < 40:
            profile = getProfile(id)
            #Tao doan thong tin anh
            if(profile != None):
                cv2.putText(frame,"Name: " +str(profile[1]),(x + 10, y + h + 30), fontface, 1, (0, 255, 0), 2)
                cv2.putText(frame,"Age: " +str(profile[2]),(x + 10, y + h + 60), fontface, 1, (0, 255, 0), 2)
                cv2.putText(frame,"Gender: " +str(profile[3]),(x + 10, y + h + 90), fontface, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Unknow", (x + 10, y + h + 30), fontface, 1, (0, 255, 0), 2)
    cv2.imshow('Image', frame)
    if(cv2.waitKey(1) == ord('q')):
        break;
cap.release()
cv2.destroyAllWindows()
