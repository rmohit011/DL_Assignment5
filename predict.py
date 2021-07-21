#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.preprocessing import image

model = load_model('model.h5')

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename

        test_image = image.load_img(imagename, target_size=(150, 150))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

       # c = pd.read_csv("category.csv")
        c={0:'buildings',
 1:'forest',
 2:'glacier',
 3:'mountain',
 4:'sea',
 5:'street'}
        for i in range(len(result[0])):
            if result[0][i] == max(result[0]):
                clas=c[i]
                print(c[i])
                pred_score=result[0][i]*100
                pred_score=str(pred_score)+"%"
                print(result[0][i])
                print(i)
                a=[{clas:pred_score}]
                return a



