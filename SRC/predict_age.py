import cv2
import json
import numpy as np
from SRC.TransfImage import *
import codecs
import ast
from keras.models import model_from_json
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
#age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']

age_dic = {'0': '(0,3)', '1': '(4,7)', '2': '(8,14)', '3': '(15,21)', '4': '(22,33)', '5': '(34,43)', '6': '(44,53)', '7': '(54,100)'}
#“0–2”, “4–6”, “8–13”, “15–20”, “25–32”, “38–43”, “48–53” and “60-100”)
#age_dic ={0: '(0,2)', 1: '(15,20)', 2: '(25,32)', 3: '(33,47)', 4: '(48,53)', 5: '(4,6)', 6: '(60,100)', 7: '(8,13)'}
#with codecs.open('SRC/mapping.json', 'r', 'utf-8') as f:
     #output= ast.literal_eval(f.read())


def predict_age(image,age_model):
    img_data=transfImag1(image)
    
    image = np.expand_dims(img_data,axis=0).reshape(1, 64, 64, 1)
    pred = age_model.predict(image)[0]
    
    age=age_dic[str(np.argmax(pred))]#reverse coding of the output
    
    return str(age)
        