import numpy as np
import cv2 as cv #pip install opencv-python,pip install opencv-contrib-python
import winsound
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
#i = 0
while True:
    
    ret, frame1 = cap.read()
    gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    
    ret, frame2 = cap.read()
    gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    ph1 = np.array(gray1).mean()
    ph2 = np.array(gray2).mean()
    if ph1-ph2 >0.5:
        #i = i+1
        winsound.Beep(1500  , 1000)
    
    
    cv.imshow('frame', gray1)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
