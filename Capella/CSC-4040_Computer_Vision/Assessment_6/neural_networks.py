#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Instructions
# 1.0 Load a pretrained neural network model created through TensorFlow.
# - 1.1  Utilize the OpenCV command cv2.dnn.readNetFromTensorflow.
# - 1.2 The neural nets utilize two input files, a .pb and .pbtxt.
# - 1.3 You may either prompt the user for the path to the files or you may hardcode the paths to the files. If you choose to hardcode the paths, it is recommended to use relative pathing from the same directory as the main .py file.

# 2.0 Prompt the user to enter in a path to a set of scene images.
# - 2.1 Open the path and read in all of the images within the folder.
# - 2.2 Load in only image files within the top level folder (do not need to recurse through sub folders).
# - 2.3 Print out the number of image files loaded.

# 3.0 Using the function cv2.dnn.blobFromImage.
# - 3.1 Convert each input image into a blob.
# - 3.2 Set the blob as input into the neural net.
# - 3.3 Retrieve the detection results from the neural net.

# 4.0 Set a threshold (between 0 and 1) for acceptable detections.
# - 4.1 Retrieve the detection score for each image’s detection results.
# - 4.2 Compare the score against your chosen threshold.
# - 4.3 For each passing detection (score greater than or equal to your threshold).
# - - 4.3.1 Obtain the bounding rectangle of the detection within the image.
# - - 4.3.2 Render the bounding rectangle onto the original image.

# 5.0 Print out the scene images into two folders, one for positive detections and one for negative detections.
# - 5.1 You may prompt the user for a path in which to create the output image folders.
# - 5.2 If a scene image contained at least one positive detection, write the scene image out into the positive folder.
# - 5.3 If a scene image had no detections, write the scene image out into the negative folder.
# - 5.4 The positive images should include the rectangle bound overlays for each detection made within the image.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------