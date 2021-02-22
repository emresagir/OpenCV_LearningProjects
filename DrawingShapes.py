from cv2 import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jfif")
cv.imshow("Cat", img)

cv.waitKey(0)
