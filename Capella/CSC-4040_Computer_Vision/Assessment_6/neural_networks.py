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
import json
from pathlib import Path

# Step 1: Load the pretrained neural network model
pb_file = '/Users/darienprall/Downloads/resources-nn_models/opencv_face_detector_uint8.pb'
pbtxt_file = '/Users/darienprall/Downloads/resources-nn_models/opencv_face_detector.pbtxt'

# Check if files exist
if not os.path.exists(pb_file):
    print(f"Error: The file {pb_file} does not exist.")
    exit()
else:
    print(f"File {pb_file} exists.")

if not os.path.exists(pbtxt_file):
    print(f"Error: The file {pbtxt_file} does not exist.")
    exit()
else:
    print(f"File {pbtxt_file} exists.")

# Load the neural network using OpenCV
net = cv2.dnn.readNetFromTensorflow(pb_file, pbtxt_file)
print("Neural network model loaded successfully.")

# Step 2: Prompt user for class JSON file
class_json_file = input("Enter the path to the class JSON file (or press Enter to skip): ").strip()

if class_json_file:
    if os.path.exists(class_json_file):
        with open(class_json_file, 'r') as file:
            classes = json.load(file)
        print(f"Class file loaded. There are {len(classes)} classes.")
    else:
        print(f"Error: The file {class_json_file} does not exist.")
        exit()
else:
    classes = None  # No class file loaded, proceed without it.

# Step 3: Define paths to the datasets
dataset_1_folder = Path("/Users/darienprall/Downloads/resources-nn_dataset_1")
dataset_2_folder = Path("/Users/darienprall/Downloads/resources-nn_dataset_2")

# Step 5: Function to process images from a given folder
def process_images(scene_folder, net, threshold=0.3, classes=None):
    # Define valid image extensions
    valid_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    
    # Load only image files (top-level only)
    image_files = [f for f in scene_folder.iterdir() if f.suffix.lower() in valid_exts and f.is_file()]
    print(f"Number of image files loaded: {len(image_files)}")

    # Prepare output folders inside the dataset folder
    output_folder = scene_folder / 'detection_scenes'
    positive_folder = output_folder / 'Positive'
    negative_folder = output_folder / 'Negative'
    positive_folder.mkdir(parents=True, exist_ok=True)
    negative_folder.mkdir(parents=True, exist_ok=True)

    for img_path in image_files:
        # Load image
        image = cv2.imread(str(img_path))

        # Convert image to blob
        blob = cv2.dnn.blobFromImage(image, size=(300, 300), mean=(104.0, 177.0, 123.0))

        # Set blob as input to the neural net
        net.setInput(blob)

        # Run forward pass to get detection results
        detections = net.forward()

        positive_detection = False  # Flag to track if there is any positive detection

        # Loop through detections
        for i in range(detections.shape[2]):  # detections.shape[2] gives number of detected objects
            confidence = detections[0, 0, i, 2]  # confidence score for the i-th detection

            # If the detection confidence is above the threshold
            if confidence >= threshold:
                # Get bounding box coordinates
                x1, y1, x2, y2 = (detections[0, 0, i, 3] * image.shape[1],
                                  detections[0, 0, i, 4] * image.shape[0],
                                  detections[0, 0, i, 5] * image.shape[1],
                                  detections[0, 0, i, 6] * image.shape[0])

                # Convert to integer values
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Draw rectangle around the detected object
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                positive_detection = True

                # If class info is provided, check the class ID
                if classes:
                    class_id = int(detections[0, 0, i, 1])
                    if class_id < len(classes):
                        class_name = classes[class_id]
                        if class_name.lower() == 'person':
                            cv2.putText(image, class_name, (x1, y1 - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (247, 219,), 2)

        # Save the image in the appropriate folder
        if positive_detection:
            output_image_path = positive_folder / img_path.name
            cv2.imwrite(str(output_image_path), image)
            print(f"Processed positive image: {img_path.name}, saved to {output_image_path}")
        else:
            output_image_path = negative_folder / img_path.name
            cv2.imwrite(str(output_image_path), image)
            print(f"Processed negative image: {img_path.name}, saved to {output_image_path}")

# Step 6: Process both scene datasets
print("Processing Scene Set 1...")
process_images(dataset_1_folder, net, classes=classes)

print("Processing Scene Set 2...")
process_images(dataset_2_folder, net, classes=classes)

print("Processing complete.")

def load_manifest(mainfest_path):
    faces = []
    no_faces = []

    with open(mainfest_path, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line == "FACES:":
                current_section = 'faces'
            elif line == "NO FACES:":
                current_section = 'no_faces'
            elif line:
                if current_section == 'faces':
                    faces.append(line)
                elif current_section == 'no_faces':
                    no_faces.append(line)
    #print(f"Manifest loaded. Faces: {len(faces)}, No Faces: {len(no_faces)}")
    return faces, no_faces

#load_manifest('/Users/darienprall/Downloads/resources-nn_dataset_1/nn_dataset_1_face_manifest.txt')

def analyze_results():
    # Define the manifest file paths
    dataset_1_manifest = '/Users/darienprall/Downloads/resources-nn_dataset_1/nn_dataset_1_face_manifest.txt'
    dataset_2_manifest = '/Users/darienprall/Downloads/resources-nn_dataset_2/nn_dataset_2_face_manifest.txt'

    # Load the manifests
    dataset_1_faces, dataset_1_no_faces = load_manifest(dataset_1_manifest)
    dataset_2_faces, dataset_2_no_faces = load_manifest(dataset_2_manifest)

    # Define the folders for positive and negative detections
    dataset_1_positive_folder = '/Users/darienprall/Downloads/resources-nn_dataset_1/detection_scenes/Positive'
    dataset_1_negative_folder = '/Users/darienprall/Downloads/resources-nn_dataset_1/detection_scenes/Negative'
    dataset_2_positive_folder = '/Users/darienprall/Downloads/resources-nn_dataset_2/detection_scenes/Positive'
    dataset_2_negative_folder = '/Users/darienprall/Downloads/resources-nn_dataset_2/detection_scenes/Negative'

    # Analyze results for dataset 1
    print("==========================================")
    print("Analyzing results for Dataset 1...")
    dataset_1_results = analyze_dataset_results(dataset_1_positive_folder, dataset_1_negative_folder, dataset_1_faces, dataset_1_no_faces)

    # Analyze results for dataset 2
    print("==========================================")
    print("Analyzing results for Dataset 2...")
    dataset_2_results = analyze_dataset_results(dataset_2_positive_folder, dataset_2_negative_folder, dataset_2_faces, dataset_2_no_faces)

def analyze_dataset_results(positive_folder, negative_folder, manifest_faces, manifest_no_faces):
    true_positive = false_positive = false_negative = true_negative = 0

    for file in os.listdir(positive_folder):
        if file in manifest_faces:
            true_positive += 1
        else:
            false_positive += 1
    
    for file in os.listdir(negative_folder):
        if file in manifest_no_faces:
            true_negative += 1
        else:
            false_negative += 1
    
    print("Analysis Results:")
    print("---------------------------------")
    print(f"True Positives: {true_positive}")
    print(f"False Positives: {false_positive}")
    print(f"False Negatives: {false_negative}")
    print(f"True Negatives: {true_negative}")
    print("==================================")

    return true_positive, false_positive, false_negative, true_negative

# Call the analyze_results function to start the analysis
analyze_results()
