import cv2
import numpy as np

ret = True
cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

outputframe = np.ndarray(shape=(height * 2, width * 2, 3))

org = (50, 50)
font =  cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
thickness = 2

while ret:
    ret, frame = cam.read()
    if not ret:
        break

    normalizedframe = frame / 255
    
    blue, green, red = cv2.split(normalizedframe)

    red   = cv2.merge((red, red, red))
    blue  = cv2.merge((blue, blue, blue))
    green = cv2.merge((green, green, green))

    red             = cv2.putText(red,             'red channel',    org, font, fontscale, (  0,   0, 255), thickness, cv2.LINE_AA)
    green           = cv2.putText(green,           'green channel',  org, font, fontscale, (  0, 255,   0), thickness, cv2.LINE_AA)
    blue            = cv2.putText(blue,            'blue channel',   org, font, fontscale, (255,   0,   0), thickness, cv2.LINE_AA)
    normalizedframe = cv2.putText(normalizedframe, 'original frame', org, font, fontscale, (255, 255, 255), thickness, cv2.LINE_AA)

    outputframe[height * 0:height * 1, width * 0:width * 1, :] = normalizedframe
    outputframe[height * 0:height * 1, width * 1:width * 2, :] = red
    outputframe[height * 1:height * 2, width * 0:width * 1, :] = green
    outputframe[height * 1:height * 2, width * 1:width * 2, :] = blue


    cv2.imshow('frame', outputframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()