import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'

def getImagesWidthID(path):
    #lay duong dan cua du lieu anh trong thu muc
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    print(imagePaths)

    faces=[]
    IDs=[]

    for imagePaths in imagePaths:
        faceImg=Image.open(imagePaths).convert('L')
        faceNp=np.array(faceImg,'uint8')
        print(faceNp)
        #Cat de lay ID cua hinh anh
        ID=int(imagePaths.split('\\')[1].split('.')[1])

        faces.append(faceNp)
        IDs.append(ID)

        cv2.imshow('Training', faceNp)
        cv2.waitKey(5000)

        return faces,IDs
    
faces, IDs = getImagesWidthID(path)

#trainning
recognizer.train(faces, np.array(IDs))
#Luu vao file
if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
    
recognizer.save ('recognizer/trainningData.yml')

cv2.destroyAllWindows()
