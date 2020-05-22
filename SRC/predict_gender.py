import cv2
import json
from keras.models import model_from_json
import numpy as np
from SRC.TransfImage import *
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)


gender_list = ['Male', 'Female']

def predict_gender(image,gender_model,blob=None):
     img_data=transfImag1(image)
     image = np.expand_dims(img_data,axis=0).reshape(1, 64, 64, 1)
     pred = gender_model.predict(image)[0]
     gender=gender_list[np.argmax(pred)]# 0=Male, 1=Female
     '''blob1 = cv2.dnn.blobFromImage(blob, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
     gender_model.setInput(blob1)
     gender_preds = gender_model.forward()
     gender = gender_list[gender_preds[0].argmax()]'''
     return str(gender)