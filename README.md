# Smart-Hand-Move-Detection-System
Immediate system locking using hand gestures , streamlined user experience resulting in reducing time spent on manual adjustments

Here is a step-by-step guide to install the necessary dependencies:

1. Install Python
Ensure you have Python installed. You can download it from python.org. Python 3.x is recommended.

2. Install OpenCV
OpenCV is required for capturing and processing video frames.

pip install opencv-python
3. Install cvzone
cvzone is a package that simplifies some common tasks in computer vision, including hand tracking.

pip install cvzone
4. Install mediapipe
Mediapipe is a framework for building perception pipelines and is used by cvzone for hand detection.

pip install mediapipe
5. Install ctypes
The ctypes library is part of the standard Python library, so no additional installation is needed. It's used for calling C functions from DLLs.


Troubleshooting
Camera Access: Ensure that your webcam is accessible and not being used by another application.
Permissions: Running the script that locks the workstation might require administrative privileges.
Environment: It’s a good practice to use a virtual environment to manage dependencies.