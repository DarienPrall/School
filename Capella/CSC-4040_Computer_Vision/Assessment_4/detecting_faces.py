import os
import cv2

# First I am creating a function to check if the file is an image. This function can be reused throughout the code
def check_if_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg'))

def read_images_from_directory():

    # Prompting the user for the directory path
    dir_path = input("Enter the path to the image directory: ")

    # Checking if the directory exists
    if not os.path.isdir(dir_path):
        print("Directory does not exist.")
        return []
    
    # Listing all image files in the directory
    images = [f for f in os.listdir(dir_path) if check_if_image(f)]
    print(f"Number of image files found: {len(images)}")

def main():
    read_images_from_directory()

if __name__ == "__main__":
    main()