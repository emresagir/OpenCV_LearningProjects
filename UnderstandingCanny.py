from cv2 import cv2 as cv
import numpy as np

def empty(a):
    pass

capture = cv.VideoCapture(0)

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("First Min","TrackBars",0,333,empty) 
cv.createTrackbar("Sec Min","TrackBars",0,333,empty)


while True:
    isTrue, frame = capture.read()
    
    f_min = cv.getTrackbarPos("First Min", "TrackBars")
    s_min = cv.getTrackbarPos("Sec Min", "TrackBars")


    imgCanny = cv.Canny(frame, f_min, s_min)

    cv.imshow("CannyImg", imgCanny)
    cv.imshow("OriVid", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
