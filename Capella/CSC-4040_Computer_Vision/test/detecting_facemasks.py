# DETECTING FACE MASKS
# - This program will be used for detecting face masks (mask/no mask) for building entry control. 
# - This is useful for personal, commercial, or industrial settings.
# DATASET CITATION
'''
Face Mask Detection. (2020). Larxel/CC0: Public Domain. Kaggle.

https://www.kaggle.com/datasets/andrewmvd/face-mask-detection
'''
# Import Libraries
import cv2
import os
import shutil
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load Pre-Trained mask detection model
model = load_model('mask_detector.h5')

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create output folders if they don't exist
os.makedirs('Masks', exist_ok = True)
os.makedirs('No Masks', exist_ok = True)

input_folder = ('/Users/darienprall/Downloads/archive/images')

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        mask_found = False

        for (x, y, w, h) in faces:
            face_img = img[y:y+h, x:x+w]
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            face_img = cv2.resize(face_img, (224, 224))
            face_img = img_to_array(face_img)
            face_img = np.expand_dims(face_img, axis = 0)
            face_img = face_img / 255.0

            (mask, no_mask) = model.predict(face_img)[0]

            if mask > no_mask:
                mask_found = True
                break

        if mask_found:
            shutil.copy(img_path, os.path.join('Masks', filename))
        else:
            shutil.copy(img_path, os.path.join('No Masks', filename))

print("Done sorting images")