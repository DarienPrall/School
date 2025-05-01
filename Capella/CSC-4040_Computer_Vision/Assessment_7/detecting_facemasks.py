# DETECTING FACE MASKS
# - This program will be used for detecting face masks (mask/no mask) for building entry control. 
# - This is useful for personal, commercial, or industrial settings.
'''
DATASET SOURCE
All photos used in this assessment are personal photos taken by Darien Prall
'''

# Import Libraries
import os
import cv2
import numpy as np

# Paths
masks_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/masks')
no_masks_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/no_masks')
raw_photos_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos')
raw_photos_manifest = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/raw_photos_manifest.txt')
prototxt_path = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/resources-nn_models-2/opencv_face_detector.pbtxt')
model_path = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/resources-nn_models-2/opencv_face_detector_uint8.pb')

# Initialize the DNN-based face detector
net = cv2.dnn.readNetFromTensorflow(model_path, prototxt_path)

# Face Detection for Single Image

def detect_faces(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]

    # Preparing the image for DNN
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB = True, crop = False)

    # Set input for the network
    net.setInput(blob)

    # Get the face detections
    detections = net.forward()

    faces = []

    for i in range(detections.shape[2]):
        confidence = detections [0, 0, i, 2]

        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            # Append the box coordinates
            faces.append((startX, startY, endX, endY))

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    return faces, image


#=============================================================================================================================================================================================================================================================
# TEST 1: Newspaper Test (Detected 3 out of 4 faces)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_2036.jpeg')
# cv2.imshow('Detected Faces', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 2: Animal Test (Detected 0 faces)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_4717.jpeg')
# cv2.imshow('Detected Faces', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 3: No Mask Test (Detected 1 Face)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_5619.jpeg')
# cv2.imshow(f'Face(s) Detected: {len(faces)}', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 3: Mask Test (Detected 1 face)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_6450.jpeg')
# cv2.imshow(f'Face(s) Detected: {len(faces)}', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 4: Crowd Test (Detected 0 faces)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_6382.jpeg')
# cv2.imshow(f'Face(s) Detected: {len(faces)}', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 5: Looking away Test (Detected 0 Faces)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/381461_10151583071816131_136497063_n.jpg')
# cv2.imshow(f'Face(s) Detected: {len(faces)}', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TEST 6: Scenery Test (Detected 0 Faces)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# faces, image_with_faces = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_9085.jpeg')
# cv2.imshow('Detected Faces', image_with_faces)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f"Detected {len(faces)} faces")
# for face in faces:
#     print(f"Face bounding box: {face}")
#=============================================================================================================================================================================================================================================================

# Manifest
def load_manifest(manifest_path):
    
    # Define Arrays
    masks = []
    no_masks = []

    # Open path
    with open(manifest_path, 'r') as file:
        
        # Define Navigator
        current_section = None

        # Loop through every line
        for line in file:

            # Strip Whitespace
            line = line.strip()

            # Check if line is FACE MASK (As set up in the manifest)
            if line == "FACE MASK":
                current_section = 'face_mask'
            # Check if line is NO FACE MASK (As set up in the manifest)
            elif line == "NO FACE MASK":
                current_section = 'no_face_mask'

            elif line:

                # Append Mask files to array
                if current_section == 'face_mask':
                    masks.append(line)
                
                # Append No Face Mask to arry
                elif current_section == 'no_face_mask':
                    no_masks.append(line)

    # Print the content for review
    # print(f"Masks: {masks}")
    # print(f"No Masks: {no_masks}")
    return masks, no_masks

# Test load_manifest
# load_manifest(raw_photos_manifest)
