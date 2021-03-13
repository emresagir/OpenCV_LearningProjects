from cv2 import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier("FaceReco\haarcascade_frontalface.xml")


capture = cv.VideoCapture(0)

capture.set(10,50)

while True:
    isTrue, frame = capture.read()
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frameGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 4)


    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()