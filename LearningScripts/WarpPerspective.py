from cv2 import cv2 as cv
import numpy as np

#corners of wanting image = 109,159 - 346,259 - 350,460 - 100,570
img = cv.imread("Photos\perspective.jfif")

width,height = 400,400
pts1 = np.float32([[109,159], [346,259], [100,570], [350,460]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgout = cv.warpPerspective(img, matrix, (width,height))

cv.imshow("Img", img)
cv.imshow("NewImg", imgout)

cv.waitKey(0)
