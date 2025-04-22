import cv2
import numpy as np

#-----------------------------------------------------------------------------------
# 1.0 - LOADING THE IMAGE
'''
Code Explanation
- For this function, it will take an image_path and be read in with cv2.imread
- I have also include a check statement to ensure that the image can be loaded
'''
def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("The image file could not be loaded. Please check the file and try again")
        return None
    # Load Test
    #print("Image loaded successfully")
    return image

# 1.1 - TESTING FOR LOADING THE IMAGE
'''
Code Explanation
- I created a temporary screenshot image and copied its file path to store into a variable
- I then pass this variable into the load_image function to test a successfull image load
- I also enter a string into the function to test that it will through an error
'''

'''
test_image = r'/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/image-processing_color2greyscale_base.png'
load_image(test_image) # Successfull Test
load_image("Hello") # Throws error
'''
#-----------------------------------------------------------------------------------
# 2.0 - DISPLAYING THE IMAGE
'''
Code Explanation
- For this function, it will take an image as well as a deafult name for the window of "Image"
- The cv2.imshow will display the image and the window name provided
- The image will display and then immediately close so I need to add a waitKey function to close the image when a key is pressed
- I also only want one window open at a time so the destroyAllWindows() will close any OpenCV windows
'''
def display_image(image, window_name="Image"):
    cv2.imshow(window_name, image)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return key

# 2.1 - TESTS FOR DISPLAYING THE IMAGE
'''
Code Explanation
- A simple test function that passes in a test image to run the function
- There is error checking to ensure there is an image, if not, it will throw an error
'''

'''
def test_display_image():
    test_image = r'/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/image-processing_color2greyscale_base.png'
    image = load_image(test_image)
    if image is not None:
        print("Image loaded successfully")
        key = display_image(image, window_name = "Test Image")
        print(f"Key pressed during display: {key}")
    else:
        print("Test failed: Unable to load image.")

test_display_image()
'''
#-----------------------------------------------------------------------------------
# 3.0 - SAVING THE IMAGE
'''
Code Explanation
- This function will take an image and a file path to save the image to
- cv2.imwrite then uses the file path and stores the image properly
'''

def save_image(image, save_path):
    if image is None:
        print("Error loading image")
    else:
        cv2.imwrite(save_path, image)
        print(f"Image saved to {save_path}")

# 3.1 - TESTS FOR SAVING THE IMAGE
'''
Code Explanation
- For this test, I want to save the image.png to my desktop by using the correct path
'''
#test_image = r'/Users/darienprall/Documents/GitHub/CSCFPX4040_Computer_Vision/image-processing_color2greyscale_base.png'
#load_test_image = load_image(test_image)
#new_save_path = r'/Users/darienprall/Desktop/saved_image.png'
#save_image(load_test_image, new_save_path)

#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# 4.0 - PROCESSING THE IMAGE
'''
Code Explanation
- USER PROMPT: This function will prompt the use for the file path to the image using the input() function
- EMPTY IMAGE CHECK: It will also check to ensure the image is not blank
- Seeing that images in numpy are stored as an array, I can access the height, width, and number of color channels
    - shape[0] is height
    - shape[1] is width
    - shape[2] is color channels
- COLOR CHANNELS: I can check if the image has 3 dimensions, if it does, simply return the number of color channels by accessing the array 'shape[2]'
- However, if the length is not 3, that means it has to be 1 color channel, meaning it has to be a grayscale image
- RESOLUTION: To find the resolution, I simply show the height by width
- TOGGLE: I need to store the image to a grayscale variable for easy access. I can then create a boolean 'toggle' and use a while loop to toggle between the color image and grayscale image
- IMAGE SAVE: Simply askes the user for the path in which they want to save their new image
'''
def process_image():
    # User Prompt
    image_path = input("Enter the path to the image file: ")
    image = load_image(image_path)

    # Empty Image Check
    if image is None:
        print("No file path to image provided. Please enter a file path.")
        return

    # Color Channels
    print(f"Number of color channels: {image.shape[2] if len(image.shape) == 3 else 1}")

    # Resolution
    print(f"Resolution: {image.shape[0]} x {image.shape[1]}")

    # Toggle
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    print("Press 'c' to switch between color and gray. Press any other key to exit.")
    toggle = True
    while True:
        if toggle:
            key = display_image(image, "Image Display")
        else:
            key = display_image(grayscale, "Grayscale Image Display")
        
        if key == ord('c'):
            toggle = not toggle
        else:
            break

    # IMAGE SAVE
    save_path = input("Enter the path and filename to save the image: ")
    save_image(image, save_path)

# 4.1 - TESTS FOR PROCESSING THE IMAGE
'''
Code Explanation
- This test is a simple one as it should ask for the file name
- When entering a file name it should print the number of color channels as well as the resolution of the image
'''
#process_image()

#-----------------------------------------------------------------------------------
# 5.0 - APPLYING MASK
'''
Code Explanation
- PATH INPUTS: Simply asks the users for the base image and mask image
- ERROR CHECKING: I want to make sure the file paths are to a valid image. I wanted to specific which file had the error rather than roll it into one error statment
- IMAGE SIZING: Both the base and mask images need to be the same size for the mask to be applied correctly. If they are not the same, the mask will be resized to the base dimensions
- CONVERT TO GRAYSCALE (MASK): I will check if the mask image is in color, and if so, I will convert it to grayscale
- THRESHOLD: To ensure the masked image has values of either 0 or 255, nothing inbetween to allow proper masking
- DISPLAY IMAGES: I want all three images to output when the code is run
- SAVE MASKED IMAGE: I added user input to allow the user to save the masked_image where they want to
'''
def apply_mask():
    # Path Inputs
    base_image_path = input("Enter the path to the base image file: ")
    mask_image_path = input("Enter the path to the mask image file: ")

    base_image = load_image(base_image_path)
    mask_image = load_image(mask_image_path)

    # Error Checking
    if base_image is None:
        print("Error loading base_image. Please check the file path and try again.")
    
    if mask_image is None:
            print("Error loading mask_image. Please check the file path and try again.")

    # Image Sizing
    #print(f"Base Image Dimensions: {base_image.shape[0]} x {base_image.shape[1]}")
    #print(f"Mask Image Dimensions: {mask_image.shape[0]} x {mask_image.shape[1]}")
    if base_image.shape[:2] != mask_image.shape[:2]:
        mask_image = cv2.resize(mask_image, (base_image.shape[1], base_image.shape[0]))
    
    # Convert to Grayscale (Mask)
    #print(len(mask_image.shape))
    if len(mask_image.shape) == 3:
        mask_image = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)

    # Threshold
    _, mask_image = cv2.threshold(mask_image, 127, 255, cv2.THRESH_BINARY)

    masked_image = base_image.copy()
    masked_image[mask_image == 255] = (0, 0, 0)

    # Display Images
    cv2.imshow("Base Image", base_image)
    cv2.imshow("Mask Image", mask_image)
    cv2.imshow("Masked Image", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save Masked Image
    save_path = input("Enter a path to save the masked image to (filepath/name_of_file.png): ")
    if save_path != "":
        cv2.imwrite(save_path, masked_image)
        print(f"Masked image saved to {save_path}")

#-----------------------------------------------------------------------------------
# 5.1 - TESTS FOR APPLYING MASK
'''
Code Explanation
- The testing for this function is completed in the function itself along the way with print statements
'''

#apply_mask() # Successfull run
#-----------------------------------------------------------------------------------

if __name__ == "__main__":
    process_image()
    apply_mask()