# DETECTING FACE MASKS
# - This program will be used for detecting face masks (mask/no mask) for building entry control. 
# - This is useful for personal, commercial, or industrial settings.
'''
DATASET SOURCE
All photos used in this assessment are personal photos taken by Darien Prall
'''

# Import Libraries
import os

# Paths
masks_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/masks')
no_masks_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/outputs/no_masks')
raw_photos_directory = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos')
raw_photos_manifest = ('/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/images/raw_photos/raw_photos_manifest.txt')

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