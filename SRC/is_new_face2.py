import cv2
import pandas as pd
import glob
import dlib
import scipy.misc
import face_recognition
from SRC.predict_age import *
from SRC.predict_gender import *
import numpy as np
from SRC.sql_functions import *
from SRC.database_creator import *
from SRC.transfImage1 import *
from datetime import datetime
from matplotlib import pyplot as plt




#to detect faces in images
face_detector = dlib.get_frontal_face_detector()
#to detect landmark points in faces and understand the pose/angle of the face
shape_predictor = dlib.shape_predictor('SRC/shape_predictor_68_face_landmarks.dat')
# face encodings (numbers that identify the face of a particular person)
face_recognition_model = dlib.face_recognition_model_v1('SRC/dlib_face_recognition_resnet_model_v1.dat')
# This is the tolerance for face comparisons
TOLERANCE = 0.5

def get_face_encodings(frame,age_model,gender_model): 
    #detect faces
    detected_faces = face_detector(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # Get pose/landmarks of  faces
    # Will be used as an input to the function that computes face encodings
    faces_img=[]

    for d in detected_faces:
        x, y, w, h= d.left(), d.top(), d.right()-d.left(), d.bottom()-d.top()
        face_img = gray[y:y+h, h:h+w].copy()
        faces_img.append(face_img)
    
    shapes_faces = [shape_predictor(frame, face) for face in detected_faces]
    print('shape_faces ',len(shapes_faces))
    try:
        genders=[predict_gender(face, gender_model,frame)for face in  faces_img]
        ages= [predict_age(face, age_model)for face in  faces_img]
    except:
        genders=['unknown'for face in detected_faces]
        ages=['unknown'for face in detected_faces]
        pass
    # For every face detected, compute the face encodings
    return [np.array(face_recognition_model.compute_face_descriptor(frame, face_pose, 1)) for face_pose in shapes_faces],ages,genders,faces_img

def compare_face_encodings(known_faces, face):
    # Calculate norm for the differences with each known face
    # Return an array with True/Face values based on whether or not a known face matched with the given face
    # A match occurs when the (norm) difference between a known face and the given face is less than or equal to the TOLERANCE value
    return (np.linalg.norm(known_faces - face, axis=1) <= TOLERANCE)

def find_match(known_faces_encoding, face_encoding):
    #checks if the new encoded face matches with any already registered face 
    matches=compare_face_encodings(known_faces_encoding,face_encoding).tolist()
    try:
        if matches.count(True)>0:
            return True
    except:
        return False
    return False


featurized_dataset = []

def register_face(frame,age_model,gender_model):
    #registers a all the new faces in the database
    current_encodings,ages,genders,faces_img=get_face_encodings(frame,age_model,gender_model)
    print('current_encodings',len(current_encodings))
    print('ages',len(ages))
    print('gender',len(genders))
    print('faces',len(faces_img))
    if len(featurized_dataset)==0 and len(current_encodings)>0:
        featurized_dataset.append({
            "face_id" : current_encodings[0],
            "gender" : genders[0],
            "age" : ages[0]
        })
        #saving
        path=f'OUTPUT/image{current_encodings[0][0]}{genders[0]}{ages[0]}.jpg'
        cv2.imwrite(path, faces_img[0])
        time=datetime.now()
        time=str(time)
        #adding the entry to a sql table
        add_face('exp1',path,ages[0],genders[0],time)
    add=True
    #compare the new face with those already present
    if len(featurized_dataset)>0:
        known_faces=[dic['face_id'] for dic in featurized_dataset]
        for i,face in enumerate(current_encodings):
            if find_match(known_faces, face):
                add=False
            if add :
                featurized_dataset.append({
                    "face_id" : face,
                    "gender" : genders[i],
                    "age" : ages[i]
                })
                time=datetime.now()
                time=str(time)
                #saving
                path=f'OUTPUT/image{face[0]}{genders[i]}{ages[i]}.jpg'
                cv2.imwrite(path, faces_img[i])
                #adding the entry to a sql table
                add_face('exp1',path,ages[i],genders[i],time)

    return featurized_dataset

#https://www.youtube.com/watch?v=tCCx9vEvOHs
#https://www.youtube.com/watch?v=iH1ZJVqJO3Y
#https://www.youtube.com/watch?v=r1MXwyiGi_U