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
2. Ask user to select a descriptor method (AKAZE, ORB, SIFT, SURF).
3. Generate keypoints and descriptors using the selected method.
4. Display and optionally save the keypoint image.
'''
def get_descriptor(detector_type):

    # Normalizing the User Entry to Uppercase and Removes Whitespace
    #For testing
    #detector_type = input("Please enter the descriptor type (AKAZE, ORB, SIFT, SURF): ")
    detector_type = detector_type.upper().strip()

    # Check if the input is a string
    if not isinstance(detector_type, str):
        raise TypeError("The detector type must be a string. Please enter AKAZE, ORB, SIFT, or SURF.")
    
    # Check if the input is empty
    if not detector_type:
        raise ValueError("The detector type cannot be empty. Please enter AKAZE, ORB, SIFT, or SURF.")

    if detector_type == 'AKAZE':
        return cv2.AKAZE_create()
        #print("AKAZE descriptor selected.")
    elif detector_type == 'ORB':
        return cv2.ORB_create()
        #print("ORB descriptor selected.")
    elif detector_type == 'SIFT':
        return cv2.SIFT_create()
        #print("SIFT descriptor selected.")
    elif detector_type == 'SURF':
        return cv2.xfeatures2d.SURF_create()
        #print("SURF descriptor selected.")
    else:
        raise ValueError("The descriptor you selected is not supported. Please choose AKAZE, ORB, SIFT, or SURF.")
        #print("The descriptor you selected is not supported. Please choose AKAZE, ORB, SIFT, or SURF.")
    
# get_descriptor Function Testing
'''
- Uncomment the get_descriptor funciton below to test the function
- Remove detector_type argument when running the script
- Uncomment line 30
- Uncomment print statements in flow control
- Comment out return statements in flow control
- When finished reverse steps
'''
#get_descriptor()

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