from cv2 import cv2 as cv
import numpy as np 

def rescaleFrame(frame, scale = 0.4):


    widht = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)
    dimensions = (widht, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

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


            

img = cv.imread("Photos\shapes.png")
img = rescaleFrame(img)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
getContours(imgCanny, img)



imgStack = stackImages(1, ([img, imgGray],[imgBlur, imgCanny]))
cv.imshow("Stack", imgStack)

cv.waitKey(0)
