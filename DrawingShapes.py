from cv2 import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.5):


    widht = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)
    dimensions = (widht, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = np.zeros((512,512,3))
#img[100:120, 100:120] = 0,0,0

cv.line(img, (0,0), (int(img.shape[1]/2), int(img.shape[0]/2)), 
(255,255,0), 10)
cv.rectangle(img, (110,110), (500,400), (255,0,0), cv.FILLED)
cv.circle(img,(int(img.shape[1]/2), int(img.shape[0]/2)),50,(0,255,0),3 )
cv.putText(img, "Hello", (300,100), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 4)

cv.imshow("Img", img)



cv.waitKey(0)
