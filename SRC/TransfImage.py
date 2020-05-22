import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/Users/silviaserafini/ironhack/PROGETTI/youtube-people-detector/SRC/haarcascade_frontalface_default.xml')
def transfImag(path):
    print ('transforming image from {}'.format(path))

    input_img=cv2.imread(path)
    input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(input_img, 1.25, 6)
    x,y,w,h = faces[0]
    img_data= input_img[y:y+h,x:x+w]
    img_data=cv2.resize(img_data,(64,64))
    
    img_data = np.stack(img_data)
    img_data = img_data / 255.0
    
    return img_data

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