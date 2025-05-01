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
faces_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/faces')
no_faces_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/no_faces')
raw_photos_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos')
raw_photos_face_manifest = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/raw_photos_face_manifest.txt')
raw_photos_mask_manifest = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/raw_photos_mask_manifest.txt')
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

        # 0.5 condifence not capturing crowds or partial faces
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            # Append the box coordinates
            faces.append((startX, startY, endX, endY))

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    return faces, image

# DETECT FACES TEST (copy and paste from tests file)

# DETECT FACES IN FOLDER
def detect_faces_in_folder(folder_path):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            faces, image_with_faces = detect_faces(image_path)
            results[filename] = faces

            if len(faces) > 0:
                save_path = os.path.join(faces_directory, filename)
            else:
                save_path = os.path.join(no_faces_directory, filename)
            cv2.imwrite(save_path, image_with_faces)

            print(f"{filename}: Detected {len(faces)} face(s)")
    return results

# TESTING DETECTING FACES IN FOLDER
#detect_faces_in_folder(raw_photos_directory)

# Mask Manifest
def load_mask_manifest(manifest_path):
    
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
            if line == "MASK":
                current_section = 'mask'
            # Check if line is NO FACE MASK (As set up in the manifest)
            elif line == "NO MASK":
                current_section = 'no_mask'

            elif line:

                # Append Mask files to array
                if current_section == 'mask':
                    masks.append(line)
                
                # Append No Face Mask to arry
                elif current_section == 'no_mask':
                    no_masks.append(line)

    # PRINT THE CONTENT FOR REVIEW
    # print(f"Contains {len(masks)} Masks: ")
    # for file in masks:
    #     print(file)
    # print(f"\nContains {len(no_masks)} No Masks: ")
    # for file in no_masks:
    #     print(file)
    return masks, no_masks

# Test load_mask_manifest
#load_mask_manifest(raw_photos_mask_manifest)

# Face Manifest
def load_face_manifest(manifest_path):
    
    # Define Arrays
    face = []
    no_face = []

    # Open path
    with open(manifest_path, 'r') as file:
        
        # Define Navigator
        current_section = None

        # Loop through every line
        for line in file:

            # Strip Whitespace
            line = line.strip()

            # Check if line is FACE MASK (As set up in the manifest)
            if line == "FACE":
                current_section = 'face'
            # Check if line is NO FACE MASK (As set up in the manifest)
            elif line == "NO FACE":
                current_section = 'no_face'

            elif line:

                # Append Mask files to array
                if current_section == 'face':
                    face.append(line)
                
                # Append No Face Mask to arry
                elif current_section == 'no_face':
                    no_face.append(line)

    # PRINT THE CONTENT FOR REVIEW
    # print(f"Contains {len(face)} Faces: ")
    # for file in face:
    #     print(file)
    # print(f"\nContains {len(no_face)} No Faces: ")
    # for file in no_face:
    #     print(file)
    return face, no_face

# Test load_face_manifest
#load_face_manifest(raw_photos_face_manifest)

