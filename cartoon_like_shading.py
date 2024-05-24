import cv2
import numpy as np
from math import sin, cos

ret = True
cam = cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
org = (50, 50)
font =  cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
thickness = 2
amin =  50
amax = 200

while ret:
    ret, frame = cam.read()
    if not ret:
        break

    
    edgeframe = cv2.Canny(frame, amin, amax)
    kernel = np.ones((2,2), np.uint8)
    edgeframe = cv2.dilate(edgeframe, kernel, iterations=1)

    edgeframe = cv2.bitwise_not(edgeframe)

    edgeframe = cv2.merge((edgeframe, edgeframe, edgeframe))

    # edgeframe = frame * edgeframe
    edgeframe = cv2.bitwise_and(frame, edgeframe)

    cv2.imshow('frame', edgeframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
