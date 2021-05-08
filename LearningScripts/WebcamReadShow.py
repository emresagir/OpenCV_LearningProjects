from cv2 import cv2 as cv

#img = cv.imread('Photos/cat.jfif')

#cv.imshow('Cat', img)

capture = cv.VideoCapture(0)
img = cv.imread('Photos\cat.jfif')

capture.set(10,1000) #Brightness setting of webcam


def rescaleFrame(frame, scale = 0.5):


    widht = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)
    dimensions = (widht, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#img_resized = rescaleFrame(img)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    #cv.imshow('img', img_resized)
    cv.imshow('Video', frame)
    cv.imshow('Rescaled Video', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break



capture.release()
cv.destroyAllWindows()

