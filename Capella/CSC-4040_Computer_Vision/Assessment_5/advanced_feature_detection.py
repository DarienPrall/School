# Assessment 5: Image Descriptors for Pattern Matching
# Author: Darien
# CSC-FPX: 4040 Computer Vision
'''
# Description: 
This script loads a marker image, generates keypoints using selected descriptors, 
matches the keypoints in scene images, and analyzes detection accuracy.
'''

# Library Imports



# --- SECTION 1: Marker Image Descriptor Mapping ---
'''
To-Do:
1. Prompt user for marker image path and load it.
2. Ask user to select a descriptor method (AKAZE, ORB, SIFT, SURF).
3. Generate keypoints and descriptors using the selected method.
4. Display and optionally save the keypoint image.
'''



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