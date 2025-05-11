Face Detection and Blurring App

Description
This Python application detects human faces in images using OpenCV's DNN module, classifies images into "face" or "no face", and applies a Gaussian blur to anonymize detected faces. It’s designed for privacy-focused applications such as photo redaction or entry control systems.

Author
Darien Prall

Dataset
- All images used in this project are original and personally taken by the author.
- A manifest file (`raw_photos_face_manifest.txt`) categorizes images as:
  - `FACE`: Contains visible faces
  - `NO FACE`: No visible faces