from cv2 import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale = 0.5):


    widht = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)
    dimensions = (widht, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



img = cv.imread("Photos\square.jfif")

kernel = np.ones((5,5), np.uint8)

#resizing and cropping
imgResized = cv.resize(img, (100,1000))
imgCropped = img[0:100, 100:300]


imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv.Canny(img, 150, 200)
imgDialation = cv.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv.erode(imgDialation, kernel, iterations=1)

cv.imshow("Image", img)
cv.imshow("GreyImage", imgGray)
cv.imshow("BlurImage", imgBlur)
cv.imshow("Canny", imgCanny)
cv.imshow("imgDialation", imgDialation)
cv.imshow("imgeroded", imgEroded)
cv.imshow("Resized Image",imgResized)
cv.imshow("CroppedImg", imgCropped)

cv.waitKey(0)