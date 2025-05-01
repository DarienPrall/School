# DETECTING FACE MASKS
# - This program will be used for detecting face masks (mask/no mask) for building entry control. 
# - This is useful for personal, commercial, or industrial settings.
# DATASET CITATION
'''
Face Mask Detection. (2020). Larxel/CC0: Public Domain. Kaggle.

https://www.kaggle.com/datasets/andrewmvd/face-mask-detection
'''
# Import Libraries
import os
import shutil
import cv2

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Define Paths
images_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/archive/images')
output_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/archive/images/outputs')

# Define Output Folders
mask_directory = os.path.join(output_directory, 'Masks')
no_mask_directory = os.path.join(output_directory, 'No Masks')
os.makedirs(mask_directory, exist_ok = True)
os.makedirs(no_mask_directory, exist_ok = True)

# Load face mask detector and mask detector model


# Function to predict mask status

