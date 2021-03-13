from cv2 import cv2 as cv
import numpy as np

def empty(a):
    pass

capture = cv.VideoCapture(0)

capture.set(10,50)

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("Hue Min","TrackBars",0,179,empty) #Values are for red
cv.createTrackbar("Hue Max","TrackBars",6,179,empty)
cv.createTrackbar("Sat Min","TrackBars",169,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)



while True:
    isTrue, frame = capture.read()
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, h_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(frameHSV, lower, upper)
    imgResult = cv.bitwise_and(frame, frame, mask=mask)
    
    
    
    
    
    
    cv.imshow('Video', frame)
    cv.imshow("HSV", frameHSV)
    cv.imshow("Result", imgResult)
    if cv.waitKey(33) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
