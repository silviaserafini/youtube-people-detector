import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/Users/silviaserafini/ironhack/PROGETTI/youtube-people-detector/SRC/haarcascade_frontalface_default.xml')


def transfImag1(image):
    try:
        faces = face_cascade.detectMultiScale(image, 1.25, 6)
        x,y,w,h = faces[0]
        img_data= input_img[y:y+h,x:x+w]
    except:
        img_data=image
        pass
    
    img_data=cv2.resize(img_data,(64,64))
    
    img_data = np.stack(img_data)
    img_data = img_data / 255.0
    
    return img_data