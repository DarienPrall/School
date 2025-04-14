import os
import cv2


'''
SECTION 1: 
'''
# First I am creating a function to check if the file is an image. This function can be reused throughout the code
def check_if_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg'))

def read_images_from_directory(dir_path):
    
    # Checking if the directory exists
    if not os.path.isdir(dir_path):
        print("Directory does not exist. Please check the path and try again.")
        return []
    
    # Creating a list comprehension to count the number of image files in the directory
    image_files = [f for f in os.listdir(dir_path) if check_if_image(f)]

    # Printing the number of image files found
    print(f"Number of image files found: {len(image_files)}")

    # Reading each image
    images = []
    for file in image_files:
        full_path = os.path.join(dir_path, file)
        img = cv2.imread(full_path)
        if img is not None:
            images.append(img)
        else:
            print(f"Failed to read image: {file}")

def load_haar_cascade():
    xml_path = input("Enter the path to the Haar Cascade XML file: ")
    if not os.path.isfile(xml_path):
        print("Haar Cascade XML file does not exist. Please check the path and try again.")
        return None
    
    # Loading the Haar Cascade
    face_cascade = cv2.CascadeClassifier(xml_path)

    if face_cascade.empty():
        print("Failed to load Haar Cascade XML file. Please check the file and try again.")
        return None
    
    print("Haar Cascade loaded successfully.")
    return face_cascade

def setup_output_directory():
    output_path = input("Enter the path to the output directory and save classified images: ")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Output directory created at: {output_path}")

    positive_path = os.path.join(output_path, "Positives")
    negative_path = os.path.join(output_path, "Negatives")

    os.makedirs(positive_path, exist_ok=True)
    os.makedirs(negative_path, exist_ok=True)
    print("Output directories for Positives and Negatives are set up.")
    return positive_path, negative_path

def classify_and_save_images(image_dir, face_cascades, positive_path, negative_path):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    
    for idx, filename in enumerate(os.listdir(image_dir)):
        if not check_if_image(filename):
            continue

        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to read image: {filename}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected = False

        for i, cascade in enumerate(face_cascades):
            color = colors[i % len(colors)]
            faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            if len(faces) > 0:
                detected = True
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

        if detected:
            cv2.imwrite(os.path.join(positive_path, filename), img)
        else:
            cv2.imwrite(os.path.join(negative_path, filename), img)

'''
SECTION 2:
'''

def load_manifest():
    manifest_path = input("Enter the path to the manifest file: ")
    
    faces = []
    no_faces = []

    if not os.path.isfile(manifest_path):
        print("Manifest file does not exist. Please check the path and try again.")
        return faces, no_faces
    
    with open(manifest_path, 'r') as file:
        current_section = None

        for line in file:
            line = line.strip()
            if line == 'FACES:':
                current_section = 'faces'
            elif line == 'NO FACES:':
                current_section = 'no_faces'
            elif line:
                if current_section == 'faces':
                    faces.append(line)
                elif current_section == 'no_faces':
                    no_faces.append(line)
    return faces, no_faces

def analyze_results(positive_path, negative_path, faces, no_faces):
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    flase_negatives = 0

    for filename in os.listdir(positive_path):
        if filename in faces:
            true_positives += 1
        else:
            false_positives += 1

    for filename in os.listdir(negative_path):
        if filename in no_faces:
            true_negatives += 1
        else:
            flase_negatives += 1
    print("\nANALYSIS RESULTS:")
    print(f"True Positives: {true_positives}")
    print(f"False Positives: {false_positives}")
    print(f"True Negatives: {true_negatives}")
    print(f"False Negatives: {flase_negatives}\n")

# def test_section_2():
#     faces, no_faces = load_manifest()
#     image_dir = input("Enter the path to the image directory for testing: ")
#     positive_path = '/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_4/Images/Positives'
#     negative_path = '/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_4/Images/Negatives'
#     analyze_results(positive_path, negative_path, faces, no_faces)

def load_mupltiple_haar_cascades():
    xml_dir = input("Enter the path to the Haar Cascade XML directory: ")
    if not os.path.isdir(xml_dir):
        print("Haar Cascade XML directory does not exist. Please check the path and try again.")
        return None
    
    cascades = []
    for file in os.listdir(xml_dir):
        if file.lower().endswith('.xml'):
            xml_path = os.path.join(xml_dir, file)
            cascade = cv2.CascadeClassifier(xml_path)
            if cascade.empty():
                print(f"Failed to load Haar Cascade XML file: {file}. Please check the file and try again.")
            else:
                cascades.append(cascade)
                print(f"Haar Cascade loaded successfully: {file}.")
    return cascades

def main():
    image_dir = input("Enter the path to the image directory: ")
    images = read_images_from_directory(image_dir)
    #face_cascade = load_haar_cascade()
    face_cascade = load_mupltiple_haar_cascades()

    if face_cascade:
        positive_path, negative_path = setup_output_directory()
        classify_and_save_images(image_dir, face_cascade, positive_path, negative_path)
    
    faces, no_faces = load_manifest()
    # TEST FOR SECTION 2
    #print("\nMANIFEST DICTIONARY COUNTS:")
    #print(f"Number of Face Images: {len(faces)}")
    #print(f"Number of No Face Images: {len(no_faces)}")
    #print("\nIMAGE DICTIONARIES:")
    #print(f"Images with Faces: {faces}")
    #print(f"\nImages without Faces: {no_faces}\n")

    analyze_results(positive_path, negative_path, faces, no_faces)

if __name__ == "__main__":
    main()