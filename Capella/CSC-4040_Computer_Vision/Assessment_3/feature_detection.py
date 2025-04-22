import cv2
import numpy as np
import os

# Similar to my previous function, just slight adjustments with flow control
def load_image():
    path = input("Enter the path to the file image: ")
    if not path:
        print("No path entered. Please check the path and try again")
        return None
    else:
        image = cv2.imread(path)
        if image is None:
            print("Error loading image. Please check the file format.")
        else:
            print("Image successufully loaded")
            return image, path

#load_image Function Test   
#load_image()

# Function to display the image in which I implemented the WINDOW_NORMAL parameter. Thank you for this suggestion
def display_image(image):
    cv2.namedWindow("Image Viewer", cv2.WINDOW_NORMAL)    
    cv2.imshow("Image Viewer", image)
    # Propmt the user to enter edit mode
    print("Press any key to edit the image window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#display_image Function Test
'''
def test_display_image():
    image_paths = [
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_1.jpg",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_2.png",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_3.png"
    ]
    for path in image_paths:
        image = cv2.imread(path)
        if image is not None:
            display_image(image)
        else:
            print(f"Failed to load image at {path}")
test_display_image()
'''
        
def apply_transform(image, key):
    if key == ord('r'):
        print("Image rotated 90 degrees clockwise.")
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE), "Rotated"
    elif key == ord('f'):
        print("Image flipped horizontally.")
        return cv2.flip(image, 1), "Flipped"
    elif key == ord('b'):
        kernel_size = (5, 5)
        print(f"Applying GaussianBlur with a Kernel Size of: {kernel_size}")
        return cv2.GaussianBlur(image, kernel_size, 0), "Blurred"
    elif key == ord('c'):
        print("Canny applied to image.")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), "Canny"
    elif key == ord('o'):
        print("Applying boudning rectangle to image.")
        return outline_bounding_rectangle(image), "Contour-bounding-rectangle"
    return image, "Original"

def outline_bounding_rectangle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = image.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return result

# Tests for transformations
'''
def test_apply_transform():
    image_paths = [
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_1.jpg",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_2.png",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_base_3.png"
    ]

    for path in image_paths:
        image = cv2.imread(path)
        if image is not None:
            print(f"Testing transformations on image: {path}")

            # Rotating
            transformed_image, transform_name = apply_transform(image, ord('r'))
            print(f"Applied transform: {transform_name}")
            display_image(transformed_image)
            
            # Flipping
            transformed_image, transform_name = apply_transform(image, ord('f'))
            print(f"Applied transform: {transform_name}")
            display_image(transformed_image)
            
            # Blurring
            transformed_image, transform_name = apply_transform(image, ord('b'))
            print(f"Applied transform: {transform_name}")
            display_image(transformed_image)
            
            # Canny
            transformed_image, transform_name = apply_transform(image, ord('c'))
            print(f"Applied transform: {transform_name}")
            display_image(transformed_image)
            
            # Bounding Rectangle
            transformed_image, transform_name = apply_transform(image, ord('o'))
            print(f"Applied transform: {transform_name}")
            display_image(transformed_image)
        else:
            print(f"Failed to load image at {path}")

test_apply_transform()
'''

# Testing Bounding Rectangle on specified contour images
'''
def test_bounding_rectangle():
    image_paths = [
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_contour_base_1.jpg",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_contour_base_2.jpg",
        "/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/Assessment_3/Images/simple-features_contour_base_3.jpg"
    ]

    for path in image_paths:
        image = cv2.imread(path)
        outline_bounding_rectangle(image)
test_bounding_rectangle()
'''

# Saving the image to the current file path directory with specified formatting
def save_image(image, base_path, transform_name):
    base_name = os.path.splitext(os.path.basename(base_path))[0]
    filename = f"{base_name}-{transform_name}.png"
    cv2.imwrite(filename, image)
    print(f"Image saved as {filename}")


def main():
    image, path = load_image()
    if image is None:
        print("Error loading image. Please check path and try again.")
        return
    display_image(image)

    current_image = image.copy()
    transform_name = "Original"
    applied_transform = None

    while True:
        cv2.imshow("Image Viewer", current_image)
        print("Press key: [r]otate, [f]lip, [b]lur, [c]anny, [o]utline, [s]ave, or any other key to exit.")
        key = cv2.waitKey(0) & 0xFF

        if key in [ord('r'), ord('f'), ord('b'), ord('c'), ord('o')]:
            if applied_transform == key:
                current_image = image.copy()
                transform_name = "Original"
                applied_transform = None
            else:
                current_image, transform_name = apply_transform(image, key)
                applied_transform = key
        elif key == ord('s'):
            save_image(current_image, path, transform_name)
        else:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
#main()