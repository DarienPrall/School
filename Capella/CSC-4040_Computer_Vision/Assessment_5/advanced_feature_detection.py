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
#process_marker_image()

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
def load_scene_images(folder_path):
    valid_exts = ['.jpg', '.jpeg']
    images = []
    filenames = []
    for file in os.listdir(folder_path):
        if os.path.splitext(file)[1].lower() in valid_exts:
            img = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
                filenames.append(file)
    print(f"Loaded {len(images)} images from {folder_path}.")
    return images, filenames

def match_images(marker_kp, marker_desc, scene_images, descriptor, out_dir):
    bf = cv2.BFMatcher()
    pos_dir = os.path.join(out_dir, 'Positive')
    neg_dir = os.path.join(out_dir, 'Negative')
    os.makedirs(pos_dir, exist_ok=True)
    os.makedirs(neg_dir, exist_ok=True)

    threshold = 10
    results = []

    for i, img in enumerate(scene_images[0]):
        kp, desc = descriptor.detectAndCompute(img, None)
        matches = bf.knnMatch(marker_desc, desc, k=2)

        # Testing Ration
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append(m)
        print(f"Image {i+1}: Found {len(good)} good matches.")

        is_match = len(good) > threshold
        img_name = scene_images[1][i]
        result_img = cv2.drawMatches(scene_images[0][i], kp, scene_images[0][i], kp, good, None)
        out_path = os.path.join(pos_dir if is_match else neg_dir, img_name)
        cv2.imwrite(out_path, result_img)

        results.append((img_name, is_match, len(good)))
        print(f"Processed {img_name}: {'Match' if is_match else 'No Match'} with {len(good)} good matches.")
    return results

# TESTING
#load_scene_images('/Users/darienprall/Downloads/resources-image-descriptors/image-descriptors_scenes')
# def quick_test():
#     marker_img, marker_kp, marker_desc = process_marker_image()
#     scene_folder = input("Enter path to the scene images folder: ")
#     scenes = load_scene_images(scene_folder)
#     out_folder = input("Enter output folder path for results: ")
#     method = input("Enter the descriptor method used earlier (AKAZE, ORB, SIFT): ")
#     descriptor = get_descriptor(method)
#     match_results = match_images(marker_kp, marker_desc, scenes, descriptor, out_folder)
#     manifest = input("Enter path to the ground truth manifest file: ")

#quick_test()

# --- SECTION 3: Evaluation Against Manifest ---
'''
To-Do:
1. Load ground truth manifest file.
2. Compare predicted match results to actual labels.
3. Count TP, FP, FN, TN values.
4. Print classification summary.
'''

def load_manifest(mainfest_path):
    marker = []
    no_marker = []

    with open(mainfest_path, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line == "CONTAINS MARKER":
                current_section = 'marker'
            elif line == "DOES NOT CONTAIN MARKER":
                current_section = 'no_marker'
            elif line:
                if current_section == 'marker':
                    marker.append(line)
                elif current_section == 'no_marker':
                    no_marker.append(line)
    manifest = {name: True for name in marker}
    manifest.update({name: False for name in no_marker})
    return manifest

def analyze_results(results, manifest_path):
    manifest = load_manifest(manifest_path)
    tp = fp = fn = tn = 0

    for name, predicted, _ in results:
        actual = manifest.get(name, False)
        if predicted and actual:
            tp += 1
        elif predicted and not actual:
            fp += 1
        elif not predicted and actual:
            fn += 1
        else:
            tn += 1

    print(f"True Positives: {tp}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Negatives: {tn}")
    return tp, fp, fn, tn
    
# --- MAIN WORKFLOW ---
'''
To-Do:
1. Load and process marker image.
2. Load all scene images.
3. Perform matching and save results.
4. Evaluate matches against manifest labels.
'''
if __name__ == "__main__":
    marker_img, marker_kp, marker_desc = process_marker_image()
    method = input("Enter the descriptor method used earlier (AKAZE, ORB, SIFT): ")
    descriptor = get_descriptor(method)

    scene_folder = input("Enter the path to the scene images folder: ")
    scenes = load_scene_images(scene_folder)
    out_folder = input("Enter output folder to save results: ")
    match_results = match_images(marker_kp, marker_desc, scenes, descriptor, out_folder)

    manifest = input("Enter path to manifest.txt: ")
    analyze_results(match_results, manifest)
    out_folder = input("Enter output folder path to save results: ")
