import cv2 as cv
from cvzone import HandTrackingModule
import os
import time
import ctypes

cap = cv.VideoCapture(0)

detector = HandTrackingModule.HandDetector()

while True:
    ret, img = cap.read()
    hands, img = detector.findHands(img)
    
    cv.imshow("Hands Detected", img)
    
    for hand in hands:
        if detector.fingersUp(hand) == [0, 0, 0, 0, 0]:  # All fingers closed -> Palm detected
            print("Palm detected")
            ctypes.windll.user32.LockWorkStation()
    
    if (cv.waitKey(1) == ord('x')):
        break
    
cap.release()
cv.destroyAllWindows()