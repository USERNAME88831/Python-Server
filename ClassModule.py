# %%
import keras.models
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import base64

CLASSES = ["Battery", "Biological", "Brown-Glass", "Cardboard", "Clothes", "Green-Glass", "Metal", "Paper", "Plastic", "Shoes", "Trash", "White-Glass"]

def __GetImageByBytes(RawImage):
    try:
        #print(RawImage)

        new_data = ""
        new_data = base64.b64decode(RawImage)
        array = np.fromstring(new_data, dtype=np.uint8)
        Image1 = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)
        Image2 = cv2.resize(Image1, (50, 50))
        return np.array(Image2).reshape(-1, 50, 50, 1)
    except Exception as e:
        print(e)

def __GetImage(ImagePath):
    try:
        Image1 = cv2.imread(os.path.join(ImagePath), cv2.IMREAD_GRAYSCALE)
        Image2 = cv2.resize(Image1, (50, 50))
        return np.array(Image2).reshape(-1, 50, 50, 1)
    except Exception as e:
        print(e)


def FindClass(RawImage="", type='bytes'):
    try:
        Img = None
        if type == 'path':
            Img = __GetImage(RawImage)
        else:
            Img = __GetImageByBytes(RawImage)
        model = keras.models.load_model("GarbageClassifier.model")
        PredictionArr = model.predict([Img])
        Place = np.where(PredictionArr == 1)[0][0]
        return CLASSES[Place]
    except Exception as e:
        print(e)



# %%



