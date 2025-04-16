# Assessment 5: Image Descriptors for Pattern Matching
# Author: Darien
# CSC-FPX: 4040 Computer Vision
'''
# Description: 
This script loads a marker image, generates keypoints using selected descriptors, 
matches the keypoints in scene images, and analyzes detection accuracy.
'''

# Library Imports
import cv2
import os
import numpy as np

from matplotlib import pyplot as plt


# --- SECTION 1: Marker Image Descriptor Mapping ---
'''
To-Do:
1. Prompt user for marker image path and load it.
2. Ask user to select a descriptor method (AKAZE, ORB, SIFT).
3. Generate keypoints and descriptors using the selected method.
4. Display and optionally save the keypoint image.
'''
def get_descriptor(detector_type):

    # Normalizing the User Entry to Uppercase and Removes Whitespace
    #For testing
    #detector_type = input("Please enter the descriptor type (AKAZE, ORB, SIFT): ")
    detector_type = detector_type.upper().strip()

    # Check if the input is a string
    if not isinstance(detector_type, str):
        raise TypeError("The detector type must be a string. Please enter AKAZE, ORB, or SIFT.")
    
    # Check if the input is empty
    if not detector_type:
        raise ValueError("The detector type cannot be empty. Please enter AKAZE, ORB, or SIFT.")

    if detector_type == 'AKAZE':
        print("AKAZE descriptor selected.")
        return cv2.AKAZE_create()
    elif detector_type == 'ORB':
        print("ORB descriptor selected.")
        return cv2.ORB_create()
    elif detector_type == 'SIFT':
        print("SIFT descriptor selected.")
        return cv2.SIFT_create()
    else:
        print("The descriptor you selected is not supported. Please choose AKAZE, ORB, or SIFT.")       
    
# get_descriptor Function Testing
'''
- Uncomment the get_descriptor funciton below to test the function
- Remove detector_type argument when running the script
- Uncomment line 30
- When finished reverse steps
'''
#get_descriptor()

def process_marker_image():

    marker_path = input("Please enter the path to the marker image: ")

    # Check if the file exists
    if not os.path.isfile(marker_path):
        print("File does not exist. Please check the path.")
        return None, None, None
    
    image = cv2.imread(marker_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Failed to load the image. Please check the path.")
        return None, None, None
    
    print("Choose a descriptor algorithm: AKAZE, ORB, SIFT")
    method = input("Enter your choice: ")
    descriptor = get_descriptor(method)
    keypoints, descriptors = descriptor.detectAndCompute(image, None)

    kp_image = cv2.drawKeypoints(image, keypoints, None, color = (0, 255, 0))
    cv2.imshow("Marker Keypoints", kp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the keypoint image with dynamic filename
    save_path = input("Enter a path to save marker keypoints image: ")
    method = method.upper()
    save_path = save_path + f"/{method}_keypoints.png"

    # Check if save_path already exists
    if os.path.exists(save_path):
        overwrite = input("An image in this filepath for this descriptor already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Image not saved.")
            return image, keypoints, descriptors
    else:
        print(f"Saving keypoints image to {save_path}")

    cv2.imwrite(save_path, kp_image)
    print(f"Keypoints image saved to {save_path}")
    return image, keypoints, descriptors

# process_marker_image Function Testing Part 1
'''
- Uncomment the process_marker_image funciton below to test the function
- Comment out line 85
- When finished reverse steps
'''
process_marker_image()

# --- SECTION 2: Scene Image Matching ---
'''
To-Do:
1. Load all valid scene images from a folder.
2. For each image, compute keypoints and descriptors.
3. Match with marker descriptors using brute force matcher.
4. Apply ratio test to filter good matches.
5. Decide match vs. no-match based on threshold.
6. Save result images in positive/negative subfolders.
'''


# --- SECTION 3: Evaluation Against Manifest ---
'''
To-Do:
1. Load ground truth manifest file.
2. Compare predicted match results to actual labels.
3. Count TP, FP, FN, TN values.
4. Print classification summary.
'''


# --- MAIN WORKFLOW ---
'''
To-Do:
1. Load and process marker image.
2. Load all scene images.
3. Perform matching and save results.
4. Evaluate matches against manifest labels.
'''