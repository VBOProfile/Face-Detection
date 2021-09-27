import cv2
import numpy
import sqlite3
import os

#Insert hoac Update vao Sqlite
def insertOrUpdate(id, name, age, gender):

    conn = sqlite3.connect('/Users/vubao/OneDrive/Máy tính/SQLiteStudio/Data.db')
  
    query = "Select * from people Where ID = "+str(id)

    cusror = conn.execute(query)

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1

    if(isRecordExist == 0):
        query = "Insert into people(id, Name, Age, Gender) values("+str(id)+", '"+str(name)+"', '"+str(age)+"','"+str(gender)+"')"
    else:
        query = "Update people set Name = '"+str(name)+"', Age = '"+str(age)+"', Gender = '"+str(gender)+"'  Where ID = "+str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

#insert vao db
id = input("Enter your ID: ")
name = input("Enter your Name: ")
age = input("Enter your Age: ")
gender = input("Enter your Gender: ")
insertOrUpdate(id, name, age, gender)

#load tv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
sampleNum = 0

while(True):
    #camera ghi hinh
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    if not os.path.exists('dataSet'):
        os.makedirs('dataSet')
    #So anh lay tang dan
    sampleNum +=1
    #Luu anh da chup khuon mat vao file du lieu
    cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+ '.jpg', gray[y:y+h,x:x+w])

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    #Thoat ra neu so anh nhieu hon 208
    if sampleNum > 200:
        break
cap.release()
cv2.destroyAllWindows()
