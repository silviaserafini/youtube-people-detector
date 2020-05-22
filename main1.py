import cv2
import numpy as np
import pafy
import sys
import os 
from argparse import ArgumentParser
from SRC.predict_age import *
from SRC.predict_gender import *
from SRC.load_models import *
from SRC.is_new_face2 import *

parser = ArgumentParser(description="Welcome to the faces detector app")
parser.add_argument("--url" , help="the youtube url, 0 if camera", default="0")
args = parser.parse_args()

url=args.url

#url of the video to predict Age and gender
if url != '0':
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="mp4") 
    cap = cv2.VideoCapture(play.url) #youtubevideo
else:
    cap = cv2.VideoCapture(0) #camera

cap.set(3, 480) #set width of the frame
cap.set(4, 640) #set height of the frame


def video_detector( age_model , gender_model):
    #input: the models for age and gender
    #output: age and gender prediction
    print('loading video_detector...')
    font = cv2.FONT_HERSHEY_SIMPLEX
   
    while True:
        #detecting faces in the video frames
        ret, image = cap.read()
        face_cascade = cv2.CascadeClassifier('SRC/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        
        if(len(faces)>0):
            print("Found {} faces".format(str(len(faces))))
        else:
            print('no faces detected')
        
        #faces processing    
        for (x, y, w, h )in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            
            #Get Face
            face_img = gray[y:y+h, h:h+w].copy()  
            
            #Predict Gender
            gender = predict_gender(face_img, gender_model, image)
            print("Gender : " + gender)
            
            #Predict Age
            age = predict_age(face_img, age_model)
            print("Age Range : " + age)

            

            #write the predictions for age and gender close to the face
            overlay_text = "%s %s" % (gender, age)
            cv2.putText(image, overlay_text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('frame', image)
        
        #save the image to a dataframe
        report = register_face(image,age_model,gender_model)
        print(report)
        # if the `q` key was pressed, break from the loop
        ch = cv2.waitKey(1)
        if ch == 27 or ch == ord('q') or ch == ord('Q'):
            print(f'I have found {str(len(report))} faces')
            for entry in report:
                print(entry['age'],entry['gender'])
            break
           
	    

if __name__ == "__main__":
    age_model , gender_model = load_models()
    video_detector( age_model, gender_model)