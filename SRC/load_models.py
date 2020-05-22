import cv2
import json
import numpy as np
from keras.models import model_from_json




def load_models():
    json_file = open('SRC/AgeModel_0.93_18-22-41.h5.json', 'r')
    #json_file = open('SRC/AgeModel_0.82_19-14-30.h5.json', 'r')
    age_model_json = json_file.read()
    json_file.close()
    age_model = model_from_json(age_model_json)
    # load weights into new model
    age_model.load_weights("SRC/AgeModel_0.93_18-22-41.h5")
    #age_model.load_weights("SRC/AgeModel_0.82_19-14-30.h5")
    
    json_file = open('SRC/GenderModel_0.98_18-22-21.h5.json', 'r')
    gender_model_json = json_file.read()
    json_file.close()
    gender_model = model_from_json(gender_model_json)
    # load weights into new model
    gender_model.load_weights("SRC/GenderModel_0.98_18-22-21.h5")
    #gender_model = cv2.dnn.readNetFromCaffe('deploy_gender.prototxt', 'gender_net.caffemodel')
    return age_model , gender_model