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
raw_photos_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos')
raw_photos_face_manifest = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/raw_photos_face_manifest.txt')
faces_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/faces')
no_faces_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/no_faces')
blurred_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/blurred')
prototxt_path = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/resources-nn_models-2/opencv_face_detector.pbtxt')
model_path = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/resources-nn_models-2/opencv_face_detector_uint8.pb')

# Initialize the DNN-based face detector
net = cv2.dnn.readNetFromTensorflow(model_path, prototxt_path)

# Face Detection for Single Image
def detect_faces(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]

    image = cv2.resize(image, (600, int(h * 600 / w)))
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

        if confidence > 0.3:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            # Append the box coordinates
            faces.append((startX, startY, endX, endY))

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(image, "Face", (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return faces, image

# DETECT FACES TEST 
# Image with Faces (SUCCESS)
# faces, img = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/704384902.618217.jpg')
# print(f"Total Faces Detected: {len(faces)}")
# cv2.imshow('Detected Faces', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Image without Faces (SUCCESS)
# faces, img = detect_faces('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/IMG_4717.jpeg')
# print(f"Total Faces Detected: {len(faces)}")
# cv2.imshow('Detected Faces', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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
detect_faces_in_folder(raw_photos_directory)

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
    # print(f"\nContains {len(no_face)} Without Faces: ")
    # for file in no_face:
    #     print(file)
    # return face, no_face

# Test load_face_manifest
#load_face_manifest(raw_photos_face_manifest)

# Comparing the Results
def compare_results_to_manifest(detection_results, manifest_path):
    # Load expected labels from manifest
    face_files, no_face_files = [], []
    current_section = None

    with open(manifest_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "FACE":
                current_section = 'face'
            elif line == "NO FACE":
                current_section = 'no_face'
            elif line:
                if current_section == 'face':
                    face_files.append(line)
                elif current_section == 'no_face':
                    no_face_files.append(line)

    # Initialize counters
    true_positive = false_positive = true_negative = false_negative = 0
    false_positives = []
    false_negatives = []

    for filename, detected_faces in detection_results.items():
        detected = len(detected_faces) > 0

        if filename in face_files:
            if detected:
                true_positive += 1
            else:
                false_negative += 1
                false_negatives.append(filename)
        elif filename in no_face_files:
            if detected:
                false_positive += 1
                false_positives.append(filename)
            else:
                true_negative += 1

    # Print summary
    print(f"\n----------FACE DETECTION RESULTS SUMMARY----------")
    print(f"True Positives:  {true_positive}")
    print(f"False Negatives: {false_negative}")
    print(f"True Negatives:  {true_negative}")
    print(f"False Positives: {false_positive}")

    print("\n# False Negatives:")
    for fn in false_negatives:
        print(f"- {fn}")

    print("\n# False Positives:")
    for fp in false_positives:
        print(f"- {fp}")

# Checking against the manifest
# results = detect_faces_in_folder(raw_photos_directory)
# compare_results_to_manifest(results, raw_photos_face_manifest)


def blur_faces(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Could not read: {filename}")
                continue

            (h, w) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
                                         (104.0, 177.0, 123.0), swapRB=True, crop=False)
            net.setInput(blob)
            detections = net.forward()

            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.3:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # Ensure the box is within image bounds
                    startX, startY = max(0, startX), max(0, startY)
                    endX, endY = min(w, endX), min(h, endY)

                    face_region = image[startY:endY, startX:endX]
                    face_region_blur = cv2.GaussianBlur(face_region, (99, 99), 30)
                    image[startY:endY, startX:endX] = face_region_blur

            save_path = os.path.join(output_folder, filename)
            cv2.imwrite(save_path, image)
            print(f"Blurred and saved: {filename}")

blur_faces(faces_directory, blurred_directory)
