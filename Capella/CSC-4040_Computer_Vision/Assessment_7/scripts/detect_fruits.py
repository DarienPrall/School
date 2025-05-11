import cv2
import os
import numpy as np

# Paths
dataset_directory = '/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/dataset'
output_directory = '/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/outputs'
log_file = '/Users/darienprall/Documents/GitHub/School/Capella/CSC-4040_Computer_Vision/Assessment_7/outputs/detection_log.txt'

os.makedirs(output_directory, exist_ok = True)

# HSV color ranges
def get_color_masks(hsv):
    # Apple: red (2 ranges)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    red_mask = cv2.bitwise_or(cv2.inRange(hsv, lower_red1, upper_red1),
                              cv2.inRange(hsv, lower_red2, upper_red2))

    # Orange: (adjust based on test images)
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])
    orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)

    return red_mask, orange_mask

# Detection function
def detect_fruit_in_image(image_path, filename):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    red_mask, orange_mask = get_color_masks(hsv)

    detected = []

    for mask, label, color in [(red_mask, "Apple", (0, 0, 255)), (orange_mask, "Orange", (0, 165, 255))]:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                detected.append(label)

    # Save output and return results
    out_path = os.path.join(output_directory, f"{filename}_labeled.jpg")
    cv2.imwrite(out_path, image)
    return detected

# Loop through dataset
def run_detection():
    with open(log_file, "w") as log:
        for subfolder in ["apples", "oranges", "mixed"]:
            folder_path = os.path.join(dataset_directory, subfolder)
            for filename in os.listdir(folder_path):
                if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    full_path = os.path.join(folder_path, filename)
                    detected = detect_fruit_in_image(full_path, os.path.splitext(filename)[0])
                    log.write(f"{filename}: {', '.join(detected) if detected else 'None'}\n")
                    print(f"{filename}: {', '.join(detected) if detected else 'None'}")

if __name__ == "__main__":
    run_detection()