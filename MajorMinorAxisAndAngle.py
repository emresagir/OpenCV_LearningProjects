from cv2 import cv2 as cv
import numpy as np 
import time

def empty(a):
    pass

def getContours(imgCanny, imgOrg):
    contours, hierarchy = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) #SIMPLE olunca düz çizgilerin
                                                                                        #başına ve sonuna nokta koyuyor sadece
                                                                                        #Bu da memorydeki yükü azaltıyor.
    # epsilon = 0.1*cv.arcLength(cnt,True) #Second argument specify that is closed contour.
    # approx = cv.approxPolyDP(cnt,epsilon,True)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 10000:
            print("cnt area = ", area)
            cv.drawContours(imgOrg, cnt, -1, (255,0,0), 3)
            (x,y),(MA,ma),angle = cv.fitEllipse(cnt)
            ellipse = cv.fitEllipse(cnt)
            cv.ellipse(imgOrg, ellipse, (0,255,0), 2)
            print("angle", angle)   
            print("MA", MA)
            print("ma", ma)
            #time.sleep(0.2)
            return angle
    
capture = cv.VideoCapture(0)
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("First Min","TrackBars",100,333,empty) 
cv.createTrackbar("Sec Min","TrackBars",200,333,empty)

font = cv.FONT_HERSHEY_SIMPLEX


while True:
    isTrue, frame = capture.read()
    
    
    f_min = cv.getTrackbarPos("First Min", "TrackBars") #adjustable treshold values.
    s_min = cv.getTrackbarPos("Sec Min", "TrackBars")
    
    
    imgOrg = frame
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgCanny = cv.Canny(imgGray, f_min, s_min)

    angle = getContours(imgCanny, imgOrg)
    strAngle = str(angle)
    cv.putText(imgOrg, strAngle, (50,50), font, 1, (0,255,255), 2)
    

    cv.imshow("Video", imgCanny)
    cv.imshow("Original Video", imgOrg)


    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
