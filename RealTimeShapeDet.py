from cv2 import cv2 as cv
import numpy as np

def getContours(frame, oriFrame):
    contours, hierarchy = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            cv.drawContours(oriFrame, cnt, -1, (0,0,255), 2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True) #need expl.
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if objCor == 3: objectType = "Tri"
            elif objCor == 4: objectType = "Rect"
            elif objCor == 5: objectType = "Pent"
            elif objCor == 6: objectType = "Hexa"
            else: objectType = "Circle"

            cv.rectangle(oriFrame, (x,y), (x+w, y+h), (255,0,0), 2)
            cv.putText(oriFrame, objectType, (x + (w//2) - 10, y + (h//2) - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 2)
    
def empty(a):
    pass



capture = cv.VideoCapture(0)


capture.set(10,50)

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("Hue Min","TrackBars",0,179,empty) 
cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    isTrue, frame = capture.read()
    copyOriginFrame = frame.copy()
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frameBlur = cv.GaussianBlur(frameHSV, (7,7), 1)
    
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

    imgResultCanny = cv.Canny(imgResult, 90,90)

    getContours(imgResultCanny, frame)

    cv.imshow('Video', frame)
    cv.imshow("Origin", copyOriginFrame)
    cv.imshow("ResultCanny", imgResultCanny)
    cv.imshow("imgResult", imgResult)

    

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
