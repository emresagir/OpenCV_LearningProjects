from cv2 import cv2 as cv
import numpy as np 

capture = cv.VideoCapture(0)

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
            print("angle", angle)
    


while True:
    isTrue, frame = capture.read()
    
    imgOrg = frame
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgCanny = cv.Canny(imgGray, 90,90)

    getContours(imgCanny, imgOrg)


    cv.imshow("Video", imgCanny)
    cv.imshow("Original Video", imgOrg)


    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
