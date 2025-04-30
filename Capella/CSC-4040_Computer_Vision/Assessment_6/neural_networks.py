#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Instructions
# 1.0 Load a pretrained neural network model created through TensorFlow.
# - 1.1  Utilize the OpenCV command cv2.dnn.readNetFromTensorflow.
# - 1.2 The neural nets utilize two input files, a .pb and .pbtxt.
# - 1.3 You may either prompt the user for the path to the files or you may hardcode the paths to the files. If you choose to hardcode the paths, it is recommended to use relative pathing from the same directory as the main .py file.

# 2.0 Prompt the user to enter in a path to a set of scene images.
# - 2.1 Open the path and read in all of the images within the folder.
# - 2.2 Load in only image files within the top level folder (do not need to recurse through sub folders).
# - 2.3 Print out the number of image files loaded.

# 3.0 Using the function cv2.dnn.blobFromImage.
# - 3.1 Convert each input image into a blob.
# - 3.2 Set the blob as input into the neural net.
# - 3.3 Retrieve the detection results from the neural net.

# 4.0 Set a threshold (between 0 and 1) for acceptable detections.
# - 4.1 Retrieve the detection score for each image’s detection results.
# - 4.2 Compare the score against your chosen threshold.
# - 4.3 For each passing detection (score greater than or equal to your threshold).
# - - 4.3.1 Obtain the bounding rectangle of the detection within the image.
# - - 4.3.2 Render the bounding rectangle onto the original image.

# 5.0 Print out the scene images into two folders, one for positive detections and one for negative detections.
# - 5.1 You may prompt the user for a path in which to create the output image folders.
# - 5.2 If a scene image contained at least one positive detection, write the scene image out into the positive folder.
# - 5.3 If a scene image had no detections, write the scene image out into the negative folder.
# - 5.4 The positive images should include the rectangle bound overlays for each detection made within the image.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import cv2
import os
from pathlib import Path

# Load manifest that maps image filenames to ground truth labels (face: True, no face: False)
def load_manifest(manifest_path):
    faces = []
    no_faces = []

    with open(manifest_path, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line == "FACES":
                current_section = 'faces'
            elif line == "NO FACES":
                current_section = 'no_faces'
            elif line:
                if current_section == 'faces':
                    faces.append(line)
                elif current_section == 'no_faces':
                    no_faces.append(line)

    # Combine both lists into a dictionary
    manifest = {name: True for name in faces}
    manifest.update({name: False for name in no_faces})
    return manifest

# ---------------------------- Step 1: Load Pretrained Neural Network ----------------------------
print("Loading neural network...")
model_path = ('/Users/darienprall/Downloads/resources-nn_models/opencv_face_detector_uint8.pb')
config_path = ('/Users/darienprall/Downloads/resources-nn_models/opencv_face_detector.pbtxt')
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
print("Neural network loaded successfully.")

# ---------------------------- Step 2: Get Input/Output Paths & Manifest ----------------------------
image_folder = input("Enter the path to the folder containing images: ").strip()

# Filter image files in the given folder (top-level only)
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(f"\nLoaded {len(image_files)} image files from {image_folder}.\n")

# Create output directories for positive and negative detections
output_base = input("\nEnter the path to the output folder: \n").strip()
positive_dir = os.path.join(output_base, "Positive")
negative_dir = os.path.join(output_base, "Negative")
os.makedirs(positive_dir, exist_ok=True)
os.makedirs(negative_dir, exist_ok=True)
print(f"\nOutput directories created: {positive_dir}, {negative_dir}\n")

# Load ground truth manifest
manifest_path = input("Enter path to manifest file: ").strip()
ground_truth = load_manifest(manifest_path)

# ---------------------------- Step 3: Image Processing and Detection ----------------------------
# Initialize counters for evaluation metrics
true_positives = false_positives = true_negatives = false_negatives = 0
threshold = 0.5  # Confidence threshold

# Iterate over each image for detection
for filename in image_files:
    img_path = os.path.join(image_folder, filename)
    image = cv2.imread(img_path)
    (h, w) = image.shape[:2]

    # Convert image to blob and feed to network
    blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    # Check detections above confidence threshold
    positive = False
    for i in range(detections.shape[2]):
        score = float(detections[0, 0, i, 2])
        if score >= threshold:
            positive = True
            # Draw bounding box on image
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # ---------------------------- Step 4: Evaluation ----------------------------
    prediction = positive
    actual = ground_truth.get(filename, False)

    # Update evaluation counters based on prediction vs actual
    if prediction and actual:
        false_positives += 1
    elif prediction and not actual:
        true_positives += 1
    elif not prediction and actual:
        false_negatives += 1
    elif not prediction and not actual:
        true_negatives += 1

    # ---------------------------- Step 5: Save Output ----------------------------
    output_path = os.path.join(positive_dir if prediction else negative_dir, filename)
    cv2.imwrite(output_path, image)

# ---------------------------- Final Summary ----------------------------
print("\nDetection Summary:")
print(f"True Positives: {true_positives}")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")
print(f"True Negatives: {true_negatives}")
